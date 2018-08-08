_file1=open('arcene_train.csv','r')
_file2=open('con_arcene_train.csv','w')
for line in _file1:
    line=line.split()
    for i in line:
        if i!=line[-1]:
            _file2.write(str(i))
            _file2.write(',')
        else:
            _file2.write(str(i))
    _file2.write('\n')