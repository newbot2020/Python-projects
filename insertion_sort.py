
# give the list which you like to sort
def insertion_sort(list):
    
    for i in range(2,len(a)) :
        item=a[i]
        j=i-1
        # checking if the element is bigger than before
        while(j>=0 and a[j]>item):
            a[j+1]=a[j]
            j=j-1

        a[j+1]=item
    return a

