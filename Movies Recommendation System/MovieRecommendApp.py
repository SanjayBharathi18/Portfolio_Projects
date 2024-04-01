import  streamlit as st

import pickle
import pandas as pd
import requests

#st.title('MOVIE RECOMMENDATION APP')
st.markdown("<h1 style='text-align: center; color: red;'>Movie Recommendation App</h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='font-size: 5px ; style=text-align: center; color: red;'>(A Platform to recommend movies on your choice)</h1>", unsafe_allow_html=True)

def fetch_poster(movie_id):
    api_key = 'ddfb3770802d5597f8635d9540c5f625'
    base_url = 'https://api.themoviedb.org/3'

    movie_id = movie_id  
    endpoint = f'{base_url}/movie/{movie_id}/images'

    params = {'api_key': api_key}

    response = requests.get(endpoint, params=params)


    if response.status_code == 200:
        data = response.json()
        posters = data.get('posters', [])
        backdrops = data.get('backdrops', [])

        if posters:
            poster_file_path = posters[0]['file_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_file_path
            return full_path
        elif backdrops:
            backdrop_file_path = backdrops[0]['file_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + backdrop_file_path
            return full_path
        else:
            return 'No images found for this movie.'
    else:
        return 'Failed to retrieve data from TMDb API.'


    

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_posters

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox(
    "Select a movie from the dropdown",
    movies['title'].values)

if st.button('Show Similar Movies'):
    names,posters = recommend(selected_movie_name)

    #display with the columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
