def bubbleSort(ls):

    for i in range(len(ls)):
        swapOccured = False

        # -1 so IndexError does not occur
        for j in range(len(ls)-1):

            if ls[j] > ls[j+1]:

                swapOccured = True

                # Swapping the variables
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp


        # If no swap occurs, that means the list is sorted
        if not swapOccured:
            break

    return ls