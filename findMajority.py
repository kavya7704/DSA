def findMajority(arr):    
  d = {}
  for i in arr:
      if i in d:
          d[i] += 1
      else:
          d[i] = 1
  
  n = len(arr)            
  arr = []
  
  for key,value in d.items():
      if value > n//3:
          arr.append(key)
          
  arr.sort()
  return arr

arr = list(map(int,input().split()))
print(findMajority(arr))
