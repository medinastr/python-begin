# aux = input("Enter yout CPF: ")
# cpf = int(aux)
cpf = "746.824.890-70"
add = 0
mult = 10

for num in cpf :
    if num.isdigit():
        add += int(num) * mult
        #print(num, int(num) * mult, add)
        mult -= 1
        if mult < 2 :
            break

add = (add * 10) % 11

if add > 9 and cpf[0] == '0' or add == int(cpf[0]) :
    print("CPF ok.")
else :
    print("Invalid CPF.")