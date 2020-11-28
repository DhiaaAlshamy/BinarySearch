def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1
        # If n is smaller, compared to the left of mid  
        else:
            return mid  
            # element was not present in the list, return -1  
    return -1  
  # Initial list1  
myList = [12, 24, 32, 39, 45, 50, 54]
print(myList)
n=int(input("Please Enter a number to search using Binary search algorithm  "))
# Function call   
result = binary_search(myList, n)  
if result != -1:  
    print("Element Found in index", str(result))  
else:  
    print("Element not Found in the list ")  