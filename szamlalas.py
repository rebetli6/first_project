numbers= [11, 24, 55, 12, 21]

s=[]
for c in numbers:
    if c%2 == 0:
        s.append(c)

print(s)

names = ["John Doe", "mike", "Jack Doe"]
s=[]
for c in names:
    s.append(len(c))
print (s)