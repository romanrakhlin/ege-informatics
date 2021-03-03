# Дана программа для исполнителя Редактор:
#
# НАЧАЛО
#   ПОКА нашлось (56) ИЛИ нашлось (1111)
#     заменить (56, 1)
#     заменить (1111, 1)
#   КОНЕЦ ПОКА
# КОНЕЦ
#
# Какая строка получится в результате применения приведённой
# ниже программы к строке, состоящей из 102 строк 561 (561561561…561)?

s = "561" * 102 # Создадим последовательность из цифр 561

# Пока 56 или 1111 есть в строке, то
while "56" in s or "1111" in s:
	s = s.replace("56", "1", 1) # Заменяем 56 на 1
	s = s.replace("1111", "1", 1) # Заменяем 1111 на 1

print(s) # 111

# В Python есть мега удобная функция replace()
# Она принимает в себя 3 значения:
# 1 - Часть, которую нужно заменить
# 2 - Часть, которою нужно поставить вместо
# 3 - Сколько раз необходимо сделать замену. (Если оставить его пустым, он будет менять все что найдет).