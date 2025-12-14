import streamlit as st
import pandas as pd
import plotly.express as px

#set page configuration
st.set_page_config(
    page_title="African Articles Engagement on Wikipedia",
    layout="wide",
    initial_sidebar_state="expanded"
)

#Indroduction of my research
st.title("Wikipedia Users Engagement with African-Related Articles on the \
         English Wikipedia")
st.write("By Hadassah Mwazemba")

st.subheader("Research Question")
st.write("""
         For the following analysis, I am interested in a variety of ways
         users on the English Wikipedia engage with articles about Africa on the
         website.
         
         With the data that I collected from wikidata and the Wikipedia 2023-2024 DPDP set, \
         I decided to look at engagement with African-Related articles through the following \
         lenses:
            1. Which Countries are the most interested in these articles?
            2. What is the nature of the most viewed articles that fit into this criteria?
         
         As such my overall Research Question is:
         
          **What is the engagement of African-Related Wikipedia articles \
         in the English Wikipedia?**
          """ )

st.divider()

st.subheader("Initial Expectations")
st.write("""
         My with this research question and its subsequent analysis is to how high \
         or low the engagement with African-Related articles is on the English Wikipedia. 
         
         I expect to find the following:
            1. The engagement is low with these articles.
            2. Continents with Majority Speaking English countries such as the Americas and Europe have the highest Engagement
            3. Articles about humans have the most Engangement in terms of views.
          """ )


st.divider()

st.subheader("Hypothesis")
st.write("My Hpothesis for this Research topic is that **American and European \
         countries have the highest engagement with these articles in terms\
         of pageviews**")
