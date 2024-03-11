# aux = input("Enter yout CPF: ")
# cpf = int(aux)
cpf = "223.450.312-93"
add = 0
mult = 10

for num in cpf:
    if num.isdigit():
        add += int(num) * mult
        mult -= 1

add = (add * 10) % 11
print(add)