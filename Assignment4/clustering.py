from sklearn import svm
from sklearn import metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA, KernelPCA
from sklearn.cluster import AgglomerativeClustering, SpectralClustering
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
_file1=pd.read_csv('arcene_train.csv', delim_whitespace=True)
#print _file1.shape
_file2=pd.read_csv('arcene_train.labels')
_file1['Class'] = (_file2['1']).astype(int)
_file1= _file1.fillna(lambda x: x.median())
train, test = train_test_split(_file1, test_size = 0.4)
train=train.values.tolist()
test=test.values.tolist()
#print len(train[:][:]),len(test)
x=[]
y=[]
for i in train:
	x.append(i[:-2])
	y.append(i[-1])


model1=SpectralClustering(7,n_init=10)
X=model1.fit(x)
#print X
#print model1.get_params()
z=model1.fit_predict(x)
# score1=metrics.adjusted_rand_score(y,z)
# score2=metrics.adjusted_mutual_info_score(y, z)
# print "train"
# print "Adjusted Rand index"
# print score1
# print "Mutual Information based scores"
# print score2
# #print z,y
for i in test:
	x.append(i[:-2])
	y.append(i[-1])
print "test"
z=model1.fit_predict(x)
z=z[:]
print z.shape,len(y)
score1=metrics.adjusted_rand_score(y,z)
score2=metrics.adjusted_mutual_info_score(y, z)
print "Adjusted Rand index"
print score1
print "Mutual Information based scores"
print score2
