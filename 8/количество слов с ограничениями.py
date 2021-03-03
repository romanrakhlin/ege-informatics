# Сколько слов длины 5, начинающихся с гласной буквы, 
# можно составить из букв Е, Г, Э? 
# Каждая буква может входить в слово несколько раз. 
# Слова не обязательно должны быть осмысленными словами 
# русского языка.

s = "егэ"
result = 0
lettrs = ["е", "э"] # глассные буквы

# количество циклов, это длина слова
# нам нужно 5-буквенные слова, поэтому циклов 5
for a in s:
	for b in s:
		for c in s:
			for d in s:
				for e in s:
					word = a + b + c + d + e # сложим все буквы в слово и получим одну из возможных вариаций
					if word[0] in lettrs: # если первая буква совпадает хоть с одной гласной, то
						result += 1 # прибавляем эту вариацию к ответу

print(result)

