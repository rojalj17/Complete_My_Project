/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - completemp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`completemp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `completemp`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add batch',7,'add_batch'),(26,'Can change batch',7,'change_batch'),(27,'Can delete batch',7,'delete_batch'),(28,'Can view batch',7,'view_batch'),(29,'Can add external_ guide',8,'add_external_guide'),(30,'Can change external_ guide',8,'change_external_guide'),(31,'Can delete external_ guide',8,'delete_external_guide'),(32,'Can view external_ guide',8,'view_external_guide'),(33,'Can add group',9,'add_group'),(34,'Can change group',9,'change_group'),(35,'Can delete group',9,'delete_group'),(36,'Can view group',9,'view_group'),(37,'Can add login',10,'add_login'),(38,'Can change login',10,'change_login'),(39,'Can delete login',10,'delete_login'),(40,'Can view login',10,'view_login'),(41,'Can add student',11,'add_student'),(42,'Can change student',11,'change_student'),(43,'Can delete student',11,'delete_student'),(44,'Can view student',11,'view_student'),(45,'Can add project_schedule',12,'add_project_schedule'),(46,'Can change project_schedule',12,'change_project_schedule'),(47,'Can delete project_schedule',12,'delete_project_schedule'),(48,'Can view project_schedule',12,'view_project_schedule'),(49,'Can add progress',13,'add_progress'),(50,'Can change progress',13,'change_progress'),(51,'Can delete progress',13,'delete_progress'),(52,'Can view progress',13,'view_progress'),(53,'Can add internal_ guide',14,'add_internal_guide'),(54,'Can change internal_ guide',14,'change_internal_guide'),(55,'Can delete internal_ guide',14,'delete_internal_guide'),(56,'Can view internal_ guide',14,'view_internal_guide'),(57,'Can add group_member',15,'add_group_member'),(58,'Can change group_member',15,'change_group_member'),(59,'Can delete group_member',15,'delete_group_member'),(60,'Can view group_member',15,'view_group_member'),(61,'Can add chat',16,'add_chat'),(62,'Can change chat',16,'change_chat'),(63,'Can delete chat',16,'delete_chat'),(64,'Can view chat',16,'view_chat'),(65,'Can add attendance',17,'add_attendance'),(66,'Can change attendance',17,'change_attendance'),(67,'Can delete attendance',17,'delete_attendance'),(68,'Can view attendance',17,'view_attendance');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `completemp_attendance` */

DROP TABLE IF EXISTS `completemp_attendance`;

CREATE TABLE `completemp_attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `date_upload` varchar(100) NOT NULL,
  `GRP_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_attendance_GRP_id_df06b43a_fk_completemp_group_id` (`GRP_id`),
  CONSTRAINT `completemp_attendance_GRP_id_df06b43a_fk_completemp_group_id` FOREIGN KEY (`GRP_id`) REFERENCES `completemp_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_attendance` */

insert  into `completemp_attendance`(`id`,`file`,`date_upload`,`GRP_id`) values (1,'/static/Attendance_files/20240117-115918.pdf','2024-59-17',1);

/*Table structure for table `completemp_batch` */

DROP TABLE IF EXISTS `completemp_batch`;

CREATE TABLE `completemp_batch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `batch` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_batch` */

insert  into `completemp_batch`(`id`,`batch`) values (1,'Batch_2021'),(2,'Batch_2022'),(3,'Batch_2023'),(5,'batch_2024');

/*Table structure for table `completemp_chat` */

DROP TABLE IF EXISTS `completemp_chat`;

CREATE TABLE `completemp_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `send_type` varchar(100) NOT NULL,
  `EXTERNAL_id` int(11) NOT NULL,
  `INTERNAL_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_chat_EXTERNAL_id_3f45363a_fk_completem` (`EXTERNAL_id`),
  KEY `completemp_chat_INTERNAL_id_87f3c5b0_fk_completem` (`INTERNAL_id`),
  CONSTRAINT `completemp_chat_EXTERNAL_id_3f45363a_fk_completem` FOREIGN KEY (`EXTERNAL_id`) REFERENCES `completemp_external_guide` (`id`),
  CONSTRAINT `completemp_chat_INTERNAL_id_87f3c5b0_fk_completem` FOREIGN KEY (`INTERNAL_id`) REFERENCES `completemp_internal_guide` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_chat` */

insert  into `completemp_chat`(`id`,`message`,`date`,`send_type`,`EXTERNAL_id`,`INTERNAL_id`) values (1,'hy','2023-23-12','external',1,1),(2,'aa','2023-12-23','external',1,1),(3,'helo','2023-10-12','internal',1,1),(4,'yes','2023-12-23','external',1,1),(5,'YES','2023-12-23','internal',1,1),(6,'heloo how r u','2024-01-17','internal',1,1);

