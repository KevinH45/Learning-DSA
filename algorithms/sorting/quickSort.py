def quickSort(ls):
    
    length = len(ls)

    
    # Base Case 1
    if length<2:
        return ls

    # Base Case 2
    elif length==2:
        if ls[0] > ls[1]:

            # Swap the two values if the list isn't in the right order
            ls[0], ls[1] = ls[1], ls[0]
        return ls
    
    elif length>2:
        pivot = ls[0]
        more = []
        less = []

        # Since the pivot is at index 0, start at index 1
        for i in ls[1:]:

            # Instead of partitioning in-place, we use two different lists
            if i>pivot:
                more.append(i)
                
            elif i<=pivot:
                less.append(i)

        
        # Recursive Call        
        sortedLess=quickSort(less)
        sortedMore=quickSort(more)

        # Return the sorted list
        return sortedLess+[pivot]+sortedMore