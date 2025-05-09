def SS(arr,n):
    
    for i in range(n-1):
        min_Index = i
        for j in range(i+1,n):
            if arr[min_Index] > arr[j]:
                min_Index = j


        if(min_Index!= i):
            arr[i],arr[min_Index] = arr[min_Index],arr[i]


    

arr = [10,1,3,216,8]

SS(arr,len(arr))

print(arr)