/*Table structure for table `completemp_external_guide` */

DROP TABLE IF EXISTS `completemp_external_guide`;

CREATE TABLE `completemp_external_guide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eg_name` varchar(200) NOT NULL,
  `eg_posts` varchar(200) NOT NULL,
  `eg_company_name` varchar(50) NOT NULL,
  `eg_place` varchar(50) NOT NULL,
  `eg_post_office` varchar(50) NOT NULL,
  `eg_pin` varchar(50) NOT NULL,
  `eg_email` varchar(50) NOT NULL,
  `eg_phone` bigint(20) NOT NULL,
  `EG_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_external_guide_EG_id_aeeeeda9_fk_completemp_login_id` (`EG_id`),
  CONSTRAINT `completemp_external_guide_EG_id_aeeeeda9_fk_completemp_login_id` FOREIGN KEY (`EG_id`) REFERENCES `completemp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_external_guide` */

insert  into `completemp_external_guide`(`id`,`eg_name`,`eg_posts`,`eg_company_name`,`eg_place`,`eg_post_office`,`eg_pin`,`eg_email`,`eg_phone`,`EG_id`) values (1,'Rahul','Assistant','Riss Technologies','Kannur','Kannur','642036','rahul@gmail.com',9754628456,3),(2,'Shalu','senior assistant','integos','caltex','kannur','675495','shalu@gmail.com',9756124863,7),(3,'Krishna','software Engineer','Riss Technologies','Kannur','Kannur','642036','krishna@gmail.com',7845968512,8),(4,'Niveditha','assisstant','Riss Technologies','Kannur','Kannur','642036','niveditharajeevan@gmail.com',9207795066,10),(5,'Niveditha','assisstant','Riss Technologies','Kannur','Kannur','642036','nivedithaarajeevan@gmail.com',9207795066,11),(6,'Niveditha','assisstant','Riss Technologies','Kannur','Kannur','642036','nivedithaarajeevan@gmail.com',9207795066,12),(7,'Shalu','assisstant','Riss Technologies','Kannur','kannur','642036','sg@gmail.com',8956321451,15),(8,'s','sd','s','sdsd','sd','642036','g@gmail.com',8956321451,17),(9,'sssssssssss','assisstant','sss','Kannur','ss','642036','sss@gmail.com',9754628456,23),(10,'wwww','ilug,jb','fyku','p;;oliuyt','iytr','642036','lkjh@gmail.com',9756124863,24);

/*Table structure for table `completemp_group` */

DROP TABLE IF EXISTS `completemp_group`;

CREATE TABLE `completemp_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grp_number` varchar(200) NOT NULL,
  `grp_email` varchar(50) NOT NULL,
  `grp_topic_name` varchar(100) NOT NULL,
  `GRP_BATCHID_id` int(11) NOT NULL,
  `GRP_EG_id` int(11) NOT NULL,
  `GRP_IG_id` int(11) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  `grp_leader` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_group_GRP_BATCHID_id_43c6cb3d_fk_completemp_batch_id` (`GRP_BATCHID_id`),
  KEY `completemp_group_GRP_EG_id_baf2f6b8_fk_completem` (`GRP_EG_id`),
  KEY `completemp_group_GRP_IG_id_add04e99_fk_completem` (`GRP_IG_id`),
  KEY `completemp_group_LOGIN_id_a2350d5f_fk_completemp_login_id` (`LOGIN_id`),
  CONSTRAINT `completemp_group_GRP_BATCHID_id_43c6cb3d_fk_completemp_batch_id` FOREIGN KEY (`GRP_BATCHID_id`) REFERENCES `completemp_batch` (`id`),
  CONSTRAINT `completemp_group_GRP_EG_id_baf2f6b8_fk_completem` FOREIGN KEY (`GRP_EG_id`) REFERENCES `completemp_external_guide` (`id`),
  CONSTRAINT `completemp_group_GRP_IG_id_add04e99_fk_completem` FOREIGN KEY (`GRP_IG_id`) REFERENCES `completemp_internal_guide` (`id`),
  CONSTRAINT `completemp_group_LOGIN_id_a2350d5f_fk_completemp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `completemp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_group` */

insert  into `completemp_group`(`id`,`grp_number`,`grp_email`,`grp_topic_name`,`GRP_BATCHID_id`,`GRP_EG_id`,`GRP_IG_id`,`LOGIN_id`,`grp_leader`) values (1,'1','rojaljyo@gmail.com','Complete My Project',1,1,1,4,'No name'),(2,'2','kp@gmail.com','Turf management',2,2,2,9,'No name'),(6,'2','rojal@gmail.com','Complete My Project',1,2,2,28,'Rojal');

/*Table structure for table `completemp_group_member` */

DROP TABLE IF EXISTS `completemp_group_member`;

