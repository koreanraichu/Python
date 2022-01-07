numeric=list(range(2,20))
with open('19 times 19.txt','w') as f:
    for i in numeric:
        f.write("{0}단\n".format(i))
        for j in numeric:
            f.write("{0} x {1} = {2}\n".format(i,j,i*j))
f.close()
