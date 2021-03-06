# Логическая функция F задаётся выражением 
# ((x → y) ∨ (y ≡ w)) ∧ ((x ∨ z) ≡ w). 
# На рисунке приведён частично заполненный фрагмент таблицы 
# истинности функции F, содержащий неповторяющиеся строки. 
# Определите, какому столбцу таблицы истинности функции F 
# соответствует каждая из переменных x, y, z, w.

# https://inf-ege.sdamgia.ru/problem?id=28677

# Обозначения:
# not() - отрицание
# and - И /\
# or - ИЛИ \/

print("X Y Z W = F") # Выведем для удобства

# Итерируем значения x, y, z, w
# со значениями от 0 до 1
for x in 0, 1:
	for y in 0, 1:
		for z in 0, 1:
			for w in 0, 1:
				# Зададим само выражения, используя обозначения выше
				F = ((not(x) or y) or (y == w)) and ((x or z) == w)

				# Сделаем чтобы F был не True/False, а 0/1
				F = int(F)

				# В этой задаче нам нужно знать когда F == 1
				# Если F равен 1, то
				if F == 1:
					print(x, y, z, w, "=", F) # Выводим все наши значения с F

# И после вывода мы не получим какой-то определенный ответ к задаче,
# Мы получим лишь таблицу истинности. 
# И уже она нам поможет найти решение к задаче.
# Мы просто должны анализовать нашу таблицу и таблицу в условии,
# менять местами различные моменты и найти ответ.
# Но главное это ПРОВЕРКА!!! 
# Когда найдем ответ, нужно расставить элементы таблицы так же как в задании
# И строки должны совпадать.