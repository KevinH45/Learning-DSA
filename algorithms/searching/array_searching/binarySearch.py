def iterativeBinarySearch(ls, n):
    left = 0  
    right = len(ls)-1  
    mid = 0  
  
    while left <= right:  
        mid = (right + left)//2
        
        if ls[mid] < n:  
            left = mid + 1  
        elif ls[mid] > n:  
            right = mid - 1  
        else:  
            return mid
        
    return None

def recursiveBinarySearch(ls, left, right, n):   
 
   if left <= right:  
      mid = (left + right) // 2  
 
      if ls[mid] > n:   
         return recursiveBinarySearch(ls,left,mid-1,n)   
      elif ls[mid] < n:   
         return recursiveBinarySearch(ls,mid+1,right,n)
      else:
         return mid
   else:   
      return None 
    