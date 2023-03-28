# SMS Spam Filter

This code has simple logic to classify the spam messages and to predict the user input message for which class it belongs to. It uses simple [classification](https://www.javatpoint.com/classification-algorithm-in-machine-learning) technique. Here, [NLP(Natural Language Processing)](https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP) techniques like tokenization, stop word removal process is used.  

## Installation
To install the required packages use pip command

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install libraries.

```bash
pip install [package-name]
```

## Usage
### Importing packages

```python
import pandas as pd
import nltk
import string
```
### To read the dataset
```python
data = pd.read_csv(r"...\spam_set.txt",sep="\t",header=None,names=['label','message']')
```
sep is a argument that accepts the delimiters names is an another argument that accepts iterable data to name the columns of dataset. 

### To display top few data from the dataset
```python
print(data.head())
```
### To Download the required nltk sub packages
```python
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
```
### To use Stop words and punctuations
```python
stop_words = nltk.corpus.stopwords.words('english')
punc = string.punctuation
```
### Applying NLP Techniques
```python
processed = "".join([word.lower() for word in text if word not in punc])
tokens = nltk.tokenize.word_tokenize(processed)
processed = [word for word in tokens if word not in stop_words]
```
### Classification of data
```python
spam_words = []
ham_words = []
for words in data['processed'][data['label'] == 'spam']:
    for word in words:
         spam_words.append(word)
for words in data['processed'][data['label'] == 'ham']:
    for word in words:
          ham_words.append(word)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/thirumalairaaj-c-v-b05036224)
