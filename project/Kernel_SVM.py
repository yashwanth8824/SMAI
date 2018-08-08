from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
_file1=pd.read_csv('TEST_LDA_SPACE/lda_space(700).csv')
#_file2=pd.read_csv('arcene_train.labels')
#_file1['Class'] = (_file2['1']).astype(int)
#print _file1
train, test = train_test_split(_file1, test_size = 0.4)
linear_svm=svm.SVC(kernel='linear')
rbf_svm=svm.SVC(kernel='rbf')
sigmoid_svm=svm.SVC(kernel='sigmoid')
poly_svm=svm.SVC(kernel='poly')
#print train,test
train=train.values.tolist()
test=test.values.tolist()
#print len(train[:][:]),len(test)
x=[]
y=[]
for i in train:
    x.append(i[1:])
    y.append(i[0])
#print len(x),y
linear_svm.fit(x,y)
rbf_svm.fit(x,y)
sigmoid_svm.fit(x,y)
poly_svm.fit(x,y)
x=[]
y=[]
for i in test:
    x.append(i[1:])
    y.append(i[0])
P_l=linear_svm.predict(x)
P_r=rbf_svm.predict(x)
P_s=sigmoid_svm.predict(x)
P_p=poly_svm.predict(x)
#print P_l[:],P_r[:],y
acc_l=0
acc_r=0
acc_s=0
acc_p=0
total=0
for i in y:
    if P_l[total]==i:
        acc_l=acc_l+1
    if P_r[total]==i:
        acc_r=acc_r+1
    if P_s[total]==i:
        acc_s=acc_s+1
    if P_p[total]==i:
        acc_p=acc_p+1
    total=total+1
A_l=acc_l/float(total)
A_r=acc_r/float(total)
A_s=acc_s/float(total)
A_p=acc_p/float(total)
print "Linear",A_l*100,"RBF",A_r*100,"Sigmoid",A_s*100,"poly",A_p*100