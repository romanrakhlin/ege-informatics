# В текстовом файле k8-4.txt находится цепочка из символов,
# в которую могут входить заглавные буквы латинского алфавита A…Z и десятичные цифры.
# Найдите длину самой длинной подцепочки, состоящей из одинаковых символов.
# Если в файл несколько цепочек одинаковой длины, нужно взять первую из них.
# Выведите сначала символ, из которого строится эта подцепочка, а затем через пробел – длину этой подцепочки.

file = open("24data/k8data/k8-4.txt", "r")
data = file.read()

# Обясняб что к чему.
# Вообще есть несколько решений данной вариции 24ого задания.
# Она ксати довольно часто выпадает на пробниках и есть подозрния что она и будет в ЕГЭ.
# Лично я раньше решал ее так - создавал словарь и аализируя все
# символы находил для каждого максимальную длиннну а после выбирал максимальную.
# Не знаю почему я это делад, ведь это намного сложнее закодить.
# Но сейчас, да да за два дня д экзамена, я придумал вариацию намного круче, кроче и быстрее!

# Обьясняю алгоритм. Мы задаем уже знакомые нам переменные count и count_max,
# но так же создадим переменную letter. Суть такая - пробегаться по всей строке. Не с начала а со второго символа.
# И проверять, если текущий символ совпадает с предыдущим то count += 1 и
# если и после этого проверяем, обогнал ли наш count максималку count_max,
# если да, то поздравляю, перед нами новый count_max.
# НО и не забудем указать текущую буквы, в которой мы установлии рекорд по длинне, это как раз переменная letter.
# Когда мы наконец дошли то го момента когда символ отличается, то снова ставим count = 1.

count = 1

count_max = 1
letter = ""

for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        count += 1
        if count > count_max:
            count_max = count
            letter = data[i]
    else:
        count = 1

print(letter, count_max)

# Ответ - W 4