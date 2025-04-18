-- login mysql as root
-- mysql -uroot -p

-- authentication
CREATE USER 'mysql_exporter'@'%' IDENTIFIED BY '123456' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'mysql_exporter'@'%';
FLUSH PRIVILEGES;

-- SHOW GRANTS FOR 'mysql_exporter'@'%';
