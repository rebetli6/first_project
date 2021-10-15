def print_employee_name():
    print("Hello Functions")

def osszead(a,b):

    return a+b

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