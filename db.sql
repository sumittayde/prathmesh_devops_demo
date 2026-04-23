/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - landmanagement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`landmanagement` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `landmanagement`;

/*Table structure for table `addland` */

DROP TABLE IF EXISTS `addland`;

CREATE TABLE `addland` (
  `ID` int(11) NOT NULL auto_increment,
  `sellername` varchar(255) default NULL,
  `Email` varchar(255) default NULL,
  `Phone` varchar(255) default NULL,
  `adharcard` varchar(255) default NULL,
  `serveyno` varchar(255) default NULL,
  `WARDno` varchar(255) default NULL,
  `Plotno` varchar(255) default NULL,
  `maplocation` varchar(255) default NULL,
  `filenamepath` varchar(255) default NULL,
  `filenamepathfordoc` varchar(255) default NULL,
  `state` varchar(255) default NULL,
  `city` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  `Landprice` varchar(255) default NULL,
  `status` varchar(255) default NULL,
  `admin` varchar(244) default 'not_verify',
  `buyer` varchar(244) default 'AVAILABLE',
  `user` varchar(255) default NULL,
  `likecount` varchar(255) default '0',
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `addland` */

insert  into `addland`(`ID`,`sellername`,`Email`,`Phone`,`adharcard`,`serveyno`,`WARDno`,`Plotno`,`maplocation`,`filenamepath`,`filenamepathfordoc`,`state`,`city`,`area`,`Landprice`,`status`,`admin`,`buyer`,`user`,`likecount`) values (1,'yash','yash@gmail.com','54421321516','789456612312','4012','5245','122','aroli','static/landdetails/service2.jpg','static/landdocumentfromseller/testimonials.jpg','Maharashtra','Thane','40cr','40000000','Land available','verify','AVAILABLE','yash','2'),(3,'roshan','ros@gmail.com','2324356787','234254353453','5225','632','268','mumbai','static/landdetails/service1.jpg','static/landdocumentfromseller/pro2.jpg','Chandigarh','Chennai','iltanpada','897824522','Land available','verify','NOT AVAILABLE','roshan','2'),(4,'admin','amit@gmail.com','23243567878','559566598223','4012','242','1333','mumbai','static/landdetails/bg_1.jpg','static/landdocumentfromseller/bg_1.jpg','Chandigarh','Kanpur','xd','45121654821','Land available','verify','AVAILABLE','yash','3'),(5,'amit','amit@gmail.com','7282828282','559566598223','4012','5245','789','mumbai','static/landdetails/about.jpg','static/landdocumentfromseller/bg_2.jpg','Bihar','Jaipur','vihar','789456123','Land available','not_verify','AVAILABLE','roshan','0');

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(255) NOT NULL,
  `emailid` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`emailid`,`password`) values ('Admin','admin@gmail.com','Admin');

/*Table structure for table `bankdetails` */

DROP TABLE IF EXISTS `bankdetails`;

CREATE TABLE `bankdetails` (
  `nameofcard` varchar(255) default NULL,
  `cardnumber` varchar(255) default NULL,
  `expmonth` varchar(255) default NULL,
  `expyear` varchar(255) default NULL,
  `CVV` varchar(255) default NULL,
  `zip_code` varchar(255) default NULL,
  `user` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bankdetails` */

insert  into `bankdetails`(`nameofcard`,`cardnumber`,`expmonth`,`expyear`,`CVV`,`zip_code`,`user`) values ('yash salvi','4561231234556','may','2022','3698','1584895','yash'),('dfhfgj','45678956510','dxcvvcv','4564','cvcv','123456','roshan');

/*Table structure for table `contact1` */

DROP TABLE IF EXISTS `contact1`;

CREATE TABLE `contact1` (
  `username` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `subject` longtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `contact1` */

insert  into `contact1`(`username`,`email`,`phone`,`subject`) values ('admin','a@gmail.com','45678912535','jolaofsjd;lkspoj;gtg');

/*Table structure for table `request1` */

DROP TABLE IF EXISTS `request1`;

CREATE TABLE `request1` (
  `id` int(255) NOT NULL auto_increment,
  `user` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `filepath` varchar(255) default NULL,
  `maplocation` varchar(255) default NULL,
  `landprice` varchar(255) default NULL,
  `request` varchar(255) default NULL,
  `status` varchar(255) default 'REQUEST ACCEPT',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request1` */

insert  into `request1`(`id`,`user`,`email`,`filepath`,`maplocation`,`landprice`,`request`,`status`) values (1,'yash','yash@gmail.com','static/landdetails/service2.jpg','aroli','40000000','yash',' ACCEPT '),(2,'roshan','ros@gmail.com','static/landdetails/service1.jpg','mumbai','897824522','roshan',' ACCEPT '),(3,'roshan','ros@gmail.com','static/landdetails/service1.jpg','mumbai','897824522','roshan','REQUEST ACCEPT'),(4,'roshan','yash@gmail.com','static/landdetails/service2.jpg','aroli','40000000','yash',' ACCEPT '),(5,'roshan','amit@gmail.com','static/landdetails/bg_1.jpg','mumbai','45121654821','yash',' ACCEPT '),(6,'roshan','amit@gmail.com','static/landdetails/bg_1.jpg','mumbai','45121654821','yash','REQUEST ACCEPT'),(7,'roshan','yash@gmail.com','static/landdetails/service2.jpg','aroli','40000000','yash','REQUEST ACCEPT'),(8,'roshan','amit@gmail.com','static/landdetails/bg_1.jpg','mumbai','45121654821','yash','REQUEST ACCEPT');

/*Table structure for table `sellerregistration` */

DROP TABLE IF EXISTS `sellerregistration`;

CREATE TABLE `sellerregistration` (
  `username` varchar(255) NOT NULL,
  `emailid` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `sellerregistration` */

insert  into `sellerregistration`(`username`,`emailid`,`password`) values ('yash','yash@gmail.com','yash'),('roshan','rosh@gmail.com','r'),('yash','yash@gmail.com','yash');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
