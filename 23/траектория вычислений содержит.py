# (№ 3088) Исполнитель Июнь15 преобразует число на экране. 
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Прибавить 2
# Программа для исполнителя Июнь15 – это последовательность команд. 
# Сколько существует программ, для которых 
# при исходном числе 5 результатом является 
# число 15 и при этом траектория вычислений содержит число 10?

# Рекурсионная функция, которая перебираает все
# варианты и если они в конечном итоге приводят к ответу, считает их.
# Мы задаем два числа: начальное и конеченое.
def make(x, y):
	if x == y:
		return 1
	elif x > y:
		return 0
	elif x < y:
		# Складываем все количества команд.
		return make(x + 1, y) + make(x + 2, y)

# Переберем от начального, до нужного нам.
# И от нужного нам до результата.
# После этого все перемножим, так как это логическое И.
n = make(5, 10) * make(10, 15)
print(n)