def main():
	#Запрашиваем строку у пользователя
	userString = input("Введите строку: ")
	executionLetter = input("Введите букву, которую не хотите видеть в слове: ")

	#Создаем переменную в которой будет храниться ответ
	answer=""

	#Изменяем строку в соответсвии с заднием
	for letter in userString:
		if letter != executionLetter:
			answer += letter + letter

	print("Измененная строка: ", answer)

if __name__ == "__main__":
	main()