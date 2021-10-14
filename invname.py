name = "John Doe"
c=0
l = len(name)
invname=""

while c < l:
    invname  = invname + name[l-c-1]
    c = c+1

print(invname)
