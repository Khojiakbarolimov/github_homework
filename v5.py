import os

naqsh = []
n = int(input("Kvadratlar soni: "))
colours = ["Red", "Blue", "Yellow", "Green"]
for i in range(n):
    os.system('cls')
    print(f"{i+1}-kvadrat bo'yash uchun kerak rang tanlang: ")
    inx = int(input("#1 Red\n#2 Blue\n#3 Yellow\n#4 Green\n"))-1
    naqsh.append(colours[inx])
count = 2
for i in range(1, n):
    if naqsh[i-1] != naqsh[i]:
        count += 1
    count += 2
os.system('cls')
print(f"naqsh({naqsh})")
print(count)