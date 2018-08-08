import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles
import pandas as pd

np.random.seed(0)
N_com=raw_input("ENTER required no of components")
#X, y = make_circles(n_samples=400, factor=.3, noise=.05)
#print X.shape
_file_train=open('arcene_train.csv','r')
w_file=open('output.csv','w')
Stor_train=[]
for line in _file_train:
    line=line.strip()
    line=line.split()
    tmp=[]
    for i in line:
        tmp.append(int(i))

    Stor_train.append(tmp)

X=pd.DataFrame(data=Stor_train)
#X=X.transpose()
print X.shape
kpca = KernelPCA(n_components=N_com,kernel="rbf", fit_inverse_transform=True, gamma=10)
X_kpca = kpca.fit_transform(X)
X_back = kpca.inverse_transform(X_kpca)
pca = PCA()
X_pca = pca.fit_transform(X)
print X_pca.shape
print X_kpca.shape
#X_kpca=X_kpca.transpose()
# Plot results
#print X_back.shape
row =0
cloumn=0
while row < 100:
	cloumn=0
	while cloumn < N_com:
		#print row,cloumn
		w_file.write(str(X_kpca[row][cloumn]))
		if cloumn != N_com-1:
			w_file.write(",")
		cloumn=cloumn+1
	w_file.write("\n")
	row=row+1