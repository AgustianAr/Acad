def linear_search(arr,find):

    
    for i in range(len(arr)):
        
        #jika data merupakan list
        if isinstance(arr[i], list):
            result = linear_search(arr[i], find)
            
            if result != -1:
                print(find, "di index", i, "kolom", result[0])
                exit()

        #jika data merupakan string
        elif isinstance(arr[i], str):
            if arr[i] == find:

                return [i]
    return -1

#data data array yang disediakan
arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print("Data yang disediakan : \n", arr)

#Input data yang akan di search
find = input("find : ")

search = linear_search(arr,find)

if search == -1:
    print(find, "tidak ada dalam array")
else:
    print(find, "di index", search[0])
