import os, re, config, sys, mysql.connector
from colorama import Fore, Style, init
from mysql.connector import errorcode
from config import SQL_HOST as MYhost
from config import SQL_PORT as MYport
from config import SQL_USER as MYuser
from config import SQL_PASS as MYpass
from config import SQL_DATABASE as MYbase
from config import vplusfile

section = '^\[([\w]*)\]$'
settings = '^(\w*) = (\w*)$'

TABLES = {}
TABLES['vplus'] = (
    "CREATE TABLE `vplus` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `section` varchar(75) DEFAULT NULL,"
    "  `enabled` varchar(75) DEFAULT NULL,"
    "  `option1` varchar(75) DEFAULT NULL,"
    "  `settings` varchar(75) DEFAULT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

def mydbconnect():
    global mydb
    mydb = mysql.connector.connect(
        host=MYhost,
        user=MYuser,
        password=MYpass,
        database=MYbase,
        port=MYport,
        )
    try:
        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print(Fore.GREEN + "Connected to MySQL database... MySQL Server version ", db_Info + Style.RESET_ALL)
    except mysql.connector.Error as err:
        print(Fore.RED + err + 'From MySQL database' + Style.RESET_ALL)

mydbconnect()

def maketable():
    mycursor = mydb.cursor()
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(Fore.GREEN + "Creating table {}: ".format(table_name), end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(Fore.RED + "already exists. Droping table and trying again." + Style.RESET_ALL)
                sql = "DROP TABLE vplus"
                mycursor.execute(sql)
                maketable()
            else:
                print(Fore.RED + err.msg + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "OK" + Style.RESET_ALL)
    mycursor.close()

def mainloop():
    try:
        plusconf = open(vplusfile, mode="r")
        Lines = plusconf.readlines()
        print(Fore.GREEN + "Adding Valheim Plus settings to table vplus" + Style.RESET_ALL)
        mycursor = mydb.cursor()
        section1 = "ValheimPlus"
        enabled1 = 0
        option = 0
        setting = 0
        for line in Lines:
            insert = 0
            if(re.search(section, line)):
                section1 = re.search(section, line).group(1)
                insert = 0
                enabled1 = 0
                option = 0
                setting = 0
            if(re.search(settings, line)):
                what = re.search(settings, line).group(1)
                setting = re.search(settings, line).group(2)
                insert = 1
                if what == "enabled":
                    enabled1 = setting
                else:
                    option = what
            if insert == 1:
                sql = """INSERT INTO vplus (section, enabled, option1, settings) VALUES ('%s', '%s', '%s', '%s')""" % (section1, enabled1, option, setting)
                mycursor.execute(sql)
                mydb.commit()
        plusconf.close()
        mycursor.close()
        print(Fore.GREEN + "Done" + Style.RESET_ALL)
    except IOError:
        print(Fore.RED + 'Could not read Valheim Plus config file. Please check config.py' + Style.RESET_ALL)

maketable()
mainloop()
mydb.close()
exit()
