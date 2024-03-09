# make a shopping list.
# The user should be able to enter, delete and see the list

lista = ['banana', 'rice']

while True:
    print("\n0 - get out")
    print("1 - insert")
    print("2 - remove")
    print("3 - show the list")
    answer = input("")

    if answer == '0':
        break
    elif answer == '1':
        answer_insert = input("What do you want to insert? ")
        lista.append(answer_insert)
    elif answer == '2':
        answer_remove = int(input("Which index do you want to remove? "))
        try :
            del lista[answer_remove]
        except :
            print("There is nothing in this index.")
    elif answer == '3':
        for element in enumerate(lista) :
            print(element)
    else:
        print("Invalid option. Please choose a valid option (0-3).")
