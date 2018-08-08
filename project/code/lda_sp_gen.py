import os
import os.path
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
from os import listdir
from os.path import isfile, join


def getwords(x):
    with codecs.open(x, "r", encoding='utf-8', errors='ignore') as f:
        line = f.read()
        element = nltk.word_tokenize(line)
        element = [w for w in element if w not in stop_set and len(w) > 1]
    return element


def getdirectory_name(d):
    return [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]


def  getfiles_in_dir(directory):
    return  [f for f in listdir(directory) if isfile(join(directory, f))]



d='datasets'
directory_name =  getdirectory_name(d)
#print directory_name

#directory name is selected

file_names = []
for i in directory_name:
    mypath = i
    Files = getfiles_in_dir(i)
    file_names.append(Files)
    #print mypath


stop_list = set(stopwords.words('english'))
stop_set = set(stop_list)

documents = []
for  i in range(len(directory_name)):
    d = []
    for k in file_names[i]:
        x = directory_name[i]  +  '/' + str(k)
        #print x
        d.append(getwords(x))
    documents.append(d)
#print documents
#for i in documents:
 #   print len(i)

#print len(documents)
_Dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')

dictionary = {}

for i in range(len(directory_name)):
    dictionary[i] =  documents[i]

lsi_space=open('lda_space.csv','w')

lda = models.LdaModel.load('/tmp/model.lsi')
for key, value in dictionary.items():
    for F in value: 
        doc=F
        vec_bow = _Dictionary.doc2bow(doc)
        vec_lsi = lda[vec_bow] # convert the query to LSI space
        vec_lsi=list(vec_lsi)
        #print vec_lsi[0][1]
        lsi_space.write(str(key+1))
        for j in vec_lsi:
            lsi_space.write(",")
            lsi_space.write(str(j[1]))
        lsi_space.write("\n")


#--------------------------------------------------------IMPORTANT POINT--------------------------------------------------------------------------                                  
#if you want only numbers in the place of dictionary replace 'directory_name[i]' in line 72 with  i 








