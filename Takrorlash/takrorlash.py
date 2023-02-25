# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}
# for key, value in python_words.items():
#     print(f"{key.title()} - {value.capitalize()}")
c = { 'uzbekistan': 'tashkent', 'kazakhistan': 'astana', 'china': 'beijing', 'ozorbayjon': 'baku'  }
# for countri in c.keys():
#     print(countri.upper())
# for city in c.values():
#     print(city.upper()
d = input('Davlatni kiriting \n>>>').lower()
if d in c.keys():
    print(c[d].title())
else:
    javob = c.get(d, 'Bunday ma`lumot kiritilmagan')
    print(javob)
    
    
    
    

    
    
    
    