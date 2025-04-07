logs = []

def liitumine(a,b):
    logs.append('liitumine')
    if isinstance (a, str) or isinstance (b, str):
        print ("vale andmed") 
        return("")
    return a + b

def minus(a,b):
    logs.append('minus')
    if isinstance (a, str) or isinstance (b, str):
        print ("vale andmed") 
        return("")
    return a - b

def delit(a,b):
    logs.append('delit')
    if isinstance (a, str) or isinstance (b, str):
        print ("vale andmed") 
        return("")
    if b == 0:
        print ("NELZA DELIT NA NOLL!!!")
        return("") 
    return a / b

def umnoz(a,b):
    logs.append('umnoz')
    if isinstance (a, str) or isinstance (b, str):
        print ("vale andmed") 
        return("")
    return a * b
def logsKuvamine(logs):
    for elem in logs:
        if elem == "liitumine":
            korr += 1
        elif elem == "minus":
            jag += 1
        elif elem == "delit":
            liit += 1
        else:
            lahut += 1
        return[jag,korr,liit,lahut]


print("insert 2 numbers")
a = int(input())
b = int(input())
print("Chose cho delat (insert number)")
print("1 - slozenie")
print("2 - minus")
print("3 - delenie")
print("4 - umnozenie")
valik = int(input())
if valik == 1:
    print(liitumine(a,b))
elif valik == 2:
    print(minus(a,b))
elif valik == 3:
    print(delit(a,b))
elif valik == 4:
    print(umnoz(a,b))
else:
     print("bebebe")




