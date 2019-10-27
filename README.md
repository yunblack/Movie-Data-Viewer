# Movie Data Viewer

I made a software program that shows a particular statistics requested by a user. The program is developed in Python language using PyCharm IDE. The data presented in this is taken from The Movies Dataset1 made available by Rounak Banik on Kaggle – which is an online community of data scientists. These files contain metadata for about 45,000 movies
released on or before July 2017. Some information about movies in production or planned is given as well. We will use a file named movies_metadata from this dataset that contains information on the following:

1) adult: TRUE/FALSE
2) genres: Zero or multiple genres. It can be considered as a list of dictionaries in Python. E.g. [{'id':
80, 'name': 'Crime'}, {'id': 35, 'name': 'Comedy'}]
3) id: ID of the movie in this dataset.
4) Imdb_id: ID of the movie as assigned by IMDB
5) Original_language: Original language of movie as given by two letter code (e.g. es for Spanish)
6) Original_title: Original title of the movie
7) Popularity: Some value showing popularity of the movie – higher is better
8) Production_companies: Dictionary list containing names of production companies. E.g. [{'name':
'Universal Pictures', 'id': 33}, {'name': 'Largo Entertainment', 'id': 1644}, {'name': 'JVC
Entertainment Networks', 'id': 4248}]
9) Production_countries: Dictionary list containing names of production countires. E.g.
[{'iso_3166_1': 'US', 'name': 'United States of America'}]
10) Release_date: Date of release in MM/DD/YYYY format
11) Revenue: Revenue obtained (in $?)
12) Runtime: length of movie in minutes
13) Spoken_language: Language spoken in the movie
14) Status: One of cancelled, In Production, Planned, Post Production, Released
15) Title: Movie title 
