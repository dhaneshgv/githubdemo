List=[4,2,3,1]
print(List)


def bubblesort(nList):

    n=len(nList)
    #Lenght is used to manipulate indexing

    for i in range(n):
        print("\ni is ",i)
        # i variable is used ignore the last elements which are already swapped

        for j in range(0,n-1-i):
            print('j is ',j,'\tj+1 is',j+1)

            if(nList[j] > nList[j+1]):
                nList[j] , nList[j+1] = nList[j+1] , nList[j]
        print("\nThe List is",nList)      
    
    print(nList)
                

bubblesort(List)