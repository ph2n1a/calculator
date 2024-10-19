print("   калькулятор \n ✣╼╼╼╼╼╼╼╼╼╼╼✣ \nвведите пример который нужно решить, например x * y \n x -- первое число \n y -- второе число  \n ═────═⌘═────═  \nможно использовать згаки +, -, *, /, % \n + -- сложение \n - -- вычетание \n * -- умножение \n / -- деление \n % -- остаток от деления \n ═────═⌘═────═ \nважно -- вводить пример с пробелами как в примере \n ═────═⌘═────═ ")

while True:
	txt = input("введите пример: ")
	
	if txt == "exit":
		exit()

	list = txt.split(" ")
	
	if len(list) == 3:
	
		if txt.count(" ") == 2:
		
			if list[0].isdigit() and list[2].isdigit() == 		True:
	
				if list[1] == "+" or list[1] == "-" or list[1] == "*" or list[1] == "/" or list[1] == "%":
					if list[1] == "+":
						print("\nответ: ", int(list[0]) + int(list[2]))
					if list[1] == "-":
						print("\nответ: ", int(list[0]) - int(list[2]))
					if list[1] == "*":
						print("\nответ: ", int(list[0]) * int(list[2]))
					if list[1] == "/":
						print("\nответ: ", int(list[0]) / int(list[2]))
					if list[1] == "%":
						print("\nответ: ", int(list[0]) % int(list[2]))
		
				else:
					print("\nошибка: неправелиный знак")
		
			else:
				print("\nошибка: в примере не должно быть букв")
		
		else:
				print("\nошибка: пример без пробелов, добавте пробелы как в примере")
	
	else:
		print("ошибка: неправильный синтаксис")
		
	print(' \n ═────═⌘═────═ \nчтобы выйти напишите "exit" ')
