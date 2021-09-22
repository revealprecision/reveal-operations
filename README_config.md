# INSTALL AND CONFIGURE REVEAL

## MariaDB

Start by launching the mariadb container

```bash
docker-compose up -d mariadb
```

Once it is running, connect to the DB and create the databases you will need.

```sql
DROP DATABASE IF EXISTS test;
CREATE DATABASE motechquartz;
CREATE USER 'opensrp_admin'@'%' identified by 'not_so_secret';
GRANT ALL PRIVILEGES ON motechquartz.* to 'opensrp_admin'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE keycloak;
CREATE USER 'keycloak'@'%' identified by 'not_so_secret';
GRANT ALL PRIVILEGES ON keycloak.* to 'keycloak'@'%';
FLUSH PRIVILEGES;
```

Create the tables for the Quartz used by OpenSRP located in `conf/mariadb/tables_quartz_mysql.sql`

---

## PostgreSQL

Next start the container and then create databases from OpenSRP, Superset and Reveal ETL

```bash
docker-compose up -d postgresql
```

Once it is running, connect to the DB and create the databases you will need.

```sql
CREATE ROLE opensrp_admin LOGIN PASSWORD 'not_so_secret';
ALTER USER opensrp_admin WITH SUPERUSER; -- for now this is needed to create the schema
CREATE DATABASE opensrp OWNER opensrp_admin;

CREATE ROLE superset LOGIN PASSWORD 'not_so_secret';
CREATE DATABASE superset OWNER superset;

CREATE ROLE reveal LOGIN PASSWORD 'not_so_secret';
ALTER USER reveal WITH SUPERUSER; -- for now this is needed to create the schema
CREATE DATABASE reveal OWNER reveal;
```

---

## Redis

Next start up the redis container

```bash
docker-compose up -d redis
```

---

## Keycloak

Next start up the redis container

```bash
docker-compose up -d keycloak
```

`TODO` CONFIGURE KEYCLOAK

---

## Superset

Start up Superset

```bash
docker-compose up -d superset
```

Once it is running, create the admin user

```bash
superset fab create-admin --username admin_user --firstname Admin --lastname User --email admin@yourdomain.com --password not_so_secret

superset db upgrade
superset init
```

---

## OpenSRP server

First in order to create the schema run the mybatis container

```bash
docker-compose up mybatis
```

After it has created the schema, you can start opensrp-server

```bash
docker-compose up -d opensrp-server
```

Double check this setting is present in the DB.

```sql
INSERT INTO core.identifier_source (id,identifier,description,identifier_validator_algorithm,base_character_set,first_identifier_base,prefix,suffix,min_length,max_length,regex_format,sequence_value) VALUES (1,2,'','LUHN_CHECK_DIGIT_ALGORITHM','0123456789','2000000','','',7,10,'',1);
```

---

## Reveal Web

Make sure you have configured all the settings in `conf/reveal-web/config.js`

In order to better understand the current working settings of Reveal Web and its interaction with Superset, please contact Stefanus Heath <sheath@akros.com>

```bash
docker-compose up -d reveal-web
```

---

## Nginx

Lastly get nginx running

```bash
docker-compose up -d nginx
```

---

## Reveal ETL

Now you can run the ETL

```bash
docker-compose up -d reveal-etl
```
