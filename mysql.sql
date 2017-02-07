-- https://www.if-not-true-then-false.com/2010/install-mysql-on-fedora-centos-red-hat-rhel/

CREATE DATABASE lostBaggage;
create user 'webdb_user'@'localhost' identified by 'sa123';
GRANT ALL ON lostBaggage.* TO 'webdb_user'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'webdb_user'@'localhost';
flush privileges;


drop table `lostBaggage`.`tbl_formulario`;

CREATE TABLE `lostBaggage`.`tbl_formulario` (
  `report_id` BIGINT NOT NULL AUTO_INCREMENT,
  `passenger_name` VARCHAR(45) NOT NULL,
  `passenger_address` VARCHAR(45) NOT NULL,
  `passenger_telephone` VARCHAR(45) NOT NULL,
  `passenger_email` VARCHAR(45) NOT NULL,
  `book_id` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`report_id`));

drop procedure if exists sp_reportLostBg;
DELIMITER $$
CREATE DEFINER=`webdb_user`@`localhost` PROCEDURE `sp_reportLostBg`(
    IN p_name VARCHAR(45),
    IN p_address VARCHAR(45),
    IN p_telephone VARCHAR(45),
    IN p_email VARCHAR(45),
    IN p_bookid VARCHAR(10)
)
BEGIN
    insert into tbl_formulario
        (
            passenger_name,
            passenger_address,
	    passenger_telephone,
	    passenger_email,
            book_id
        )
        values
        (
            p_name,
            p_address,
            p_telephone,
            p_email,
	    p_bookid
        );

END$$
DELIMITER ;
