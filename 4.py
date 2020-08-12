import math
number = int(input())

while number > 0:
   for i in range(2, int(math.sqrt(number)) + 1): # обычно делитель не будет больше корня
       while (number % i == 0): # while, а не if
           print(i)
           number //= i # убираем множитель из числа
   if (number != 1): # но один делитель может быть больше корня
    print (number)
    break
while number < 0:
   for i in range(-2, 2, int(math.sqrt(+-number)) + 1): # обычно делитель не будет больше корня
       while (number % -i == 0): # while, а не if
           print(i)
           number //= -i # убираем множитель из числа
   if (number != 1): # но один делитель может быть больше корня
    for i in range(2, int(math.sqrt(-number)) + 1): # обычно делитель не будет больше корня
       while (number % i == 0): # while, а не if
           print(i)
           number //= i # убираем множитель из числа
    print (-number)
    break
