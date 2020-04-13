def count_positives_sum_negatives(arr):
    a = 0
    b = 0
    if arr == ([]): 
         return ([])
    for i in arr:
        if i > 0:
            a += 1
        elif i < 0:
            b += i
    return ([a, b])