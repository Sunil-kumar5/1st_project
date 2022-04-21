def bubblesort(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1], l[j]
    print(l)
l = [1,2,3,1,4,5,3,5,65,44]
bubblesort(l)