from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA, KernelPCA
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
_file1=pd.read_csv('arcene_train.csv', delim_whitespace=True)
_file2=pd.read_csv('arcene_train.labels')
_file1['Class'] = (_file2['1']).astype(int)
#print _file1.isnull()
#print _file1.info()##################################################################################cleaning missing values
_file1= _file1.fillna(lambda x: x.median())
#print _file1.info()
#print _file1
train, test = train_test_split(_file1, test_size = 0.4)
linear_svm=svm.SVC(kernel='linear')########################################################################linear_SVM
rbf_svm=svm.SVC(kernel='rbf')##############################################################################rbf_SVM
kpca = KernelPCA(n_components=55,kernel="rbf", fit_inverse_transform=True, gamma=10)#######################################KPCA

#print train,test
train=train.values.tolist()
test=test.values.tolist()
#print len(train[:][:]),len(test)
###########################################################################################################################data
x=[]
y=[]
for i in train:
	x.append(i[:-2])
	y.append(i[-1])
########################################################################################################################end data

###############################################################################################kpca
X_kpca = kpca.fit_transform(x)
X_back = kpca.inverse_transform(X_kpca)
pca = PCA()
X_pca = pca.fit_transform(x)
#X_kpca=X_kpca.values.tolist()
#print X_kpca
linear_svm.fit(X_kpca,y)
rbf_svm.fit(X_kpca,y)
x=[]
for i in X_kpca:
	x.append(i[:])
P_l=linear_svm.predict(x)
P_r=rbf_svm.predict(x)
#print P_l[:],P_r[:],y
acc_l=0
acc_r=0
total=0
for i in y:
	if P_l[total]==i:
		acc_l=acc_l+1
	if P_r[total]==i:
		acc_r=acc_r+1
	total=total+1
A_l=acc_l/float(total)
A_r=acc_r/float(total)
print "linear  rbf with n_components"
print A_l*100,A_r*100