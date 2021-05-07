# ValheimPlus-Discord_Bot
Valheim Plus discord bot based off of [ckbaudio's valheim-discord-bot](https://github.com/ckbaudio/valheim-discord-bot)

## Setup:
**Working MySQL server is needed for this bot.**  
`table_info.sql` Has Table info for the database  
`pip install -r requirements.txt` To install Pyhton requirements.

## [config.py](code/config.py)
Edit this file with your info. Setting should be self-explanitory.  

Add `-logfile /location/to/file.log` to your start command to get a logfile.  

**Warning:** Using the `BepInEx/LogOutput.log` file will not work  

For `WORLDSIZE` user running the bot must have read permissions to the world.db.old file

## [dbsetup.py](code/dbsetup.py)
Tables and data for the MySQL database.  

**Warning: Set up the config.py before running this**  
Run `python3 dbsetup.py` from the code dir to create tables.

## Usage:
`python3 plusbot.py` While in the `code` dir.  
`nohup python3 plusbot.py &` Too run in background.  
Or you can create a service to run `plusbot.py` under systemd  

**help** Shows available commands

## [Optional:](optional)
Check the optional dir for addons

### Example Output:
![](example/example.png)

## Changes:
- March 4, 2021: Major rewrite
