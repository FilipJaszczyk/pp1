tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def sumTab(arr):
    if arr == []:
        return arr
    if isinstance(arr[0], list):
        return sumTab(arr[0]) + sumTab(arr[1:]) 
    return sumTab(arr[1:]) + arr[:1]
print(sum(sumTab(tab)))

