s = {1, 4, 2.2, 9}
s1 = {2.2, 9, 55}

print(s.difference(s1))
s.update(s1)
s.discard(1)
print(s)