# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:51:19 2023

@author: Bahodir
"""
# import math
# print("Salom bu dastur siz kiritgan gradusga mos keluvchi sin cos tg a ctgning qiymatnini chiqarib beradi. Burchakni gradus o`lchovida kiriting ")
# print("Dasturni to`xtatish uchun exit deb yozing")
# while True:
#     x = int(input("\n>>>"))
#     if x != 'exit':
#         print(f"{x} gradusda sinusning qiymati {round(math.sin(math.radians(x)),1)}" )
#         print(f"{x} gradusda sinusning qiymati {round(math.cos(math.radians(x)),1)}" )
      
#     else:
#         break
# print('Dastur to`xtadi')
# q = "Sonni darajasini hisoblaymiz: "
# q += "(dasturni  to`xtatish uchun 'exit' deb yozing)"
# q += " Sonni kiriting\n>>>"
# son = ''
# daraja= ''
# while son != 'exit':
#     son = input(q)
#     if son != 'exit' :
#         daraja = input(f"{son} ning nechanchi darajasini hisoblaymiz\n>>>")
#         print(f"{son} ning {daraja}-darajasi {int(son)**int(daraja)} bo`ladi")
# print('Dastur tugadi ')
# q = "Sonni darajasini hisoblaymiz: "
# q += "(dasturni  to`xtatish uchun 'exit' deb yozing)"
# q += " Sonni kiriting\n>>>"
# son = ''
# daraja= ''
# target = True
# while target:
#     son = input(q)
#     if son == 'exit' :
#         target = False
    
#     else:
#         daraja = input(f"{son} ning nechanchi darajasini hisoblaymiz\n>>>")
#         print(f"{son} ning {daraja}-darajasi {float(son)**float(daraja)} bo`ladi")
        
# print('Dastur tugadi ')
q = "Sonni darajasini hisoblaymiz: "
q += "(dasturni  to`xtatish uchun 'exit' deb yozing)"
q += " Sonni kiriting\n>>>"
son = ''
daraja= ''

while True:
    son = input(q)
    if son == 'exit' :
        break
    
    else:
        daraja = input(f"{son} ning nechanchi darajasini hisoblaymiz\n>>>")
        print(f"{son} ning {daraja}-darajasi {float(son)**float(daraja)} bo`ladi")
        
print('Dastur tugadi ')




















    
    
  

     