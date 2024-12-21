import random
def shifr():
    rnd = list(range(3, 21))
    shifr = random.choice(rnd)
    return shifr
def code():
    doorpass = {}
    doorpass.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746,
                     11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968,
                     15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089,
                     18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
                     20: 13141911923282183731746416515614713812911})
    code = doorpass.get(n)
    return code
n = shifr()
print('Ключ:', n)
FirstNum = list(range(1, n))
SecondNum = list(range(1, n))
SumNum = []
result = ''
for i in FirstNum:
    for j in SecondNum:
        FN = i
        SN = j
        if FN >= SN:
            continue
        else:
            f = n % (FN + SN)
            if f == 0:
                SumNum.append([FN, SN])
                result = result + str(FN) + str(SN)
print('Пары решений', *SumNum)
print('Введите во вторую вставку код:', result)
if int(result) == code():
    print('Поздравляем!!! Вы выбрались из этой ловушки!!! Мы не надеялись на вас, но у вас получилось!!!')