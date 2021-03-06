# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=19&cat154=on&cat163=on
# Код вы уже знаете! Этог разбор вариации когда сумма камней в куче ограничена от и до.
# В данном примере: если в куче больше 50 и меньше 70 камней, то побеждает игрок, сделавший ход последним.
# Иначе, побеждает игрок номер два.

results = {}

def game(S):
    if S in results:
        return results[S]

    # Я добавил тут условие (ограничение) с помощью and.
    if S >= win and S <= 70:
        results[S] = 0
        return 0
    # Ходы, которые ведут на больше 70 ограничиваются.
    # Почему я задал именно 1. Нуууу на самом деле я тестил и с -1 и другими,
    # и только при этом получается правильный ответ ЛОЛ.
    # Но башка чет не варит и сложно разобраться в этой большой рекурсии.
    # Я еле еле допер что к чему.
    # Ну смотрите, например челик стоит на 49, у менго понятное дело ходы на 50 (победа - 0)
    # и еще какаято большая хрень но не важно, важно что есть 0. И это ознаечает что
    # срабатывает условие что хоть один ход ведет на 0, поэтому устанавливает 1.
    # Но вот когда челик стоит на 48, то он может походить либо на 49, либо там на вообще 80 с чем-то.
    # То есть ведет на 1 и еще 1. То есть 48 распознается как проигрышная херня.
    # Поэтому к 48 присваивается отрицательное число. Именно для этого и нужно присваивть 1 к числам больше 70.
    elif S > 70:
        results[S] = 1
        return 1
    else:
        next_move = [game(S + 1), game(S * 2)]

        if 0 in next_move:
            results[S] = 1
            return 1
        elif min(next_move) > 0:
            results[S] = max(next_move) * -1
            return max(next_move) * -1
        else:
            arr = []

            for i in next_move:
                if i < 0:
                    arr.append(i)

            results[S] = (max(arr) * -1) + 1
            return (max(arr) * -1) + 1

win = 50

for S in range(80, 0, -1):
    n = game(S)
    print(S, n)

# 19 - 13
# 20 - 12
# 21 - 22