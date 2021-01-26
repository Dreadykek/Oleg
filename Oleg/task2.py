def main():
	#Инициализируем список из предыдушего задания
	spicok = ['Buick','Cadillac','Chevrolet','Chrysler','Dodge','GMC','Hummer']
	#Выводим список марок
	print(spicok)
	#Выведем первый, третий, четвертый и последний элементы
	print(spicok[0])
	print(spicok[2])
	print(spicok[3])
	print(spicok[len(spicok) - 1])
	#Разобьём список на 3 части, как сказанно в задании
	list1 = spicok[:3]
	list2 = spicok[3]
	list3 = spicok[4:]
	#Создаем список который состоит из подсписков главного списка
	mnogo_spisok = [list1, list2, list3]
	#Выведем этот список в консоль
	print(mnogo_spisok)
	#Меняем первый и последний элементы
	temp = mnogo_spisok[2]
	mnogo_spisok[2] = mnogo_spisok[0]
	mnogo_spisok[0] = temp
	#Выводим список после изминений
	print(mnogo_spisok)
	#Добавляеи новый элемент
	mnogo_spisok.append("new_element")
	#Выводим список после изминений
	print(mnogo_spisok)
	#Добавляем новый элемент в подсписок списка
	mnogo_spisok[0].append("new_element")
	#Выводим список после изминений
	print(mnogo_spisok)
	#Убираем все элементы кроме первого
	temp = mnogo_spisok[0]
	mnogo_spisok.clear()
	mnogo_spisok.append(temp)
	#Выводим список после изминений
	print(mnogo_spisok)

if __name__ == "__main__":
	main()