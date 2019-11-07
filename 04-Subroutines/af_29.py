from statistics import median,mode
tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
def medianSelf(arr):
    #działa dla parzystej ilości liczb w tablicy
    arrSorted = sorted(arr)
    mediana = (arrSorted[int(len(arrSorted)/2)] + arrSorted[int((len(arrSorted)/2)-1)])/2
    return mediana

#dominanta == mode
def modeSelf(arr):
    return max(set(arr), key=arr.count)
def medianStat(arr):
    return median(arr)
def modeStat(arr):
    return mode(arr)

print(medianSelf(tab))
print(modeSelf(tab))
print(medianStat(tab))
print(modeStat(tab))
