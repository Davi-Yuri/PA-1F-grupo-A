#escrever um programa que o usuário digita um número de 1 a 20
#o programa deverá fazer uma contagem regressiva
#não permitir que o usuario digite número maior que 20 ou menor que 1
#imprimir uma mensagem de "acabou a contagem" no final.
#não permitir digitar letras

n = int(input("escreva um número de 1 a 20"))

if n > 20:
 print("número não aceito")

elif n < 1:
 print("número não aceito")

else:

 for i in range (n):
        print(n - i)

print("acabou a contagem")