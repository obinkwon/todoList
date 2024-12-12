-- todolist_db.todos definition
-- DROP TABLE todos;

CREATE TABLE `todos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(100) DEFAULT NULL,
  `strt_date` varchar(10) DEFAULT NULL,
  `end_date` varchar(10) DEFAULT NULL,
  `upt_date` varchar(10) DEFAULT NULL,
  `status` char(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;