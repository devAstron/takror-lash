# # -*- coding: utf-8 -*-
# """
# Created on Wed Feb 22 20:33:49 2023

# @author: Bahodir
# """

# # Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email
# #   manzili va telefon raqamini qabul
# #   qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu 
# #   yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, 
# #   tel.raqam, el.manzil)
# def user_data_saver(name, surname, birth_date, birth_place, mail = '', phone_number = ''):
#     user_info = {
#                 'ism': name,
#                 'familya': surname,
#                 't_sana': birth_date,
#                 't_joy': birth_place,
#                 'pochta': mail,
#                 'tnomer': phone_number
#                 }
#     return  user_info  
# user1 = [ ]
# ism = input('Ismingiz nima? \n>>>')
# familya = input("Familyangiz nima \n>>>")
# t_sana = input("Tug`ilgan sanangiz\n>>>")
# t_joy = input("Tug`ilgan joyingiz \n>>>")
# pochta = input("Pochta manzilingiz\n>>>")
# tnomer = input("Telefon raqamingiz\n>>>")
# user1.append(user_data_saver(ism, familya, t_sana, t_joy), pochta, tnomer)
# print(f" Foydalanuvchi ma`lumoti: {user1['ism'].title()} {user1['familya']} {user1['tnomer']}")
# # print(f"{user1['ism'].title()} {user1['familya'].title()} {user1['tnomer']}")

# # def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
# #     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
# #     mijoz = {'ism':ism,
# #              'familiya':familiya,
# #              'tyil':tyil,
# #              'yoshi':2020-tyil,
# #              'tjoy':tjoy,
# #              'email':email,
# #              'telefon':tel}
# #     return mijoz

# # print("Mijoz haqida ma'lumotlarni kiriting.")
# # mijozlar =[]
# # while True:
# #     ism = input("Ismi: ")
# #     familiya = input("Familiyasi: ")
# #     tyil = int(input("Tug'ilgan yili: "))
# #     tjoy = input("Tug'ilgan joyi: ")
# #     email = input("Email: ")
# #     telefon = input("Telefon raqami: ")
# #     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
# #     javob = input("Davom etasizmi? (ha/yo'q)")
# #     if javob!='ha':
# #         break

# # print("Mijozlar:")
# # for mijoz in mijozlar:
# #     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
# #           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")   
# def list_range(min, max, step = 1):
#     numbers = [ ]
#     while min < max:
#         numbers.append(min)
#         if step != 1:
#             min += step
#         else: 
#             min += 1
#     return numbers

# print("Salom dasturimiz [ list_range()] funksiyasi yordamida kiritilgan a b oraliqdagi sonlar ro`yxatini shakllantirib beradi 1-sonni kiritin:")
# a = input(">>>")
# b = input('2-sonni kirting \n>>>')
# a , b = int(a), int(b)
# request = input(f"{a} va {b} oraliqdagi ro`yxat uchun qadamni ham kirtasizmi? (yes or no) ")
# if request != 'yes':
#     newlist = list_range(a, b)
#     print(newlist)
# else: 
#     step = int(input("Qadamni kiriting \n>>>"))
#     newlist = list_range(a, b, step)
#     print(newlist)

  
    
    
    
    
    
    
    
    
    
    
    
    
    
 