#Sms Spam filter

import pandas as pd
import nltk
import string

'''Fetching and adding column name to the sample dataset (.txt file) of spam & ham messages '''

data = pd.read_csv(r"E:\PY\spam_set.txt",sep="\t",header=None,names=['label','message'])

'''get corpus text of stop words in english language
initialize punctuations to process the data'''

stop_words = nltk.corpus.stopwords.words('english')
punc = string.punctuation

#Pre-processing

def processData(text):
    '''pass the user input to pre-process the data.
The processed data will be the result
it includes stop word removal,punctuation removal and tokenization process'''
    
    processed = "".join([word.lower() for word in text if word not in punc])
    tokens = nltk.tokenize.word_tokenize(processed)
    processed = [word for word in tokens if word not in stop_words]
    return processed

col = data['message']
func = lambda sms:processData(sms)
data['processed'] = col.apply(func)

#categorizing the data

def categorize():
    '''categorizing the data into two classes namely spam and ham
Returns list of spam and ham words'''
    
    spam_words = []
    ham_words = []
    for words in data['processed'][data['label'] == 'spam']:
        for word in words:
             spam_words.append(word)
    for words in data['processed'][data['label'] == 'ham']:
        for word in words:
            ham_words.append(word)

    return spam_words,ham_words

spam_words,ham_words = categorize()

#predict the user input message whether it is spam or not

def check(input_):
    '''it gets processed user input as parameter to predict the class with accuracy in percentage'''
    
    spam_count = 0
    ham_count = 0
    for words in input_:
        spam_count += spam_words.count(words)
        ham_count += ham_words.count(words)

    if spam_count > ham_count:
        accuracy = (spam_count/(spam_count+ham_count))*100
        print("SPAM! with accuracy of {:.2f}% ".format(accuracy))
    elif ham_count > spam_count:
        accuracy = (ham_count/(spam_count+ham_count))*100
        print("NOT A SPAM ! with accuracy of {:.2f}%".format(accuracy))
    else:
        print("50% CHANCE OF SPAM !")

sms = input("Enter the message: ")
processed_sms = processData(sms)

check(processed_sms)
