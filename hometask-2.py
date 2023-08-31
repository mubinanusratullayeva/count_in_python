# numb = int(input('son kiriting'))

a = int(input('1-sonni kiriting'))
b = int(input('2-sonni kiriting'))
c = int(input('3-sonni kiriting'))

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