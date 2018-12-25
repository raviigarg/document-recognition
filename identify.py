# import required packages
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# import dataset into pandas dataframe using the read_table method
"""
dataset is tab separated.
we will be using '\t' as the value for 'sep' argument which specify this format.
rename the column by specifying a list ['label', 'content'] to the 'names' argument of read_table().
"""
df = pd.read_table("doccollection/DocCollection", sep='\t', header=None, 
                   names=['label', 'content'])

# Data Preprocessing
# map labels yes to 1 and no to 0
df['label'] = df.label.map({'no':0, 'yes':1})

# prepare training data
x_train = df['content']
y_train = df['label']

# applying Bag of Words processing to our dataset using count vectorizer 
count_vector = CountVectorizer()
training_data = count_vector.fit_transform(x_train)

# apply Naive Bayes algorithm
# fit training data to Multinomial Naive Bayes classifier in sckit-learn
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)
print("Data preprocessing done")



