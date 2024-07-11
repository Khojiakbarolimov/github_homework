class negativenumber(Exception):
    pass
def sumdigits(number):
    return sum(int(digit) for digit in str(number))
dct = {}
numbers = []
n = int(input("Elementlar soni: "))
try:
    for i in range(n):
        temp = int(input("Musbat son kiriting: "))
        if temp < 0:
            raise negativenumber
        numbers.append(temp)
except:
    print("Faqat musbat son qabul qilinadi!!!")
numbers = sorted(numbers, key=sumdigits)
print(numbers)