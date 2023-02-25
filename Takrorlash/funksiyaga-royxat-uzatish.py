# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:32:58 2023

@author: Bahodir
"""

def bahola(names):
    rates = { } 
    while names:
        name = names.pop()
        baho = int(input(f"{name.title()}ning bahosini kiriting \n>>>"))
        rates[name] = baho
    return rates

students = [ ]
while True:
    student = input("Talabnining ismini kiriting: ")
    students.append(student)
    request = input("Yana talaba qo`shilsinmi(yes or no): ")
    if request == 'no':
        break
print("Talabalar qo`shildi!")
tblist = bahola(students)
print(tblist)








