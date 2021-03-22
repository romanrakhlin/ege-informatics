# Задача номер 1 из сборника К. Полякова
# Код взят и частично изменен: https://www.youtube.com/watch?v=tBHU9W167yA


# Тк это рекурсия, то прога свова и свона перебирает уже
# до этого найденные значения. Изза чего работает довольно медленно.
# Чтобы это пофиксить, мы будем сохранять уже найденные значения в словарь.
results = {}

# Функция будет принимать на вход количество камней в первой куче (x)
# И количество камней во второй куче (S)
def game(x, S):
	# Проверяем, искали ли мы уже ранне эти x и S.
	# Если искали, то просто возвращаем результат работы программы для них.
	if (x, S) in results:
		return results[(x, S)]
	# Если в сумме в двух кучах камей достаточно для победы,
	# то возвращаем 0 (уже победная позиция).
	if x + S >= win:
		# Сохраним в словарь результат работы проги.
		results[(x, S)] = 0

		# Вернем 0
		return 0
	# Если же в двух кучах в сумме не хватает камней то победы, то
	else:
		# Так же зададим массив, в котором будут храниться
		# все 4 возможных исхода.
		next_move = [game(x + 1, S), game(x * 2, S), game(x, S + 1), game(x, S * 2)]
		
		# Если текущая позиция ведет хоть на один 0, то
		# она выигрышная за 1 ход. Возвращаем 1.
		if 0 in next_move:
			# Сохраним в словарь результат работы проги.
			results[(x, S)] = 1

			# Вернем 0
			return 1
		# Если из текущей позиции можно походить только на
		# положительную, то это значит, что она проигрышная,
		# тк ведет соперника на победу.
		# Но тк мы хотим оттягивать поражение как можно дольше,
		# то мы походим на проигрыш за самое долгое количество ходов.
		# Поэтому выберем максимальное и умножим на -1.
		elif min(next_move) > 0:
			return max(next_move) * -1
		# Если же в массиве есть хоть одно отрицательное число,
		# то значит, что эта позиция выигрышная.
		# И тут мы уже хотим выиграть как можно быстрее,
		# поэтому выберем выигрыш за самое маленькое количество шагов.
		# Так как мы рассматриваем отрицательные числа, мы берем наибольше ез них,
		# далее делаем его положительным и прибавляем 1.
		else:
			# Создадим временный массив. В который будем складывать
			# отрицательные числа.
			arr = []

			# Перебираем все числа из массива next_move.
			for i in next_move:
				# Если число отрицательное, то
				if i < 0:
					# Добавляем его во временный массив.
					arr.append(i)

			# Сохраним в словарь результат работы проги.
			results[(x, S)] = (-1 * max(arr)) + 1

			# Возвращаем наибольшее из отрицательных чисел
			# и делаем его положительным, после чего, добавляем 1
			return (-1 * max(arr)) + 1

# Задодим число, при котором наступает победа.
win = 75

# Перебираем числа с конца (тк так быстрее).
for S in range(win, 0, -1):
	n = game(8, S)

	# Выводим получившуюся таблицу.
	print(S, n)

