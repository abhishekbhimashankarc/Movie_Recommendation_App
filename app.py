import streamlit as st
import google.generativeai as genai # type: ignore
import os
from dotenv import load_dotenv
load_dotenv() # active api key
genai.configure(api_key = os.getenv('GOOGLE_GEMINI_API'))

# Movie Recommender System
st.title("🍿🎥✮⋆˙ Movie Recommendation system 🍿🎥✮⋆˙ ")
user_input = st.text_input('Enter Movie Name')
submit = st.button('Click Here')

if submit:
    st.markdown('Movie name has been entered ✨')
else :
    st.warning('You need to enter the Movie name ⎚-⎚')

model = genai.GenerativeModel('gemini-2.5-flash-lite')

if submit and user_input.strip():
    st.markdown(f'Movie name entered: {user_input}')
    response = model.generate_content(f'Generate Movie Recommendations based on this movie: {user_input}')
    st.write(f'RECOMMENDATIONS FOR SIMILAR MOVIES :\n{response.text}')
else:
    st.write("No movie name entered yet.")