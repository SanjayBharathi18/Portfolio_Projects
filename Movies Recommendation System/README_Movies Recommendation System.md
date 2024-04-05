![MovieRecommend](https://github.com/SanjayBharathi18/Portfolio_Projects/assets/165292172/dd4121d7-06c3-4392-af5b-4fc75b0a04ca)

# MOVIES RECOMMENDATION SYSTEM

The dataset that we are using here is the TMDB 5000 Movie Dataset.This dataset consists of movies released on or before July 2017. Under this dataset, there are 2 files:

1. tmdb_5000_movies.csv: It includes 20 columns like budget, genres, id, keywords, title, tagline, etc.
2. tmdb_5000_credtis.csv: It includes 4 columns- movie_id, title, cast, and crew.

## TYPES OF RECOMMENDER SYSTEMS
There are three types of recommender systems:

- Demographic filtering: They make basic recommendations to each user based on movie popularity and/or genre. The System recommends the same films to users that share comparable demographic characteristics. Because each user is unique, this technique is seen overly simplistic. The underlying principle behind this system is that more successful and highly acclaimed films have a higher chance of being appreciated by the general public.

- Content-based filtering: They recommend related things based on a specific item. This system makes movie recommendations based on item metadata such as genre, director, description, actors, and so on. The main assumption underlying these recommender systems is that if a person likes one item, he or she will enjoy another item that is similar.

- Collaborative filtering: This algorithm matches people with similar interests and makes suggestions based on those matches. Unlike their content-based cousins, collaborative filters do not require item metadata.

In this project, we have used Content-based filtering to recommend the Top 5 similar movies based on the movie name given.

## StreamLit
Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

We have deployed the Movie recommendation system in streamlit and displayed the poster of the movies which was extracted from TMDB Database through API key. 


## How to run ?

- Copy/Download the codes from [MoviesRecommendationSystem.ipynb](https://github.com/SanjayBharathi18/Portfolio_Projects/blob/9f35192d598798ccbb1790841013de4918fdc284/Movies%20Recommendation%20System/MoviesRecommendationSystem.ipynb) and [MovieRecommendApp.py](https://github.com/SanjayBharathi18/Portfolio_Projects/blob/9f35192d598798ccbb1790841013de4918fdc284/Movies%20Recommendation%20System/MovieRecommendApp.py)
-  Go to the command prompt.
- Change to the directory where code files were placed.
- Type the below command and click enter.
- It will be directed to streamlit website where our project is deployed. 


```bash
  streamlit run file_name.py 
```

