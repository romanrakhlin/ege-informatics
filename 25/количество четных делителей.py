# Напишите программу, которая ищет среди целых чисел, 
# принадлежащих числовому отрезку [95632; 95700], 
# числа, имеющие ровно шесть различных чётных натуральных делителей. 
# Для каждого найденного числа запишите 
# эти шесть делителей в шесть соседних столбцов 
# на экране с новой строки. 
# Делители в строке должны следовать в порядке возрастания.

# Зададим массив, в который
# будем сохранять ответы
arr = []

# Итерируем через числа от 95632 до 95700
for i in range(95632, 95701):
	# Зададим временные переменные
	count = 0 # Для счета количества делителей
	delitels = [] # Для хранения подходящих делителей

	# Итерируем через числа от 1 до i
	for j in range(1, i+1):
		# Если текущий делитель четный:
		if j % 2 == 0:
			# Если i делится на j:
			if i % j == 0:
				count += 1 # Плюсуем делитель
				delitels.append(j) # Добавляем его в массив

	# Если делителей ровно 6, то:
	if count == 6:
		# Добавляем массив с шестью делителями в массив с ответами
		arr.append(delitels)

# Выводим ответ
print(arr)
# Вывод:
# [[2, 10, 50, 3826, 19130, 95650], 
# [2, 26, 338, 566, 7358, 95654], 
# [2, 4, 8, 23918, 47836, 95672]]