CREATE TABLE `completemp_group_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `GRP_ID_id` int(11) NOT NULL,
  `LEADER_STUD_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_group_mem_GRP_ID_id_3bcebd75_fk_completem` (`GRP_ID_id`),
  KEY `completemp_group_mem_LEADER_STUD_ID_id_417ce3b9_fk_completem` (`LEADER_STUD_ID_id`),
  CONSTRAINT `completemp_group_mem_GRP_ID_id_3bcebd75_fk_completem` FOREIGN KEY (`GRP_ID_id`) REFERENCES `completemp_group` (`id`),
  CONSTRAINT `completemp_group_mem_LEADER_STUD_ID_id_417ce3b9_fk_completem` FOREIGN KEY (`LEADER_STUD_ID_id`) REFERENCES `completemp_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `completemp_group_member` */

/*Table structure for table `completemp_internal_guide` */

DROP TABLE IF EXISTS `completemp_internal_guide`;

CREATE TABLE `completemp_internal_guide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ig_name` varchar(200) NOT NULL,
  `ig_email` varchar(200) NOT NULL,
  `ig_phone` bigint(20) NOT NULL,
  `IG_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_internal_guide_IG_id_b73c2180_fk_completemp_login_id` (`IG_id`),
  CONSTRAINT `completemp_internal_guide_IG_id_b73c2180_fk_completemp_login_id` FOREIGN KEY (`IG_id`) REFERENCES `completemp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_internal_guide` */

insert  into `completemp_internal_guide`(`id`,`ig_name`,`ig_email`,`ig_phone`,`IG_id`) values (1,'Anitha Haridas','anithaharidas@gmail.com',9571243654,2),(2,'Raji k','raji@gmail.com',9754682165,5),(3,'Jasna B','jasna@gmail.com',8574961245,6);

/*Table structure for table `completemp_login` */

DROP TABLE IF EXISTS `completemp_login`;

CREATE TABLE `completemp_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_login` */

insert  into `completemp_login`(`id`,`username`,`password`,`usertype`) values (1,'admin@gmail.com','admin','admin'),(2,'anithaharidas@gmail.com','7210','Internal Guide'),(3,'rahul@gmail.com','4103','External_Guide'),(4,'rojaljyo@gmail.com','718','Group'),(5,'raji@gmail.com','2254','Internal Guide'),(6,'jasna@gmail.com','8551','Internal Guide'),(7,'shalu@gmail.com','1404','External_Guide'),(8,'krishna@gmail.com','2830','External_Guide'),(9,'kp@gmail.com','5784','Group'),(10,'niveditharajeevan@gmail.com','800','External_Guide'),(11,'n','4687','External_Guide'),(12,'nivedithaarajeevan@gmail.com','6397','External_Guide'),(15,'sg@gmail.com','4246','External_Guide'),(16,'rj@gmail.com','6210','Group'),(17,'g@gmail.com','2219','External_Guide'),(23,'sss@gmail.com','1952','External_Guide'),(24,'lkjh@gmail.com','9517','External_Guide'),(26,'KK@gmail.com','8368','Group'),(27,'r@gmail.com','1829','Group'),(28,'rojal@gmail.com','9252','Group');

/*Table structure for table `completemp_progress` */

DROP TABLE IF EXISTS `completemp_progress`;

CREATE TABLE `completemp_progress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `progress_file` varchar(100) NOT NULL,
  `date_upload` date NOT NULL,
  `remark` varchar(500) NOT NULL,
  `GRP_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_progress_GRP_id_0482797b_fk_completemp_group_id` (`GRP_id`),
  CONSTRAINT `completemp_progress_GRP_id_0482797b_fk_completemp_group_id` FOREIGN KEY (`GRP_id`) REFERENCES `completemp_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_progress` */

insert  into `completemp_progress`(`id`,`progress_file`,`date_upload`,`remark`,`GRP_id`) values (1,'/static/progress_files/20240117-120140.pdf','2024-01-17','80%complete',1);

/*Table structure for table `completemp_project_schedule` */

DROP TABLE IF EXISTS `completemp_project_schedule`;

CREATE TABLE `completemp_project_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `note` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(15) NOT NULL,
  `BATCH_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_project_s_BATCH_id_056dd0bb_fk_completem` (`BATCH_id`),
  CONSTRAINT `completemp_project_s_BATCH_id_056dd0bb_fk_completem` FOREIGN KEY (`BATCH_id`) REFERENCES `completemp_batch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_project_schedule` */

insert  into `completemp_project_schedule`(`id`,`note`,`date`,`time`,`BATCH_id`) values (1,'Submit Report of the project after vacation','2023-12-23','10:00',1),(2,'submit er on TUESDAY','17-01-24','12:45',5),(7,'GGG','17-01-24','12:43',2);

/*Table structure for table `completemp_student` */

DROP TABLE IF EXISTS `completemp_student`;

