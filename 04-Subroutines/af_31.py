def reverse(tab):
    arr = []
    while len(tab) > 0:
        x = tab.pop()
        arr.append(x)
    tab = arr
    return tab

print(reverse([2, 5, 4, 1, 8, 7, 4, 0, 9]))
