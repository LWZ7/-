import random
import time

def Array(n):
    a = []
    for i in range(n):
        a.append(random.randint(0 , n))
    return a

def find(n):
    array = Array(100)
    array = sorted(array)
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] > n:
            right = mid - 1
        elif array[mid] < n:
            left = mid + 1
        else:
            return mid
    print("找不到")
    return -1
#-------取第k大元素-------
def QuickSort(n):
    array = Array(100)
    if n > len(array) or n < 1:
        print("超出范围，找不到")
        return
    n = n-1
    a = qsort(0 , len(array)-1 , array , n)
    print(sorted(array))
    print("-----------------------------")
    print(a)

def qsort(start , end , array , n):
    if start == end:
        res = array[start]
    if start < end:
        key = partation(array , start , end)
        print(start , key , end)
        if key > n :
            res = qsort(start , key-1 , array , n)
        elif key < n:
            res = qsort(key+1 , end , array , n)
        else:
            res = array[key]
    return res

def swap(array , start , end):
    temp = array[start]
    array[start] = array[end]
    array[end] = temp

def partation(array , start , end):
    temp = array[start]
    while start < end :
        while start<end and array[end]<=temp:
            end-=1
        swap(array , start , end)
        while start<end and array[start]>=temp:
            start+=1
        swap(array , start , end)
    return start

#查找第一个值等于给定值的元素
def find_1(n):
    array = Array(100)
    array = sorted(array)
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] > n:
            right = mid - 1
        elif array[mid] < n:
            left = mid + 1
        else:
            if mid==0 or array[mid] != array[mid-1]:
                return mid
            else:
                right = mid - 1
    print("找不到")
    return -1

#查找最后一个值等于给定值的元素
def find_2(n):
    array = Array(100)
    array = sorted(array)
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] > n:
            right = mid - 1
        elif array[mid] < n:
            left = mid + 1
        else:
            if mid==right or array[mid] != array[mid+1]:
                return mid
            else:
                left = mid + 1
    print("找不到")
    return -1

#查找第一个值大于等于给定值的元素
def find_3(n):
    array = Array(100)
    array = sorted(array)
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] >= n:
            if mid==0 or array[mid-1]<n:
                return mid
            else:
                right = mid - 1
        else array[mid] < n:
            left = mid + 1
    print("找不到")
    return -1

#查找最后一个值小于等于给定值的元素
def find_4(n):
    array = Array(100)
    array = sorted(array)
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left+right)/2)
        if array[mid] <= n:
            if mid==right or array[mid+1]>n:
                return mid
            else:
                left = mid + 1
        else array[mid] > n:
            right = mid - 1
    print("找不到")
    return -1

#循环数组的二分查找
def find_5(n):
    array = [4 , 5 , 6 , 1 , 2 , 3]
    left = 0
    right = len(array)-1
    while left < right:
        mid = int((left+right)/2)
        if array[mid] > array[right]:
            left = mid+1
        else:
            right = mid
    temp = left
    left = 0
    right = len(array)-1
    if n < array[left]:
        left = temp
    else:
        right = temp-1
