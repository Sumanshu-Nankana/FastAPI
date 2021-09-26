## This repository contains the FAST-API Learning Documentation, Code
## 

## YouTube Videos for explanation of all available code
[You Tube - FastAPI Videos](https://www.youtube.com/playlist?list=PLaNsxqNgctlM0CEzKBidDbYVmNsoBK8Ss "You Tube - Fast API")

## Credits to Sourabh Sinha for Udemy course 
Course Name: FastAPI Full Stack Web Development (API + Webapp)

## How to change the Default password for 'postgres'
-  su root
-  su postgres
-  psql
-  ALTER USER postgres PASSWORD 'postgres';
-  \q

## Some postgres commands
- \l (To list all databases)

## How to check and restart postgresql service in Ubuntu
-  ```sudo systemctl status postgresql```    (to check status of postgresql service)
-  ```sudo service postgresql restart```     (to restart the postgresql service)


## Commands/Steps for the SQLAlchemy alembic
- ```alembic init migrations```   ('migrations' is the folder name which I want, we can gave any name)

- Update the alembic.ini file with the database url in the key : sqlalchemy.url

 > a) if we want to write migrations scripts manually - then directly issue : ```alembic revision -m "Initial"```
	
 > b) if we want to generate migrations scripts automatically - then perform below steps

	 >> b.1) Update the env.py file (in migrations folder) with target_metdata

     >> b.2) Issue : ```alembic revision --autogenerate -m "Initial"```

- Last step is to apply the migrations scripts by command : ```alembic upgrade head```
  (head is basically pointing to the current version)


## If we are using alembic
- Then comment the Base.metdata.create_all(bind=engine) line in main.py
  Because, now tables will get created using alembic


## Steps to set connectivity between Docker Container (Web-app) with Postgres Database (On Localhost)

>Step1: Update postgresql configuration file, to allow all remote connection access

```sudo nano /etc/postgresql/12/main/postgresql.conf```

Find the line "listen_address" and uncomment it , also change from localhost to '*', So after change it should look like this
listen_address = '*'

>Step2: Update postgres hba configuration file, to allow docker container connection to host database

```sudo nano /etc/postgresql/12/main/pg_hba.conf```

#### host db_name user_name docker_ip/16  trust
```host testing postgres 172.17.0.0/16 trust```

>Step3: Restart the postgres service

```sudo /etc/init.d/postgresql restart```

>Step4: Build the docker image

```docker build --network=host -t myappimage . ```

>Step5: Run the container

```docker run -d --network=host -e "DB_DBNAME=testing" -e "DB_PORT=5432" -e "DB_USER=postgres" -e "DB_PASS=postgres" -e "DB_HOST=127.0.0.1" --name myappcontainer myappimage```

## Deploy using docker-compose

> Check the version of docker-compose : ```docker-compose -v```

> Step1 : Create the docker-compose.yml file

> Step2 : To Build and Start the Container, issue 

```docker-compose up -d```

> Step3 : To Stop all the container/services, issue

```docker-compose down```
