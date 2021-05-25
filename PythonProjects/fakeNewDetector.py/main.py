#Importing necessary module

import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#Read the data 
df=pd.read.scv('/Users/rian/Downloads/fake-news/train.csv')

#Get shape and head
df.shape
df.head()

#DataFlair = get the labels
labels = df.label
labels.head()

#Dataflair = split the dataset
x_train,x_test,y_train,y_test = train_test_split(df['text'], labels, text_size=0.2, random_state=7)

#Dataflair = initialize a tfidfvectorizer
Tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

#Dataflair = fit and transform train set, transform test set
Tfidf_train = Tfidf_vectorizer.fit_transform(x_train)
tfidf_test = Tfidf_vectorizer.transform(x_test)

#Dataflair = initialize a passiveaggresiveclassifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(Tfidf_train,y_train)

#Dataflair = Predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

#Dataflair = build confussion matrix
confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])
