set1 = {1,2,3,4,5}
set2 = set([2,4,6,8,10,12])

print(len(set2))

print(set1.union(set2))

print(set1.difference(set2))

print(set1.intersection(set2))

set2.remove(12)
print(set2)

set1.update([6,7])
print(set1)