numb = float(input('son kiriting'))

# a = int(input('1-sonni kiriting'))
# b = int(input('2-sonni kiriting'))
# c = int(input('3-sonni kiriting'))

# masala-1

# if numb > 0:
#     numb += 1
#     print(numb)
# else:
#     print(numb)

# masala-2

# if numb > 0:
#     numb += 1
#     print(numb)
# else:
#     numb -= 2
#     print(numb)


# masala-3

# if numb > 0:
#     numb += 1
#     print(numb)
# elif numb < 0:
#     numb -= 2
#     print(numb)
# else:
#     print(10)

# masala-4

#
# def count_positive_numbers(numbers):
#     positive_count = 0
#     for number in numbers:
#         if number > 0:
#             positive_count += 1
#     return positive_count
#
# numbers = [a, b, c]
# positive_count = count_positive_numbers(numbers)
# print(positive_count)


# masala-5
#
# def count_all_numbers(numbers):
#     positive_count = 0
#     negative_count = 0
#     for number in numbers:
#         if number > 0:
#             positive_count += 1
#         if number < 0:
#             negative_count += 1
#
#     return positive_count, negative_count
#
#
# numbers = [a, b, c]
# positive_count, negative_count = count_all_numbers(numbers)
# print(f"musbat sonlar: {positive_count} ta, manfiy sonlar: {negative_count} ta")


# masala-6

# if a > b:
#     print(f"{a} va {b} sonlari orasida {a} soni katta")
# else:
#     print(f"{a} va {b} sonlari orasida {b} soni katta")


# masala-7

# if a > b:
#     print('1. ', b)
#     print('2. ', a)
# else:
#     print('1. ', a)
#     print('2. ', b)


# masala-8

# if a > b:
#     print('1. ', a)
#     print('2. ', b)
# else:
#     print('1. ', b)
#     print('2. ', a)


# masala-9

# if a > b:
#     a, b = b, a
#     print('1-son', b, '2-son', a)
# else:
#    a, b = a, b
# print('1-son', b, '2-son', a)

# masala-10

# if a != b:
#     count = a + b
#     print(count)
# else:
#     count = 0
#     print(count)


# masala-11

# if a != b:
#     count = max(a, b)
#     print(count)
# else:
#     count = 0
#     print(count)

# masala-12

# count = min(a, b, c)
#
# print(count)

# masala-13

# largest = max(a, b, c)
# smallest = min(a, b, c)
#
# average = (a + b + c - largest - smallest) / 1
#
# print(average)

# masala-14

# positive_count = 0
#
# if a > 0:
#     positive_count += 1
# if b > 0:
#     positive_count += 1
# if c > 0:
#     positive_count += 1
#
# print('musbat sonlar', positive_count, 'ta')


# masala-15

# positive_count = 0
# negative_count = 0
#
# if a > 0:
#     positive_count += 1
# else:
#     negative_count += 1
#
# if b > 0:
#     positive_count += 1
# else:
#     negative_count += 1
#
# if c > 0:
#     positive_count += 1
# else:
#     negative_count += 1
#
# print('musbat sonlar', positive_count, 'ta')
# print('manfiy sonlar', negative_count, 'ta')


# masala-16

# if a < b < c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c
#
# print(a, b, c)


# masala-17

# if a < b < c or a > b > c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c
#
# print(a, b, c)


# masala-18

# if a == b:
#     c = a + 1
#
# print(c)


# masala-19

# if numb == a == b:
#     c = numb + 1
#


# print(c)


# masala-20

# a_first = float(input("a nuqtaning x-koordinatasini kiriting: "))
# b_second = float(input("a nuqtaning y-koordinatasini kiriting: "))
# c_third = float(input("a nuqtaning z-koordinatasini kiriting: "))
#
# closest_point = (0, b_second, 0)
#
# distance = abs(a_first)
#
# print("a nuqtaga eng yaqin nuqta:", closest_point)
# print("A nuqta va eng yaqin nuqta orasidagi masofa:", distance)


# masala-29

# if numb > 0 and numb % 2 == 0:
#     print(f'{numb} musbat juft son')
# elif numb < 0 and numb % 2 == 0:
#     print(f'{numb} manfiy toq son')
# else:
#     print('toq son')



# homework-day-3

# masala-1
# k va n butun sonlari berilgan (n > 0). k sonini n marta chiqaruvchi dastur tuzing.

# k = int(input('k sonni kiriting: '))
# n = int(input('n sonni kiriting: '))
#
# for i in range(n):
#     if i > 0:
#         print(k)


# masala-2
# a va b butun sonlari berilgan (a < b). a va b sonlari orasidagi barcha butun sonlarni (a va b ni ham) chiqaruvchi va ciqarilgan sonlar sonini chiqaruvchi dastur tuzing

# a = int(input('a sonini kiriting: '))
# b = int(input('b sonini kiriting: '))


# for i in range(a, b + 1):
#         print(i)
#
# print(f'a va b orasidagi sonlar soni: {b - a}')



# masala-3
# a va b butun sonlari berilgan (a<b). a va b butn sonalri orasidagi barcha butun sonlarni  (a va b dan tashqari) kamayish tartibida chiqaring

# for i in range(b-1, a, -1):
#     print(i)
#
# print(f'a va b orasidagi sonlar soni: {b - a}')


# masala-4
# 1 kg konfetning narxi berilgan (haqiqiy son). 1, 2 ..., 10 kg konfetni narxini chiqaring

# for i in range(1, 11):
    # print(f"{i} kg konfetning narxi {i * numb} so'm")


# masala-5
# 1 kg konfetning narxi berilgan(haqiqiy son). 0.1, 0.2, ..., 0.9,  1kg konfetning narxini chiqaring

# for i in range(1, 11):
#     print(f"{i / 10} kg konfetning narxi {i / 10 * numb}")