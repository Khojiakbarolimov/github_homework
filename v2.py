n= int(input("Elementlar soni: "))
dct = {}
voted, notvoted = 0, 0
for i in range(n):
    key = input("Key = ")
    value = int(input("value = "))
    dct.update({key:value})
    if value > 0:
        voted += 1
    else:
        notvoted += 1
if voted > notvoted:
    print(1)
    for key, value in dct:
        if value > 0:
            print(key)
elif notvoted > voted:
    print(0)
    for key, value in dct:
        if value == 0:
            print(key)
else:
    print(1)
    for key, value in dct:
        if value == 1:
            print(key)
    print(0)
    for key, value in dct:
        if value == 0:
            print(value)