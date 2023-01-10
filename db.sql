/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - face_mask
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`face_mask` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `face_mask`;

/*Table structure for table `attendence` */

DROP TABLE IF EXISTS `attendence`;

CREATE TABLE `attendence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`,`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

insert  into `attendence`(`id`,`sid`,`date`,`attendance`) values 
(1,7,'2021-09-21',1),
(2,6,'2021-09-20',1),
(3,7,'2021-09-20',0),
(4,6,'2021-09-21',0),
(5,6,'2021-09-27',1),
(6,8,'2021-09-21',0),
(7,8,'2021-09-20',0),
(8,7,'2021-09-27',0),
(9,8,'2021-09-27',0),
(10,11,'2021-09-21',0),
(11,11,'2021-09-20',0),
(12,11,'2021-09-27',0),
(13,44,'2021-09-21',0),
(14,42,'2021-09-21',0),
(15,44,'2021-09-20',0),
(16,42,'2021-09-20',0),
(17,44,'2021-09-27',0),
(18,42,'2021-09-27',0),
(19,48,'2021-09-21',0),
(20,48,'2021-09-20',0),
(21,48,'2021-09-27',0);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`fid`,`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`sid`,`feedback`,`date`) values 
(1,3,'5uip','2021-09-22'),
(2,2,'huua','2021-09-24'),
(3,2,'rrrr','2021-09-24'),
(4,2,'podo','2021-09-24'),
(5,2,'daaa','2021-09-24'),
(6,3,'good','2021-10-01'),
(7,3,'perfect','2021-10-01');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'sales','sales','staff'),
(3,'hilal','hilalp','staff'),
(19,'pppp','900900','staff'),
(21,'adminjyg','FGHF','staff'),
(28,'admind','dfgdg','staff'),
(30,'sadad','wwwww','staff'),
(33,'sss','sssss','staff'),
(35,'ddddddd','123412341243','staff'),
(37,'sefwe','ewrwr','staff'),
(40,'qqqq','qqqq','staff'),
(42,'shemi','shemiasi','staff'),
(44,'basil','123456','staff'),
(48,'hilalwafa','hilalwafa','staff');

/*Table structure for table `mask_violation` */

DROP TABLE IF EXISTS `mask_violation`;

CREATE TABLE `mask_violation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `mask_violation` */

insert  into `mask_violation`(`id`,`date`,`image`,`status`,`uid`) values 
(1,'2021-09-28 12:40:10','20210928_123942.jpg','pending',8);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(50) DEFAULT NULL,
  `date` varchar(43) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`nid`,`notification`,`date`) values 
(8,'shemeem is very bad gay','2021-09-30');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `SID` int(11) NOT NULL AUTO_INCREMENT,
  `LID` int(11) NOT NULL,
  `FNAME` varchar(50) DEFAULT NULL,
  `LNAME` varchar(50) DEFAULT NULL,
  `GENDER` varchar(50) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `QUALIFICATION` varchar(50) DEFAULT NULL,
  `POST` varchar(50) DEFAULT NULL,
  `PHONE` bigint(20) DEFAULT NULL,
  `EMAIL` varchar(50) DEFAULT NULL,
  `IMAGE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SID`,`LID`),
  UNIQUE KEY `EMAIL` (`EMAIL`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`SID`,`LID`,`FNAME`,`LNAME`,`GENDER`,`DOB`,`QUALIFICATION`,`POST`,`PHONE`,`EMAIL`,`IMAGE`) values 
(32,42,'shameem','sam','male','2001-05-25','degree','thootha',9605395837,'shameemck2002@gmail.com','2021_07_21_09_24_IMG_8674.JPG'),
(33,44,'BASIL ','T P','male','1999-08-01','degree','ALANALLUR',8606476638,'mohammedbasiltp9468@gmail.com','2021_08_25_16_23_IMG_3246.JPG'),
(35,48,'hilal wafa','p','male','2000-06-08','degree','thelakkad',8789858653,'hilalwafa@gmail.com','2020_11_17_15_32_IMG_0021.JPG');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `work` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` varchar(43) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`work_id`,`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`work_id`,`sid`,`work`,`description`,`date`,`status`) values 
(1,3,'rrr','gttgtgere','2021-09-20','dddd'),
(3,4,'kooli','kdk','2021-09-20','pending'),
(7,2,'25','okkkkkkkkkkk','2021-09-21','eegyh'),
(8,7,'drgt','','2021-09-21','pending'),
(9,42,'marketing manager','.............................','2021-09-30','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
