with open("hodimlar.txt") as file:
    data = file.read()
    data = data.split("\n")
bolimlar = {
    "1-bo'lim" : 0, 
    "2-bo'lim" : 0, 
    "3-bo'lim" : 0
}
for i in range(len(data)):
    data[i] = data[i].split()
    data[i][2], data[i][3] = int(data[i][2]), int(data[i][3])
    if data[i][3] > 0:
        bolimlar[data[i][-1]] += 1
engkop = max(bolimlar, key=bolimlar.get)
for i, val in bolimlar.items():
    if val == bolimlar[engkop]:
        print(i)