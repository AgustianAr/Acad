import random 

def quick_sort(arr): 

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2] 
    print("Pivot :", pivot)
    left = [x for x in arr if x < pivot]
    print("left",left)
    middle = [x for x in arr if x == pivot]
    print("middle : ",middle)
    right = [x for x in arr if x > pivot]
    print("right : ",right)
    print() 

    return quick_sort(left) + middle + quick_sort(right)



Random_Numbers = random.sample(range(1, 51), 10)
print("\nUnsorted Numbers :\n",Random_Numbers,"\n")

sorting = quick_sort(Random_Numbers)

sorted_array = []

sorted_array.append(sorting)
print("Sorted array :\n",sorted_array,"\n")  