CREATE TABLE `completemp_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `std_name` varchar(200) NOT NULL,
  `std_regno` varchar(200) NOT NULL,
  `std_email` varchar(50) NOT NULL,
  `std_phone` bigint(20) NOT NULL,
  `type_mem_lead` varchar(200) NOT NULL,
  `std_group_id_id` int(11) NOT NULL,
  `std_batch_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `completemp_student_std_group_id_id_899401b8_fk_completem` (`std_group_id_id`),
  KEY `completemp_student_std_batch_id_id_3d530548_fk_completem` (`std_batch_id_id`),
  CONSTRAINT `completemp_student_std_batch_id_id_3d530548_fk_completem` FOREIGN KEY (`std_batch_id_id`) REFERENCES `completemp_batch` (`id`),
  CONSTRAINT `completemp_student_std_group_id_id_899401b8_fk_completem` FOREIGN KEY (`std_group_id_id`) REFERENCES `completemp_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `completemp_student` */

insert  into `completemp_student`(`id`,`std_name`,`std_regno`,`std_email`,`std_phone`,`type_mem_lead`,`std_group_id_id`,`std_batch_id_id`) values (1,'Sonali ck','cw18','sck@gmail.com',8754692316,'--select--',1,1),(2,'Niveditha vk','cw33','nvk@gmail.com',9207795066,'Member',1,1),(3,'Rojal Jyothish','cw17','rojaljyo@gmail.com',9563220044,'Leader',1,1),(4,'Nandana kp','cw31','nkp@gmail.com',7548692154,'Leader',2,1),(7,'geethu','2','geethu@gmail.com',9563220044,'1',6,1);

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
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(17,'completemp','attendance'),(7,'completemp','batch'),(16,'completemp','chat'),(8,'completemp','external_guide'),(9,'completemp','group'),(15,'completemp','group_member'),(14,'completemp','internal_guide'),(10,'completemp','login'),(13,'completemp','progress'),(12,'completemp','project_schedule'),(11,'completemp','student'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-12-23 03:47:12.070928'),(2,'auth','0001_initial','2023-12-23 03:47:12.196523'),(3,'admin','0001_initial','2023-12-23 03:47:12.557190'),(4,'admin','0002_logentry_remove_auto_add','2023-12-23 03:47:12.635323'),(5,'admin','0003_logentry_add_action_flag_choices','2023-12-23 03:47:12.635323'),(6,'contenttypes','0002_remove_content_type_name','2023-12-23 03:47:12.729078'),(7,'auth','0002_alter_permission_name_max_length','2023-12-23 03:47:12.760385'),(8,'auth','0003_alter_user_email_max_length','2023-12-23 03:47:12.807870'),(9,'auth','0004_alter_user_username_opts','2023-12-23 03:47:12.807870'),(10,'auth','0005_alter_user_last_login_null','2023-12-23 03:47:12.854977'),(11,'auth','0006_require_contenttypes_0002','2023-12-23 03:47:12.854977'),(12,'auth','0007_alter_validators_add_error_messages','2023-12-23 03:47:12.854977'),(13,'auth','0008_alter_user_username_max_length','2023-12-23 03:47:12.902115'),(14,'auth','0009_alter_user_last_name_max_length','2023-12-23 03:47:12.933596'),(15,'auth','0010_alter_group_name_max_length','2023-12-23 03:47:12.980839'),(16,'auth','0011_update_proxy_permissions','2023-12-23 03:47:12.996601'),(17,'completemp','0001_initial','2023-12-23 03:47:13.358761'),(18,'sessions','0001_initial','2023-12-23 03:47:13.847275'),(19,'completemp','0002_group_grp_leader','2024-01-17 09:40:51.639184'),(20,'completemp','0003_student_std_batch_id','2024-01-17 10:23:40.371855');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('8oxa6ovg2wru1bictaksbm0szgr3gdr3','MjcyMWZkOGMzZDdiMjU1MDU2NzE4YjRlZTIyZjBjYWM3MmIwMTEyNzp7ImxnIjoibGluIiwibGlkIjozfQ==','2024-01-06 06:04:28.805070'),('9ap9mn6f4n7bk7y8w3v6jsm685658wuo','OWY3NzAxN2FlOGZmZTM2M2RmMWNlOWEwYWM2OWVmMWI2NWNkYWE1Yjp7ImxnIjoibGluIn0=','2024-01-20 04:50:21.872847'),('c8apyrqdtjbsrsg5f6fxgp4jvg3cu060','NzRhOWM4MWQ4MTNjNzdlNzM0ODMxOGE5N2IxMDUyOTgyOWI5M2U0NTp7ImxnIjoibGluIiwibGlkIjozLCJoZWFkIjoiQ0hBVCIsInVpZCI6IjEifQ==','2024-01-31 06:36:01.337543');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
