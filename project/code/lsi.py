import numpy
import scipy
import gensim
import nltk
import codecs
import collections

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from numpy import zeros
from scipy.linalg import svd
from collections import defaultdict
from gensim import corpora, similarities
from gensim import models

stoplist = set(stopwords.words('english'))

def getwords(x):
	with codecs.open(x, "r", encoding='utf-8', errors='ignore') as f:
		line = f.read()
		element = nltk.word_tokenize(line)
	return element




files = []
a = getwords('input.txt')#mention  file names in input.txt
for i in a:
	files.append(i)
#print files

j = 0
documents = []
for i in files:
	documents.append(getwords(files[j]))
	j = j + 1

#print documents



documents = [[word for word in document if word not in stoplist] for document in documents]

frequency = defaultdict(int)
for text in documents:
     for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
          for text in documents]



dictionary = corpora.Dictionary(texts)


corpus = [dictionary.doc2bow(text) for text in texts]


#----------------------------------------------

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]


#lsi
no_of_topic=raw_input("enter no of topic")
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=no_of_topic)
corpus_lsi = lsi[corpus_tfidf]
#x=lsi.print_topics(5)
lsi.save('/tmp/model.lsi')
dictionary.save('/tmp/deerwester.dict')
#print x

#index = similarities.MatrixSimilarity(lsi[corpus])

#_test=open('001.txt','r')
#F=_test.read()
#F=F.strip()
#F=F.split()
#doc = ['Human' , 'computer' , 'Interaction']
#doc=F
#vec_bow = dictionary.doc2bow(doc)
#vec_lsi = lsi[vec_bow] # convert the query to LSI space
#print vec_lsi
#sims = index[vec_lsi]
#sims = sorted(enumerate(sims), key=lambda item: -item[1])
#print sims
#count=0
#for i in sims:
#     print i
#     count=count+1
#     if count > 5:
#        break


