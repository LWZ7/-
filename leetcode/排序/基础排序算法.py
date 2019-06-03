import random
import time

def Array(n):
    a = []
    for i in range(n):
        a.append(random.randint(0 , n))
    return a
#---------插入排序----------
def insert():
    array = Array(100)
    time_start=time.time()
    for i in range(1 , len(array)):
        for j in range(i , 0 , -1):
            if array[j] > array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else:
                break
    time_end=time.time()
    print(array)
    print('totally cost',time_end-time_start)

#考点：为什么用插入而不用冒泡？

#选择排序无法做像冒泡排序那样的优化，是因为选择排序无法保证交换的时候之后的元素位置也会变
def select():
    array = Array(100)
    time_start=time.time()
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            if array[j] > array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    time_end=time.time()
    print(array)
    print('totally cost',time_end-time_start)

#如果出现提前排完序的情况，遍历一遍就不再有数据交换，所以可以退出了
#冒泡排序是每次外循环都能保证至少有一个元素回归到正确的位置上，并且在它之后的所有元素的位置都会改动，所以可以做这样的优化，而插入排序就不可以
def bubble():
    array = Array(100)
    time_start=time.time()
    for i in range(len(array)-1 , 0 , -1):
        flag = False
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = True
        if not flag:
            break
    time_end=time.time()
    print(array)
    print('totally cost',time_end-time_start)
#考点：冒泡的优化

#--------------快排(三数取中)-------------
def QuickSort():
    array = Array(100)
    time_start=time.time()
    qsort(0 , len(array)-1 , array)
    time_end=time.time()
    print(array)
    print('totally cost',time_end-time_start)

def qsort(start , end , array):
    if start < end:
        key = partation(array , start , end)
        qsort(start , key-1 , array)
        qsort(key+1 , end , array)

def swap(array , start , end):
    temp = array[start]
    array[start] = array[end]
    array[end] = temp

def change(array , start , mid , end):
    if array[start] > array[mid]:
        swap(array , start , mid)
    if array[start]>array[end]:
        swap(array , start , end)
    if array[mid] > array[end]:
        swap(array , mid , end)
    swap(array , mid , start)

def partation(array , start , end):
    #mid = int((start+end)/2)
    #change(array , start , mid , end)
    temp = array[start]
    while start < end :
        while start<end and array[end]<=temp:
            end-=1
        swap(array , start , end)
        while start<end and array[start]>=temp:
            start+=1
        swap(array , start , end)
    return start

#考点：为什么一定是end比start先?
#      怎么分析快排的时间复杂度？最好的情况和最坏的情况分别是怎么样的？
#      怎么对快排进行优化？
#      O(n)的时间复杂度求Top n 大小的数


#------------------归并-----------------
def merge(a , b):
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i] > b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i>=len(a):
        for k in range(j , len(b)):
            c.append(b[k])
    if j>=len(b):
        for k in range(i , len(a)):
            c.append(a[k])
    return c

def devide(array):
    if len(array) == 1:
        return array
    else:
        mid = int((0 + len(array)) / 2)
        leftArray = devide(array[0:mid])
        rightArray = devide(array[mid:len(array)])
        return merge(leftArray , rightArray)
    
def mergesort():
    array = Array(100)
    time_start=time.time()
    m = devide(array)
    time_end=time.time()
    print(m)
    print('totally cost',time_end-time_start)
#--------希尔排序---------
def Shell():
    array = Array(100)
    size = len(array)
    h = int(size/2)
    while h > 0:
        for i in range(h , size):
            temp = array[i]
            for j in range(i , h-2 ,-h):
                if temp > array[j-h]:
                    array[j] = array[j-h]
                else:
                    break
            array[j] = temp
        h = int(h / 2)
    print(array)

#-----堆排序--------
def makeHeap(array , i ,N):
    while 2*i+1 < N:
        child = 2*i+1
        if child != N-1 and array[child] < array[child+1]:
            child+=1
        if array[child] > array[i]:
            temp = array[child]
            array[child] = array[i]
            array[i] = temp
            i = child
        else:
            break
def heapSort():
    array = Array(100)
    for i in range(int(len(array)/2) , -1 , -1):
        makeHeap(array , i , len(array))
    for i in range(len(array)-1 , -1 , -1):
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        makeHeap(array , 0 , i)
    print(array)
