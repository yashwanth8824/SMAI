from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA, KernelPCA
from sklearn.cluster import AgglomerativeClustering, SpectralClustering
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn import metrics
from sklearn.cross_validation import train_test_split
_file1=pd.read_csv('arcene_train.csv', delim_whitespace=True)
_file2=pd.read_csv('arcene_train.labels')
_file1['Class'] = (_file2['1']).astype(int)
##################################################################################cleaning missing values
_file1= _file1.fillna(lambda x: x.median())
#print _file1
train, test = train_test_split(_file1, test_size = 0.4)
linear_svm=svm.SVC(kernel='linear')########################################################################linear_SVM
rbf_svm=svm.SVC(kernel='rbf')##############################################################################rbf_SVM
sigmoid_svm=svm.SVC(kernel='sigmoid')
poly_svm=svm.SVC(kernel='poly')
#print train,test
train=train.values.tolist()
test=test.values.tolist()
#print len(train[:][:]),len(test)
x=[]
y=[]
for i in train:
	x.append(i[:-2])
	y.append(i[-1])
#print len(x),y
_lda = PCA(n_components=200)#########################################################################LDA
_lda.fit(x, y)
z=_lda.transform(x)


kmeans = KMeans(n_clusters=2, random_state=0).fit(z)
l=kmeans.predict(z);
#print l ,y
score1=metrics.adjusted_rand_score(y,l)
score2=metrics.adjusted_mutual_info_score(y, l)
print "Adjusted Rand index"
print score1
print "Mutual Information based scores"
print score2


#print z.shape
#print len(z)
# linear_svm.fit(z,y)
# rbf_svm.fit(z,y)
# sigmoid_svm.fit(z,y)
# poly_svm.fit(z,y)
# x=[]
# y=[]
# for i in test:
# 	x.append(i[:-2])
# 	y.append(i[-1])
# z=_lda.transform(x)
# P_l=linear_svm.predict(z)
# P_r=rbf_svm.predict(z)
# P_s=sigmoid_svm.predict(z)
# P_p=poly_svm.predict(z)
# #print P_l[:],P_r[:],y
# acc_l=0
# acc_r=0
# acc_s=0
# acc_p=0
# total=0
# for i in y:
# 	if P_l[total]==i:
# 		acc_l=acc_l+1
# 	if P_r[total]==i:
# 		acc_r=acc_r+1
# 	if P_s[total]==i:
# 		acc_s=acc_r+1
# 	if P_p[total]==i:
# 		acc_p=acc_r+1
		
# 	total=total+1
# A_l=acc_l/float(total)
# A_r=acc_r/float(total)
# A_s=acc_s/float(total)
# A_p=acc_p/float(total)
# print A_l*100,A_r*100,A_s*100,A_p*100