if __name__ == "__main__":
    #EXERCISE 1
    start = int(input("Введіть початок "))
    end = int(input("Введіть кінець  "))

    for number in range(start, end + 1):
        if number % 7 == 0:
            print(number)
            #EXERCISE 2
            start = int(input("Введіть початок діапазону: "))
            end = int(input("Введіть кінець діапазону: "))
            print("Всі числа у діапазоні")
            for number in range(start, end + 1):
                print(number)
            print("Всі числа у діапазоні")
            for number in range(end, start - 1, -1):
                print(number)
            print("Числа, кратні 7")
            for number in range(start, end + 1):
                if number % 7 == 0:
                    print(number)
            count = 0
            for number in range(start, end + 1):
                if number % 5 == 0:
                    count += 1
            print("Кількість чисел, кратних 5", count)
            #EXERCISE 3
            start = int(input("Введіть початок діапазону: "))
            end = int(input("Введіть кінець діапазону: "))

            for number in range(start, end + 1):
                if number % 3 == 0 and number % 5 == 0:
                    print("Fizz Buzz")
                elif number % 3 == 0:
                    print("Fizz")
                elif number % 5 == 0:
                    print("Buzz")
                else:
                    print(number)
