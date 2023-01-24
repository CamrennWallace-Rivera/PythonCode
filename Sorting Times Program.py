#Camrenn Wallace-Rivera
from random import randint
from Bubble_sort import bubble_sort
import time
from Merge_Sort import merge_sort
from Selection_Sort import selection_sort

def get_aList(item):

    aList=[]

    for i in range(0,item):

        aList.append(randint(1,100))

    return aList

def test(size):

    
    start=time.time()
    
    bubble_sort(get_aList(size))

    end=time.time()

    print((end-start)*1000)

    print(f"bubble_sort:{(end-start)*1000}ms")



    start=time.time()
    
    merge_sort(get_aList(size))

    end=time.time()

    print((end-start)*1000)

    print(f"merge_sort:{(end-start)*1000}ms")

                                    

    start=time.time()
    
    selection_sort(get_aList(size))

    end=time.time()

    print((end-start)*1000)

    print(f"selection_sort:{(end-start)*1000}ms")

   

   


def main():

    for i in range(1,7):

        test(10000*i)

        
    
    

main()


