import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ce88ddb003629ce18e3e8a5c6d9051c6&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original'+ data['poster_path']

def recommend(movie_name):
    movie_index = movie[movie['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie =[]
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movie.iloc[i[0]].movie_id
        recommended_movie.append(movie.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append((fetch_poster(movie_id)))
    return recommended_movie,recommended_movies_poster

movie_dic = pickle.load(open('movie_dic.pkl','rb'))
movie = pd.DataFrame(movie_dic)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movie['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

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