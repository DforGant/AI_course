num = input('Number: ')
List = []


# Создание списка с игнорированием STR
for i in num:
	try:
		int_check = int(i)
	except ValueError:
		continue
	else:
		List.append(i)

# Определение последней и предпоследней цифры
last_Symbol = int(List[-1])

try:	#Отлов ошибки отсутствующей последней цифры
	penult_Symbol = int(List[-2])
except IndexError:
	penult_Symbol = 0


# Решение об окончании
if penult_Symbol == 1:
	suffix = 'рублей'
elif last_Symbol < 5 and last_Symbol > 0:
	if last_Symbol == 1:
		suffix = 'рубль'
	else:
		suffix = 'рубля'
else:
	suffix = 'рублей'


print(num, suffix)
