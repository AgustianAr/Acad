#Linear Search

Linear Search adalah sebuah Algoritma Search yang melakukan search dengan cara mencocokkan data dari data yang paling kiri ke kanan dengan data yang ingin dicari. 



    def linear_search(arr,find):

Pertama, pada program dibuat sebuah function agar memudahkan mengeksekusi program nantinya

    for i in range(len(arr)):
   
lalu dibuat perulangan for untuk meng iterate atau melakukan perulangan satu per satu data yang ada dalam array

    if isinstance(arr[i], list):
            result = linear_search(arr[i], find)
            
            if result != -1:
                print(find, "di index", i, "kolom", result[0])
                exit()
                
jika data merupakan list bercabang, program akan melakukan search ke dalam list tersebut dan akan mengoutput index dari list bercabang dan index data dalam list bercabang tersebut. jika data yang dicari tidak ada program akan mengecek data yang lain

    elif isinstance(arr[i], str):
            if arr[i] == find
                
                return [i]       

jika data bukan merupakan list bercabang melainkan string. maka, program akan mencompare ata mencocokkan dengan data yang dicari dan akan melakukan return index jika data sesuai dengan data yang dicari. jika data tidak sesuai maka program akan lanjut mencompare ke data lain

    return -1
    
 jika tidak ada data yang sesuai di array dengan daya yang dicari maka program akan melakukan return -1
 
    arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
    print("Data yang disediakan : \n", arr)
    
    find = input("find : ")
    
 array yang tersedia dan input data yang akan di search 

    search = linear_search(arr,find)

eksekusi function linear search

    if search == -1:
       print(find, "tidak ada dalam array")
    else:
       print(find, "di index", search[0])
       
jika data yang dicari tidak ditemukan oleh program maka program akan me return -1. dan program akan meng-output bahwa data yang dicari tidak ada dalam array.  
jika data di temukan dalam array berupa string bukan list bercabang maka program akan meng-output data yang dicari dan letak index dari data tersebut.

       
 


Elements :
- def

elemen 'def' berfungsi untuk membuat sebuah function yang dapat dieksekusi saat dipanggil
- for

elemen 'for' disini digunakan untuk melakukan perulangan ke setiap data yang ada di dalam array

-isinstance

elemen function ini mengeksekusi data jika data memiliki tipe tertentu

- if

elemen ini mengksekusi data jika syarat yang ada terpenuhi

-input

elemen ini membuat user dapat melakukan input.

    
