# scrapy

This's a simple use for web-crawler in python with scrapy. You can use this data for analysis about the best players in the season according to your season stats or whatever you want do. 😄

Data collected in [basketball-reference](https://www.basketball-reference.com/leagues/NBA_2020_per_game.html) 👍

###### Configs

Create a file named .env (this file is responsible for archive locally all connection string) with this config bellowCreate a file named .env (this file is responsible for archive locally all connection string) with this config bellow

```
POSTGRES_HOST = "HOST"
POSTGRES_PORT = "HOST_PORT_HERE"
POSTGRES_DB = BD_NAME
POSTGRES_USER = BD_USER
POSTGRES_PASSWORD = BD_PASSWORD
```

###### Install dependencies

You need pip installed in your environment, if you've installed pip previously, go ahead!

```
pip install -r requirements.txt
```

or if you want to install with pip3

```
pip3 install -r requirements.txt
```

###### Execution

**Create docker container (Postgresql)**
Open the terminal in the root folder project and put this command

```
sudo docker-compose up -d 
```

ps: Obviously, you need docker and docker-compose installed

**Testing the connection**
Ok, in terminal again go to folder connection

```
cd bd/connection/
```

Test if there is a connection to the database and if is everything ok

```
python3 ManagerConection.py
```

ps: If you have any problems with the connection, check that the docker container is **started**

And then, in your terminal put this line:

```
scrapy runspider nba-api-test.py -o ./output-tests/output.json 
```

This is the start for our scrapy, that line is responsible for taking the data and the parameter **-o** give us an output about this data.
