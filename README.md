# scrapy

This's a simple use for web-crawler in python with scrapy. You can use this data for analysis about the best players in the season according to your season stats or whatever you want do. 😄

Data collected in [basketball-reference](https://www.basketball-reference.com/leagues/NBA_2020_per_game.html) 👍

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

in your terminal put this line:

```
scrapy runspider nba-api-test.py -o ./output-tests/output.json 
```

This is the start for our scrapy, that line is responsible for taking the data and the parameter **-o** give us an output about this data.
