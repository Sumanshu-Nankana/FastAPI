## This repository contains the FAST-API Learning Documentation, Code
## 

## How to change the Default password for 'postgres'
-  su root
-  su postgres
-  psql
-  ALTER USER postgres PASSWORD 'postgres';
-  \q

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

