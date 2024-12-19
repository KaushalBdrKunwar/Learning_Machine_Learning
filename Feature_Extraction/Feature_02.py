import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('stopwords', quiet=True)

# print(stopwords.words('english'))

#Data Pre-processing 
#loading the dataset to a pandas DataFrame
news_dataset = pd.read_csv(r'C:/Users/legion/Desktop/Data_Science/Datasets/fake_news_dataset.csv')
print(news_dataset.shape)

#print the first five rows
print(news_dataset.head())

#counting the number of missing values in the dataset.
print(news_dataset.isnull().sum())

#replacing the null with empty string
news_dataset = news_dataset.fillna('')

#merging the author name and news title
news_dataset['content'] = news_dataset['author']+' '+news_dataset['title']
print(news_dataset['content'])

#seperating the data and label
X = news_dataset.drop(columns='label', axis=1)
Y = news_dataset['label']

#----Stemming-----#
##stemming is the process of reducing a word to its Root word
#example: actor,actress,acting -> act
port_stem = PorterStemmer()

stop_words = set(stopwords.words('english'))
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower().split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stop_words]
    return ' '.join(stemmed_content)


news_dataset['content'] = news_dataset['content'].apply(stemming)

# print(news_dataset['content'])

#Seperating the data and label
X = news_dataset['content'].values
Y = news_dataset['label'].values

print(X)
print(Y)

#--------TF-IDF---------------#
#convert the textual data to feature vectors
vectorizer = TfidfVectorizer()

vectorizer.fit(X)
X = vectorizer.transform(X)
print(X)
