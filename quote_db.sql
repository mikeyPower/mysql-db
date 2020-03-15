CREATE DATABASE IF NOT EXISTS mickpower$quotes;

--
-- Table structure for table `quotes`
--
DROP TABLE IF EXISTS `quotes`;

CREATE TABLE `quotes` (
  `quote_id` int(11) NOT NULL AUTO_INCREMENT,
  `quote` varchar(255) NOT NULL,
  `quote_date` date DEFAULT NULL,
  `author` varchar(255) NOT NULL,
  PRIMARY KEY (`quote_id`),
  UNIQUE KEY `date_unique` (`quote_date`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
