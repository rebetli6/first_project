def print_employee_name():
    print("Hello Functions")

def osszead(adando):
    sum=0
    for c in adando:
        sum=sum+c
    return sum

def space_count(text):
    sum=0
    for c in text:
        if c == " ":
            sum= sum +1
    return sum

def atlag(adando):
    sum=0
    for c in adando:
        sum=sum+c
    sum = sum/ len(adando)
    return sum

print_employee_name()

adando= [2, 4, 6]

s=osszead(adando)
print(s)

text="kk aaa zzzzzzzzz gggg"
s=space_count(text)
print(s)

s=atlag(adando)
print(s)

