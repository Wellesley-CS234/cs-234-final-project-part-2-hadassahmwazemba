import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Text Classification",
    layout="wide",
    initial_sidebar_state="expanded"
)



#Read the csv
PATH = "data/groundtruth_df.csv"
df = pd.read_csv(PATH)


st.title("Text Classification (African Vs Non-African)")


st.subheader("1. Establishment of the Ground truth")
st.write("""
         In order to build a classifier to categories the articles as either \
         African or Non-African, I had to establish the ground truth.
         
         To do so, I used the Wikidata attributes *country* and *country \
         of citizenship* of the articles from WikiProject Africa (around 120000) to filter and retrieve articles that were explicitly about \
         people, locations and events in Africa. I collected about **28000** that fit \
         into this criteria.
         
         Below is a snippet of the ground truth data after collection""")

df = df.drop(columns=['Unnamed: 0'])
st.dataframe(df.head(15))

st.divider()
st.subheader("2. Building the classifier")

st.write("""
         I built the classifier using Naive bayes using the following steps.
         
         1. Training the model.
            I used the description column to train the model
            70% percent of the data was used training and 30% was used for testing
            For the training data not about Africa, I filtered out all the QIDs \
            from the WikiProject Africa dataset in the DPDP set to ensure that the articles being used were not related\
            to the continent.
         
         2. Vectorizing the data
            I vectorized the data using **TF-IDF**
         
         3. Modelling
            I used **Multinomial Naive Bayes** as my classifier.""")

st.divider()
st.subheader("3. Evaluation of the Model")
st.write("""
         To evaluate the model, I used a confusion matrix to visualize the classification report
         
         The results of the classifier were as follows:
         1. Precision = 96%
         2. Recall = 96%
         3. F1-Score = 96%""")

st.divider()
st.subheader("4. Classified Results")
st.write("""
         I used the model to classify the articles that I had collected from the WikiProject Africa dataset \
         to find articles that were clearly and explicitly related to Africa for my analysis.""")

st.write("Below is a snippet of the articles that were labelled as African \
         after classification using the description \
         column as the classifying input data")

african_classified = pd.read_csv("data/african_classified.csv")

african_classified = african_classified.drop(columns=['Unnamed: 0'])

st.write(african_classified.tail(50))

