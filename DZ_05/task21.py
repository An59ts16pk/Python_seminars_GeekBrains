# Задача 1.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]  
# =============================================================================

sp = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА', 'показабвение']

res = list(filter(lambda x: 'АБВ' not in x and 'абв' not in x, sp))
print(res)