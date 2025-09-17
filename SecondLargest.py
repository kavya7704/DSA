def getSecondLargest(arr):
      largest = -1
      second = -1
      for i in range(0,len(arr)):
          
          if arr[i] > largest:
              second = largest
              largest = arr[i]
              
          elif arr[i] < largest and arr[i] > second:
              second = arr[i]
      
      return second
arr = list(map(int,input().split()))
print(getSecondLargest(arr))
