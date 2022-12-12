/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 5.7.36 : Database - onlineshopping
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`onlineshopping` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `onlineshopping`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add customer',7,'add_customer'),
(26,'Can change customer',7,'change_customer'),
(27,'Can delete customer',7,'delete_customer'),
(28,'Can view customer',7,'view_customer'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add master',9,'add_master'),
(34,'Can change master',9,'change_master'),
(35,'Can delete master',9,'delete_master'),
(36,'Can view master',9,'view_master'),
(37,'Can add order',10,'add_order'),
(38,'Can change order',10,'change_order'),
(39,'Can delete order',10,'delete_order'),
(40,'Can view order',10,'view_order'),
(41,'Can add shop',11,'add_shop'),
(42,'Can change shop',11,'change_shop'),
(43,'Can delete shop',11,'delete_shop'),
(44,'Can view shop',11,'view_shop'),
(45,'Can add reviews',12,'add_reviews'),
(46,'Can change reviews',12,'change_reviews'),
(47,'Can delete reviews',12,'delete_reviews'),
(48,'Can view reviews',12,'view_reviews'),
(49,'Can add products',13,'add_products'),
(50,'Can change products',13,'change_products'),
(51,'Can delete products',13,'delete_products'),
(52,'Can view products',13,'view_products'),
(53,'Can add feedback',14,'add_feedback'),
(54,'Can change feedback',14,'change_feedback'),
(55,'Can delete feedback',14,'delete_feedback'),
(56,'Can view feedback',14,'view_feedback'),
(57,'Can add complaint',15,'add_complaint'),
(58,'Can change complaint',15,'change_complaint'),
(59,'Can delete complaint',15,'delete_complaint'),
(60,'Can view complaint',15,'view_complaint');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'shop','customer'),
(8,'shop','login'),
(9,'shop','master'),
(10,'shop','order'),
(11,'shop','shop'),
(12,'shop','reviews'),
(13,'shop','products'),
(14,'shop','feedback'),
(15,'shop','complaint');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2022-10-11 06:22:13.246768'),
(2,'auth','0001_initial','2022-10-11 06:22:13.639082'),
(3,'admin','0001_initial','2022-10-11 06:22:13.754484'),
(4,'admin','0002_logentry_remove_auto_add','2022-10-11 06:22:13.754484'),
(5,'admin','0003_logentry_add_action_flag_choices','2022-10-11 06:22:13.766129'),
(6,'contenttypes','0002_remove_content_type_name','2022-10-11 06:22:13.828041'),
(7,'auth','0002_alter_permission_name_max_length','2022-10-11 06:22:13.882571'),
(8,'auth','0003_alter_user_email_max_length','2022-10-11 06:22:13.906621'),
(9,'auth','0004_alter_user_username_opts','2022-10-11 06:22:13.906621'),
(10,'auth','0005_alter_user_last_login_null','2022-10-11 06:22:13.938319'),
(11,'auth','0006_require_contenttypes_0002','2022-10-11 06:22:13.938319'),
(12,'auth','0007_alter_validators_add_error_messages','2022-10-11 06:22:13.954058'),
(13,'auth','0008_alter_user_username_max_length','2022-10-11 06:22:13.985206'),
(14,'auth','0009_alter_user_last_name_max_length','2022-10-11 06:22:14.016652'),
(15,'auth','0010_alter_group_name_max_length','2022-10-11 06:22:14.051260'),
(16,'auth','0011_update_proxy_permissions','2022-10-11 06:22:14.051260'),
(17,'auth','0012_alter_user_first_name_max_length','2022-10-11 06:22:14.083235'),
(18,'sessions','0001_initial','2022-10-11 06:22:14.112837'),
(19,'shop','0001_initial','2022-10-11 06:22:14.631922');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('djio059r3kb6mywotpzx9sqtc5t4bd01','eyJsaWQiOjJ9:1ojekD:o1_nsMPdhu7J-pRLn8hS7RE4xWpZOjbLCPiQUtq8oPI','2022-10-29 10:50:17.731251'),
('2z0j9l498pjt6i8wkacvncamnul7r8hk','eyJsaWQiOjJ9:1ok4DO:_TS_W5Gz8K7xcbpOIl3NYelytsSOjYN33yMBd2Qrb50','2022-10-30 14:02:06.995519'),
('kkcmdf4ztlrswtdexz2lzx46vwiu9mwf','eyJsaWQiOjR9:1ol1wJ:FGI6-asrSTNxCs3iGC5zxysLH34obiAI_A323GnxeVY','2022-11-02 05:48:27.420267'),
('9yisb3mm6mwiq0s1ajwvrm02azkn56fj','NzAyNGExYjZlYzRjNWNhMGMxZWRmZTUzMjdlMWE4MGRkMmJiMzQ0Yzp7ImxpZCI6NCwiYSI6ImFjdGl2ZSJ9','2022-11-11 05:05:48.475448'),
('utox4cdp52bk9l3dbv8w8cks3dpgy3bq','eyJsaWQiOjN9:1oq61W:yBqBpndS_SigMchLQtAkEqtxLYFzzd7wPbd-cioJpmA','2022-11-16 05:10:46.234763'),
('nigpy3bm5lgyiu02hflrjrofo8ygx0ey','eyJsaWQiOjN9:1oxLIC:3VXsHlQ-xjcbRZmf0H0dGZknOS_iPL0dOJ7UWmZHayc','2022-12-06 04:53:56.704624'),
('mmioixuy5yzx95u08baeuaiednu4gvqo','eyJsaWQiOjN9:1p1X0W:KcBcKxPVpQ4ZSmks_uWVBnn60N2lC2iEgQMO3xX9iEU','2022-12-17 18:13:00.750314'),
('3o23qejcowbde1fqs4xreq7uyslrsyb6','eyJsaWQiOjN9:1p2cZW:LGTW0u5aVtDR3msYqJKWJBpFPKcp53IlyfCgTz1FbXY','2022-12-20 18:21:38.452679');

