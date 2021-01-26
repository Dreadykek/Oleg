def main():
	#Запрашиваем строку у пользователя
	userString = input("Введите строку: ")
	userString += " "
	#Список для слов
	words = []
	#Спомогательная пересенная 
	word=""
	#Цикл для формирования списка 
	for item in userString:
		#Если пробел то добовляем слово в список
		if(item !=" "):
			word+=item
		else:
			if word != "":
				words.append(word)
			word=""
			continue

	print(words)
	#переменная, которая хронит сколько различных букв в минимальном слове 
	minLetterCount = len(userString)
	#переменная хранящая ответ
	answer = userString
	#цикл который считает количество букв в слове
	for word in words:
		#создаем список 
		letterList = []
		for letter in word:
			#добовляем только уникальные буквы
			if (not letter in letterList):
				letterList.append(letter)
		if len(letterList)<minLetterCount:
			answer = word
			minLetterCount = len(letterList)

	print("Число с наименьшим количеством букв: ", answer)

if __name__ == "__main__":
	main()