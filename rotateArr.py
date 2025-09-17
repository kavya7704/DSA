def rotate(arr, s, e):
  while s < e:
      arr[s], arr[e] = arr[e], arr[s]
      s += 1
      e -= 1
            
def rotateArr(arr, d):

    n = len(arr)
    d %= n
    
    self.rotate(arr, 0, d-1)
    
    self.rotate(arr, d, n-1)
    
    self.rotate(arr, 0, n-1)
    
    return arr

arr = list(map(int,input().split()))
d = int(input())
print(rotateArr(arr,d))
