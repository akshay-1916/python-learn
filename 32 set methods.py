s={"akshay","kokare",15,2015,111}
l={"man","kokare","animal",15,44}
# print(s.union(l))
s.update(l)
# print(s,l)
t=s.symmetric_difference(l)
print(t)
print(s.issuperset(l))
print(s.issubset(l))
s.add("ak")
print(s)
r=s.pop()
print(r)
del s
del r