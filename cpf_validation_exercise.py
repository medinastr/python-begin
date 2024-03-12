cpf = input("Enter yout CPF: ")

digit1 = 0
mult1 = 10

digit2 = 0
mult2 = 11

for num in cpf[:9] :
    digit1 += int(num) * mult1
    mult1 -= 1
    digit2 += int(num) * mult2
    mult2 -= 1

digit1 = (digit1 * 10) % 11
digit1 = digit1 if digit1 <= 9 else 0

digit2 = ((digit2 + digit1 * 2) * 10) % 11
digit2 = digit2 if digit2 <= 9 else 2

cpf_validation = cpf[:9] + str(digit1) + str(digit2)

if cpf_validation == cpf :
    print("CPF ok.")
else :
    print("Invalid CPF.")