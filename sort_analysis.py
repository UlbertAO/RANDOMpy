import random
import timeit


def heapify(sqc, end,i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    max = i
    if l < end and sqc[i] < sqc[l]:
        max = l
    if r < end and sqc[max] < sqc[r]:
        max = r
    if max != i:
        swap(sqc,i, max)
        heapify(sqc,end, max)

def heapSort(intList):
    end = len(intList)
    start = end // 2 - 1 
    for i in range(start, -1, -1):
        heapify(intList,end, i)
    for i in range(end-1, 0, -1):
        swap(intList,i, 0)
        heapify(intList,i, 0)
    return intList



def quickSort(L):
    less = [];
    equal = [];
    greater = [];
    if len(L) > 1:
        pivot = random.randrange(0, len(L))
        for x in L:
            if x < L[pivot]:
                less.append(x)
            elif x == L[pivot]:
                equal.append(x)
            else:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)

    else:
        return L;



def mergeSort(li):
    #L = self.intli;
    n = len(li)
    if n is 1:
        return li
    mid = n//2
    firstHalf = li[0:mid]
    secondHalf = li[mid:n]
    B = mergeSort(firstHalf)
    C = mergeSort(secondHalf)
    intList = merge(B, C)
    return intList

def merge(B, C):
    i = j = 0
    A = []
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A.append(B[i])
            i += 1
        else:
            A.append(C[j])
            j += 1
    if i == (len(B)):
        for k in range(j, len(C)):
            A.append(C[k])
    else:
        for k in range(i, len(B)):
            A.append(B[k])
    return A


def bubbleSort(intList): 
    n = len(intList) 
  
    for i in range(n): 
        for j in range(0, n-i-1): 
            if intList[j] > intList[j+1] : 
                intList[j], intList[j+1] = intList[j+1], intList[j]
    return intList

def selectionSort(intList):
        for i in range(len(intList)):
            least = i;
            for j in range(i+1, len(intList)):
                if intList[j] < intList[least]:
                    least = j
            swap(intList, i, least)
        return intList
        
def insertionSort(intList):
    for i in range(1, len(intList)):
        j = i;
        while j > 0 and intList[j] < intList[j-1]:
            swap(intList, j, (j-1))
            j -= 1
    return intList


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    
    
def generateList(listSize):
    randList = list(range(0, listSize));
    for i in randList:
        randList[i] = random.randrange(0, listSize*100);
    return randList

def generateSorted(listSize):
    L = generateList(listSize)
    M = sorted(L)
    return M

def generateReversed(listSize):
    L = generateList(listSize)
    M = sorted(L)
    M.reverse()
    return M



def sort_analysis(fun,size):
    random = generateList(size)
    nonDec = generateSorted(size)
    dec = generateReversed(size)
    
    listList = [random, nonDec, dec]
    listTime = [['Random'], ['Non-Decreasing'],  ['Decreasing']]

    for j in range(len(listList)):
        start=timeit.default_timer()
        M = fun(listList[j])
        runTime=(timeit.default_timer()-start)*1000000
        runTime=float("{:.5f}".format(runTime))
        listTime[j].append(runTime)
    return listTime

'''
l=generateList(10)
print(l)
l=heapSort(l)
print(l)
'''
size=[10,100]
sort=[bubbleSort,selectionSort,insertionSort,mergeSort,quickSort,heapSort]
for i in range(len(size)):
    print("FOR ARRAY SIZE ",size[i])
    print("BUBBLE SORT")
    print(sort_analysis(bubbleSort,size[i])) 
    print("SELECTION SORT")
    print(sort_analysis(selectionSort,size[i])) 
    print("INSERTION SORT")
    print(sort_analysis(insertionSort,size[i])) 
    print("MERGE SORT")
    print(sort_analysis(mergeSort,size[i])) 
    print("QUICK SORT")
    print(sort_analysis(quickSort,size[i])) 
    print("HEAP SORT")
    print(sort_analysis(heapSort,size[i])) 
    
    print()
    
