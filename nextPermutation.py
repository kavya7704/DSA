def nextPermutation(arr):
  n = len(arr)
  pivot = -1
  for i in range(n - 2, -1, -1):
      if arr[i] < arr[i + 1]:
          pivot = i
          break
          
  if pivot == -1:
      arr.reverse()
      return arr
  
  for i in range(n - 1, -1, -1):
      if arr[i] > arr[pivot]:
          arr[pivot], arr[i] = arr[i], arr[pivot]
          break
      
  r, l = pivot + 1, n - 1
  while r < l:
      arr[r], arr[l] = arr[l], arr[r]
      r += 1
      l -= 1

arr = list(map(int,input().split()))
print(nextPermutation(arr))
        return arr
