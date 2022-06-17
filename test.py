class AllTasks:
    temp_lista = []
    temp_listb = []

    def task1(self):
        print("*" * 100)
        self.temp_lista.clear()
        self.temp_listb.clear()
        integers = input("Enter elements separated by spaces to perform which are divisible by 5 or not?")
        integers= integers.split(' ')
        integers = [int(integers[i]) for i in range(0, len(integers))]
        for item in integers:
            if item % 5 == 0:
                self.temp_lista.append(item)
            else:
                self.temp_listb.append(item)
        return self.temp_lista, self.temp_listb

    def task2(self):
        print("*" * 100)
        self.temp_lista.clear()
        self.temp_listb.clear()
        integers = input("Enter elements separated by spaces to perform which are divisible by 5 and 3 or not?")
        integers = integers.split(' ')
        integers = [int(integers[i]) for i in range(0, len(integers))]
        for item in integers:
            if item % 5 == 0 and item % 3 == 0:
                self.temp_lista.append(item)
            else:
                self.temp_listb.append(item)
        return self.temp_lista, self.temp_listb


    def task3(self):
        print("*" * 100)
        self.temp_lista.clear()
        self.temp_listb.clear()
        integers = input("Enter strings separated by spaces to perform which strings start with 'p' or not?")
        integers = integers.split(' ')
        for item in integers:
            if item[0] == 'p':
                self.temp_lista.append(item)
            else:
                self.temp_listb.append(item)
        return self.temp_lista, self.temp_listb

    def task4(self):
        print("*" * 100)
        self.temp_lista.clear()
        self.temp_listb.clear()
        integers = input("Enter strings separated by spaces to perform which strings start and end with 'p'?")
        integers = integers.split(' ')
        for item in integers:
            if item[0] == 'p' and item[-1] == 'p':
                self.temp_lista.append(item)
            else:
                self.temp_listb.append(item)

        return self.temp_lista, self.temp_listb

    def task5(self):
        print("*" * 100)
        self.temp_lista.clear()
        self.temp_listb.clear()
        five_multiplelist = []
        integers = input("Enter elements separated by spaces to perform which are divisible by 3 "
                         "and not multiples of 5 from any range of numbers")
        integers = integers.split(' ')
        integers = [int(integers[i]) for i in range(0, len(integers))]
        for item in integers:
            if item % 5 == 0:
                five_multiplelist.append(item)
            elif item % 3 == 0 and item not in five_multiplelist:
                self.temp_lista.append(item)
            else:
                self.temp_listb.append(item)
        return self.temp_lista, self.temp_listb

    def task6(self):
        print("*" * 100)
        self.temp_lista.clear()
        self.temp_listb.clear()
        integers = input("Enter list of elements separated by spaces to fetch two lists :"
                         "\n1. Adding +2 for each element in list\n2. Multiplying *2 for each element in list ")
        integers = integers.split(' ')
        integers = [int(integers[i]) for i in range(0, len(integers))]
        for i in integers:
            self.temp_lista.append(i+2)
            self.temp_listb.append(i*2)
        return self.temp_lista, self.temp_listb

    def task7(self):
        password = input("Enter Password : ")
        while(True):
            if password == 'git123':
                message = False
                print("*" * 100)
                print("WELCOME")
                break
            else:
                message = True
                print("Wrong Password... \nEnter correct password")
                break
        return message

    def task8(self):
        password = input("Please Enter [Y/N] : ")
        while(True):
            if password == 'Y':
                message = False
                print("*" * 100)
                print("WELCOME")
                break
            elif password == 'N':
                message = False
                print("*" * 100)
                print("SIGNING OFF!!!")
                break
            else:
                message = True
                print("Please Enter correct option [Y/N]")
                break
        return message

if __name__ == '__main__':
    obj = AllTasks()

    a1, b1 = obj.task1()
    if a1 == []:
        print("The provided Number List : {} are not divisible by 5".format(b1))
    else:
        print("The Number List : {} are divisible by 5".format(a1))
        print("The Number List : {} are not divisible by 5".format(b1))

    a2, b2 = obj.task2()
    if a2 == []:
        print("The provided Number List : {} are not divisible by 5 and 3".format(b2))
    else:
        print("The Number List : {} are divisible by 5 and 3".format(a2))
        print("The Number List : {} are not divisible by 5 and 3".format(b2))

    a3, b3 = obj.task3()
    print("The given word list '{}'{} starts with letter 'P'".format(a3, ' '))
    print("The given word list '{}'{} not starts with letter 'P'".format(b3, ' '))

    a4, b4 = obj.task4()
    print("The given words '{}'{} starts and ends with letter 'P'".format(a4, ' '))
    print("The given words '{}'{} not starts and ends with letter 'P'".format(b4, ' '))

    a5, b5 = obj.task5()
    if a5 == []:
        print("The given numbers list : {} are not divisible by 3 nor with 5 from any range".format(b5))
    else:
        print("The given numbers list : {} are divisible by 3 and not multiples of 5 from any range".format(a5))
        print("The given numbers list : {} are not divisible by 3 nor with 5 from any range".format(b5))

    a6,b6 = obj.task6()
    print("List A : {}\nList B : {}".format(a6, b6))

    print("*" * 100)
    a7 = obj.task7()
    while(a7):
        a7 = obj.task7()

    print("*" * 100)
    a8 = obj.task8()
    while (a8):
        a8 = obj.task8()
    print("*" * 100)

