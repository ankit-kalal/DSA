def binarySearch(arr,key):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2

    while start<=end:
        if arr[mid]==key:
            return mid

        if arr[mid]>key:
            end = mid-1
        else:
            start = mid+1

        mid = (start+end)//2
    
    return -1



if __name__ == '__main__':
  even = [2,4,6,8,12,18]
  odd = [3, 8, 11, 14, 16]
  
  evenIndex = binarySearch(even, 6)
  print("Index of 6 is: ", evenIndex)
  
  oddIndex = binarySearch(odd, 14)
  print("Index of 14 is: ", oddIndex)