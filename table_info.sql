--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` text NOT NULL,
  `smessage` text NOT NULL,
  `image` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`(7)) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Data for table `events`
--


INSERT INTO `events` (`id`, `type`, `smessage`, `image`) VALUES
(1, 'Skeletons', 'Skeleton Surprise', 'skeleton.png'),
(2, 'Blobs', '..', 'Ooze.png'),
(3, 'Foresttrolls', 'The ground is shaking', 'troll.png'),
(4, 'Wolves', 'You are being hunted', 'wolf.png'),
(5, 'Surtlings', 'There\'s a smell of sulfur in the air', 'surtling.png'),
(6, 'Eikthyrnir', 'Meadows', 'Eikthyr.png'),
(7, 'GDKing', 'Black Forest', 'The_Elder.png'),
(8, 'Bonemass', 'Swamp', 'Bonemass.png'),
(9, 'Dragonqueen', 'Mountain', 'Moder.png'),
(10, 'GoblinKing', 'Plains', 'Yagluth.png'),
(11, 'army_eikthyr', 'Eikthyr rallies the creatures of the forest', 'Boar.png'),
(12, 'army_theelder', 'The forest is moving...', 'Greydwarf.png'),
(13, 'army_bonemass', 'A foul smell from the swamp', 'Draugr.png'),
(14, 'army_moder', 'A cold wind blows from the mountains', 'Drake.png'),
(15, 'army_goblin', 'The horde is attacking', 'Fuling.png');

--
-- Table structure for table `exstats` (Optinal Table only needed if enabling Extra Server Info in Config)
--

CREATE TABLE `exstats` (
  `id` int NOT NULL AUTO_INCREMENT,
  `savezdos` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `savesec` varchar(10) DEFAULT NULL,
  `worldsize` varchar(10) DEFAULT NULL,
  `serverversion` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `plusversion` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `gameday` int DEFAULT NULL,
  `timestamp` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Data for table `events`
--

INSERT INTO `exstats` VALUES (1,'NULL','NULL','NULL','NULL','NULL','NULL',1616448381);

--
-- Table structure for table `players`
--

CREATE TABLE `players` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(100) NOT NULL,
  `deaths` int NOT NULL DEFAULT '0',
  `valid` varchar(50) DEFAULT NULL,
  `startdate` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `playtime` bigint DEFAULT '0',
  `jointime` bigint DEFAULT NULL,
  `ingame` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `users` (`user`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `serverstats`
--

CREATE TABLE `serverstats` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(20) DEFAULT NULL,
  `timestamp` bigint DEFAULT NULL,
  `users` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `timestamp` (`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
