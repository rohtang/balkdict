#balkdict


prerequisites:

python >= 2.7
web.py
python2.7-mysql
lxml



on a debian-based system; run 
apt-get install python-pip python-mysqldb

once completed, run
pip install beautifulsoup
pip install pyMySQLdb
pip install web.py
pip install lxml


currently, this relies on an mysql schema with the following characteristics:
--
-- Table structure for table `entries`
--

DROP TABLE IF EXISTS `entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` text NOT NULL,
  `description` text NOT NULL,
  `user` text NOT NULL,
  `datetime_added` datetime NOT NULL,
  `datetime_modified` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COMMENT='dicten, yo';


modify the connectionstring in db.py

to launch the devserver, simply run
python dict.py 8080

the website will be accessible through http://localhost:8080
