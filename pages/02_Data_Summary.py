import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Summary",
    layout="wide",
    initial_sidebar_state="expanded"
)



#Read the csv
PATH = "data/african_classified_dpdp.csv"
df = pd.read_csv(PATH)


st.title("Data Summary")

st.subheader("Overview of the data metrics used for analysis")

st.metric("Number of Countries:","92")
st.metric("Number of rows(articles per day)","53205")
st.metric("Wikipedia Project", "WikiProject Africa")
st.metric("Date Range","02-06-2023 - 12-31-2024")


st.divider()

st.subheader("Data Collection Process")

st.write("""
         The data used in the analysis was collected using the following process:

         Using **WikiProject Africa (a Wikipedia project that covers all the \
         articles about people, things and events about Africa)**, \
         I got all the QID (unique identification) \
         of the articles that were in the project.

         These QIDs were then used to get the instances for all the articles that \
         fell into this category in the **DPDP** dataset that had at least 1000 daily page views. \
         The page views of the articles are the metric that is being used to measure engagement in this analysis.

         After filtering and retrieving all the relevant rows from the DPDP dataset, I \
         used **Wikidata** to get the *descriptions* and *instances* of all the articles for the \
         analysis.

         While doing this, it became clear that some of the articles in the dataset \
         were not explicitly/clearly relevant to Africa. Some articles were in the \
         dataset even though they had mentioned the continent in passing, such as \
         the article for *Boxing day*

         As such I had to build a classifier to categorize the articles in this dataset\
         as *African* or *Not African*

         After classification, only 53205 rows of data remained. \
         This final data is what was used for the analysis.
         """)

st.divider()

st.subheader("Structure of the Dataset")
st.write("A preview of the data used is provided below")

df = df.drop(columns=["Unnamed: 0", "Unnamed: 0.1"])
st.dataframe(df.head(50))

st.divider()
st.subheader("Descriptive Statistics")
st.write("The following are the descriptive statistics of the dataset based on the pageviews")
st.write(df['views'].describe())