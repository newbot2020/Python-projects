a=[4,8,1,5,9,6,3,2]
index_min=0
for i in range (len(a)-1):
    for j in range (len(a)-1-i):
        if(a[i+j]>a[i+j+1]):
            index_min=j+i+1
            temp=a[i+j]
            a[i+j]=index_min
            a[i+j+1]=temp


print("The ascending sorted list is : {}".format(a))