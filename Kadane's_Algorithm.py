def maxSubarraySum(arr):

  res = arr[0]
  
  maxS = arr[0]
  
  for i in range(1,len(arr)):
      
      maxS = max(maxS + arr[i],arr[i])
      
      res = max(maxS,res)
      
  return res

arr = list(map(intinput().split())) #arr[] = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr)) # 11
