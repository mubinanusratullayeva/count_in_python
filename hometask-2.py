# numb = float(input('son kiriting'))

a = int(input('1-sonni kiriting'))
b = int(input('2-sonni kiriting'))
# c = int(input('3-sonni kiriting'))

buzz = 0

n = a

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


# masala-6
# 1 kg konfetning narxi berilgan (haqiqiy son). 1.2, 1.4, ..., 2 kg konfetni narxini chiqaring

# for i in range(12, 21, 2):
     # print(f"{i / 10} kg konfetning narxi {i / 10 * numb}")


# masala-7
# a va b butun sonalri berilgan (a<b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaring

# bar = 0
#
# for i in range(a, b + 1):
#      bar += i
# print(bar)


# masala-8
# a va b butun sonlari berilgan (a<b). a va b gacha bo'lgan barcha butun sonlarning ko'qaytmasini chiqaring

# bar = 1
#
# for i in range(a, b):
#      bar *= i
# print(bar)


# masala-9
# a va b butun sonalri berilgan (a < b). a dan b gacha bo'lgan barcha butun sonalar kvadratlarining yig'indisini chiqaring
#
# bar = 0
#
# for i in range(a, b + 1):
#      buzz = i ** 2
#      bar += buzz
# print(bar)


# masala-10
# n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblng
# S = 1 + 1/2 + 1/3 + ... + 1/n

# s = 0
#
# for i in range(1, n + 1):
#      s += 1/i
# print(s)


# masala-11
# n butun soni berilgan (n>0). Quyidagi yig'indini hisoblang
# S = n ** 2 + (n+1) ** 2 + ... (2 * n) ** 2

# s = 0
#
# for i in range(n, 2*n+1):
#     s += i**2
# print


# masala-12
# n butun soni berilgan (n>0). Quyidagi ko'paytmani hisoblang'
# S = 1.1 * 1.2 * 1.3 ... (n ta ko'paytuvchi)

# s = 1
#
# for i in range(1, n+1):
#     s *= (1 + i/10)
# print(s)


# masala-13
# n butun son berilgan (n > 0). Qiyidagi yig'indini hisobalng'
# S = 1.1 - 1.2 + 1.3 - ...
# (n ta qo'shubchi, ishoralar almashib keladi. Shart operatoridan foydalanmang)

# s = 0
#
# for i in range(1, n+1):
#     if i < 0:
#         j = i * (-1)
#         s += (1+j/10 - 1+j/10)
#     else:
#         s += (1+i/10 - 1+i/10)
#
# print(s)


# masala-14
# n butun soni berilgan (n > 0). shu sonning kvadratini shu formuladan foydalanib yeching
# n **2 = 1 + 3 + 5 + ... + (2*n - 1)
# har bir qo'shiluvchidan keyin natijani chiqarib boring. Natijada ekranda 1 dan n gacha bo'lgan sonlar kvadrati chiqariladi

# s = 0
#
# for i in range(1, n+1):
#     s += (2*i - 1)
#     print(f"Qo'shgandan keyin {2*i - 1}, {s} bo'ladi")
#
# print(f"yig'indi {s}")


# homework-

# 1-masala
# A va B butun musbat sonlari berilgan (A > B). A uzunlikdagi kesmada maksimal darajada B kesma joylashtirilgan. A kesmaning bo'sh qismini aniqlovchi dastur tuzung. Ko'paytirish va bo'lish ammallarini ishlatmang.

# while a > b:
#     a = a - b
#     buzz += 1
# print(a, buzz)


# 2-masala
# A va B butun musbat sonlari berilgan (A > B).A uzunlikdagi kesmada B kesmadan nechta joylashtirish mumkin. Ko'paytirish va bo'lish ammallarini ishlatmang.

# count = 0
#
# while a >= b:
#     a -= b
#     count += 1
#
# print(f"uzunligi {n} bo'lgan kesmada {b} uzunlikdagi keamadan {count} ta joylashtirish mumkin ")



# 3-masala
# N va K butun musbat sonlari berilgan. Faqat ayirish va qo'shish amallarini ishlatib N sonini K soniga bo'lgandagi qoldiq va butun qismini aniqlang

# o = a
# while o >= b:
#     o -= b
#
# print(f"""javob = {a // b},
#  qoldiq {o}""")

# 4-masala
# n butun soni berilgan (n>0). Agar n soni 3 ning darajasi bo'lsa, "3 ning darajasi", aks holda "3-ning darajasi emas" degan natijani chiqaring. Qoldiqli bo'lish va bo'lish amallarini ishlatmang

# while n % 3 == 0:
#     n /= 3
#
# if n == 1:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")

# 5-masala
# 2 sonining qandaydir darajasini bildiruvchi n butun soni berilgan (n>0) n = 2 ** k. k ni aniqlovchi dastur tuzing

# k = 0
#
# while n > 1:
#     n /= 2
#     k += 1
#
# print(f"k = {k}")

# 6-masala
# n natural soni berilgan (n > 0). Quyidagi ifodani hisoblovchi dastur tuzing
# n!!=n*(n-2)*(n-4)...
# Agar n juft bo'lsa oxirgi ko'paytuvchi 2, top bo'lsa 1 bo'ladi

# r = 1
# while n > 0:
#     r *= n
#     n -= 2
#
# print(f"n!! = {r}")

# 7-masala
# n natural soni berilgan (n > 0). Kvadrati n dan katta bo'ladigan eng kichik butun k sonini (k**2 > n) aniqlovchi dastur tuzing. Ildizdan chiqarivchi funksiyadan foydalanmang

# k = 1
# while k ** 2 <= n:
#     k += 1
#
# print(k)


# 8-masala
# n natural soni berilgan (n > 0). Kvadrati n dan katta bo'lmagan eng katta butun k sonini (k**2 <= n) aniqlovchi dastur tuzing. Ildizdan chiqaruvchi funksiyadan foydalanmang

# k = 1
# while k ** 2 <= n:
#     k += 1
#
# print(k-1)

# 9-masala
# n natural soni berilgan (n > 1). 3 **k > n sharti qanoatlantiruvchi eng kichik butun k sonini aniqlang

# k = n + 1
# while k <= n:
#     k += 1
#
# print(k)


# 10-masala
# n natural soni berilgan (n > 1). n**k <= n shartini qanoatlantiruvchi eng katta butun k sonini aniqlang

# k = 0
# while n ** k <= n:
#     k += 1
#
# print(k - 1)