e= set()
print(type(e))

s={10,12,13,10,10,14,10,10,10}
print(s)
s.add(20)
print(s)
s.remove(13)
print(s)

s1={100,200,300}
s2={100,300,500,700}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
