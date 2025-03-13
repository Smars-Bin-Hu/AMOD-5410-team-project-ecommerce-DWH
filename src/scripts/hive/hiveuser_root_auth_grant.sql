-- # beeline login hive as root
beeline -u jdbc:hive2://localhost:10000 -n root

-- ADMIN ROLE and DATABASE PRIVILEGE GRANT
SET ROLE ADMIN;
-- GRANT ALL ON DATABASE ods TO ROLE ADMIN; -- auth to ods layer
-- GRANT ROLE ADMIN TO USER root; -- Error Granting: root already has the role admin

SHOW CURRENT ROLES;
SHOW GRANT ROLE ADMIN;