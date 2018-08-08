import csv
import pandas as pd
from sklearn.decomposition import PCA
from numpy import zeros as np
file_=open('1train_dorothea.csv')
w_file=open('VV_train_dorothea.csv','w')
X=np((800,100000),dtype=int)
#print X[1]
row=0
for line in file_:
	line=line.strip()
	line_list=line.split(',')
	for count in line_list:
		count=int(count)
		X[row][count-1]=1
	row=row+1
#print X[0]
df = pd.DataFrame(data=X)
df = df.transpose()
pca = PCA(n_components=500)
pca.fit(df)
#print pca.components_
Y=pca.components_
Y=Y.transpose()
print X.shape,Y.shape
row =0
cloumn=0
while row < 800:
	cloumn=0
	while cloumn < 500:
		w_file.write(str(Y[row][cloumn]))
		if cloumn != 499:
			w_file.write(",")
		cloumn=cloumn+1
	w_file.write("\n")
	row=row+1