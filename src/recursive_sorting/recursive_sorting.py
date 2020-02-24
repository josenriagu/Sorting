# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    while len(arrA) != 0 and len(arrB) != 0:
        # compare elements at index zero for  both lists
        if arrA[0] < arrB[0]:
            # if index zero for first list is smaller, append to merged_arr, then remove from the parent list
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            # otherwise, do the reverse
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    # when the first list is now empty, append the second list
    if len(arrA) == 0:
        merged_arr += arrB
    # otherwise, do the reverse
    else:
        merged_arr += arrA
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # base case
    if len(arr) < 2:
        return arr
    # TO-DO
    # find the midpoint of the list
    midpoint = len(arr) // 2
    # split the list into two halves from the midpoint and recursively call merge_sort
    LHS = merge_sort(arr[: midpoint])
    RHS = merge_sort(arr[midpoint:])
    # call the helper function on the halves
    return merge(LHS, RHS)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
