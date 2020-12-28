#for binary Search The list must be already sorted
myList = []

def binarySearch(myList, ele):
    low = 0
    high = len(myList)
    while low <= high:
        mid = int(low + (high-low)/2)
        guess = ele
        if guess == myList[mid]:
            print(mid)
            low = high+1
        elif guess < myList[mid]:
            high = mid-1
        else:
            low = mid+1
    return None
        
n = int(input("Enter the size of array "))
for i in range(n):
    i = int(input())
    myList.append(i)
    
print(myList) # prints the lists
ele = int(input("Enter the ele you want to search "))
binarySearch(myList, ele)