/*Table structure for table `shop_complaint` */

DROP TABLE IF EXISTS `shop_complaint`;

CREATE TABLE `shop_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(500) NOT NULL,
  `reply_date` date NOT NULL,
  `cust_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_complaint_cust_id_id_5c1ec0a7` (`cust_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `shop_complaint` */

insert  into `shop_complaint`(`id`,`complaint`,`date`,`reply`,`reply_date`,`cust_id_id`) values 
(1,'Please Help Me','2022-11-28','pending','2022-11-28',5);

/*Table structure for table `shop_customer` */

DROP TABLE IF EXISTS `shop_customer`;

CREATE TABLE `shop_customer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `place` varchar(200) NOT NULL,
  `post` varchar(200) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_number` bigint(20) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `login_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_customer_login_id_id_7ac9bf11` (`login_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `shop_customer` */

insert  into `shop_customer`(`id`,`name`,`place`,`post`,`pin`,`photo`,`email`,`phone_number`,`dob`,`gender`,`password`,`login_id_id`) values 
(1,'Ruzain Abdurahman','Kannapuram','Cherukunnu',670301,'/static/pic/customer/221128-105335.jpg','ruzainruzi90@gmail.com',7012768795,'2022-11-23','Male','r',3),
(2,'Razeen Abdurahman','Kannapuram','Cherukunnu',670301,'/static/customer/img/221105-192911.jpg','razeen@gmail.com',9207399717,'2001-04-22','Male','Razeen90*',5),
(3,'Raniya Abdurahman','Kannapuram','Cherukunnu',670301,'/static/customer/img/221117-231521.jpg','raniya@gmail.com',7012768795,'2022-11-08','Female','raniya',11),
(4,'rt','tt','fgg',5558,'/static/customer/img/221121-104653.jpg','g@gmail.com',88598656,'2022-11-24','Male','gg',12),
(5,'Abhinav KL','Chuzhali','Chuzhali',670142,'/static/pic/customer/221128-002536.jpg','abhinav@gmail.com',7510186249,'2001-11-14','Male','ab',13);

/*Table structure for table `shop_feedback` */

DROP TABLE IF EXISTS `shop_feedback`;

CREATE TABLE `shop_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `cust_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_feedback_cust_id_id_b18be621` (`cust_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `shop_feedback` */

insert  into `shop_feedback`(`id`,`feedback`,`date`,`cust_id_id`) values 
(1,'Please Improve The UI','2022-11-28',5);

/*Table structure for table `shop_login` */

DROP TABLE IF EXISTS `shop_login`;

CREATE TABLE `shop_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `u_type` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `shop_login` */

insert  into `shop_login`(`id`,`username`,`password`,`u_type`) values 
(1,'admin@emart.com','admin','admin'),
(2,'razeenrazi5@gmail.com','Razeen5*','shop'),
(3,'ruzainruzi90@gmail.com','r','customer'),
(4,'mybazaar@gmail.com','Mybazaar1*','shop'),
(5,'razeen@gmail.com','Razeen90*','customer'),
(6,'info@greenshypermarket.com','Greens1*','pending'),
(11,'raniya@gmail.com','raniya','customer'),
(12,'g@gmail.com','gg','customer'),
(13,'abhinav@gmail.com','ab','customer');

/*Table structure for table `shop_master` */

DROP TABLE IF EXISTS `shop_master`;

CREATE TABLE `shop_master` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `cust_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_master_cust_id_id_96873500` (`cust_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `shop_master` */

insert  into `shop_master`(`id`,`status`,`date`,`cust_id_id`) values 
(1,'Booked','2022-11-28',5),
(2,'Add to Cart','2022-11-28',1);

/*Table structure for table `shop_order` */

DROP TABLE IF EXISTS `shop_order`;

CREATE TABLE `shop_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `date` date NOT NULL,
  `master_id_id` bigint(20) NOT NULL,
  `product_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_order_master_id_id_8a92848a` (`master_id_id`),
  KEY `shop_order_product_id_id_ccedb244` (`product_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `shop_order` */

insert  into `shop_order`(`id`,`quantity`,`date`,`master_id_id`,`product_id_id`) values 
(1,1,'2022-11-28',1,7),
(5,1,'2022-11-28',2,10),
(3,2,'2022-11-28',1,10),
(6,4,'2022-11-28',2,11),
(7,1,'2022-11-28',2,7);

/*Table structure for table `shop_products` */

DROP TABLE IF EXISTS `shop_products`;

CREATE TABLE `shop_products` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `stock` bigint(20) NOT NULL,
  `shop_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_products_shop_id_id_e4061ba1` (`shop_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `shop_products` */

insert  into `shop_products`(`id`,`name`,`photo`,`price`,`stock`,`shop_id_id`) values 
(10,'Ballpoint Pen (Red, 12 piece)','/static/pic/products/221101-124323.jpg','99',123,4),
(11,'Bamboo Notebook (Brown)','/static/pic/products/221101-124346.jpg','65',128,4),
(12,'Nataraj Pencil - 621 Bold (10 Pieces)','/static/pic/products/221103-111540.jpg','40',1389,4),
(7,'Apple MacBook Pro 14 (M1 Pro, 14.2 inch, 16GB, 512GB, Space Grey)','/static/pic/products/221025-124840.jpg','179900',66,2),
(6,'Apple iPhone 14 Pro Max (Space Black, 1 TB)','/static/pic/products/221025-123825.jpg','189900',97,2),
(8,'Corsair Dark Core Rgb Se Wireless Mouse','/static/pic/products/221025-134035.jpg','9990',49,2),
(13,'Maped Color Peps Color Pencil Set - Pack of 48 (Multicolor)','/static/pic/products/221110-215129.jpg','580',356,4),
(15,'Portronics Bubble Wireless Keyboard 2.4 GHz & Bluetooth 5.0 (Black)','/static/pic/products/221103-112701.jpg','1449',311,2),
(16,'Apple 20W USB-C Power Adapter','/static/pic/products/221103-113112.jpg','1799',132,2),
(17,'2022 Apple iPad Air with Apple M1 Chip (10.9-inch, Wi-Fi, 64GB) - Blue','/static/pic/products/221103-113419.jpg','54799',211,2);

/*Table structure for table `shop_reviews` */

DROP TABLE IF EXISTS `shop_reviews`;

CREATE TABLE `shop_reviews` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `review` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `cust_id_id` bigint(20) NOT NULL,
  `order_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_reviews_cust_id_id_a2dcfa56` (`cust_id_id`),
  KEY `shop_reviews_order_id_id_507353a1` (`order_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `shop_reviews` */

insert  into `shop_reviews`(`id`,`review`,`date`,`cust_id_id`,`order_id_id`) values 
(1,'Great Product','2022-11-28',5,1),
(2,'Loved it','2022-11-28',5,3);

/*Table structure for table `shop_shop` */

DROP TABLE IF EXISTS `shop_shop`;

CREATE TABLE `shop_shop` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `place` varchar(200) NOT NULL,
  `post` varchar(200) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_number` bigint(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  `shop_id_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_shop_shop_id_id_2ae912c0` (`shop_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `shop_shop` */

insert  into `shop_shop`(`id`,`name`,`place`,`post`,`pin`,`photo`,`email`,`phone_number`,`password`,`shop_id_id`) values 
(1,'Al Razeen','Kannapuram','Cherukunnu',670301,'/static/pic/221101-115934.jpg','razeenrazi5@gmail.com',9207399717,'Razeen5*',2),
(2,'My Bazaar','Kannapuram','Cherukunnu',670301,'/static/pic/221101-124155.jpg','mybazaar@gmail.com',9400542009,'Mybazaar1*',4),
(3,'Greens Hypermarket','Kannur','Talap',670002,'/static/pic/221106-210705.jpg','info@greenshypermarket.com',8606900755,'Greens1*',6);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
