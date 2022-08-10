List=[4,2,3,1]

def selectionSort(List):
    l=len(List)
    
    minIndex = 0

    for i in range(l):
        minIndex=i
        
        for j in range(i+1,l):
            if(List[j]<List[minIndex]):
                minIndex=j

        List[minIndex],List[i]=List[i],List[minIndex]

    print(List)

selectionSort(List)