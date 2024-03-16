# storing functions for easy access

import pandas
import re
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Data cleaning function from EDA notebook

def make_df():
    # Reading in the data
    df = pandas.read_csv("Phishing_Email.csv")
    # Dropping the unecessary index row
    df = df.drop(df.columns[0], axis=1)
    
    #calculate counts before cleaning
    num_rows = df.shape[0]
    num_nulls = df['Email Text'].isnull().sum()
    num_emptys = (df['Email Text'].str.lower() == 'empty').sum()
    num_not_empty_and_not_null = num_rows - num_nulls - num_emptys
    
    # Removing Nulls
    # Check for null values in the "Email Text" column
    null_mask = df["Email Text"].isnull()

    # If there are null values, drop the corresponding rows
    if null_mask.any():
        df = df.drop(df[null_mask].index)
        
    #Remove 'empty' emails from the dataframe
    df_cleaned = df[df['Email Text'].str.lower() != 'empty']
    df = df_cleaned
    
    return df




# Download NLTK resources (uncomment if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK resources
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Preprocessing and tokenization function
def preprocess_and_tokenize(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return tokens