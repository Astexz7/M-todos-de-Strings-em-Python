#atividade 10
#letra(a)
n= input('Digite o nome do arquivo: ')
print(n.endswith(".csv"))

#atividade 10
#letra(b)
e= input('Digite seu email institucional: ')
print(e.endswith("@ufrpe.br"))

#atividade 11
#letra(a)
a=input('Digite seu email: ')
print(a.find('@'))

#atividade 11
#letra(b)
b=input('Digite o comando:valor; ')
print(b.find(':'))

#atividade 12
#letra(a)
c=input('Digite seu nome: ')
print(c.isalpha())

#atividade 12
#letra(b)
categoria=input('Digite uma categoria: ')
if categoria.isalpha():
    print(f'Válido. {categoria}')
else:
    print('Inválido (Digite apenas letras)')

#atividade 13
#letra(a)
number=input('Digite um número: ')
print(number.isdigit())

#atividade 13
#letra(b)
age=input('Digite sua idade: ')
if age.isdigit():
    print(f'Válido. {age}')
else:
    print('Inválido. (Digite apenas números)')

#atividade 14
#letra(a)
codigo=input('Digite o código: ')
print(codigo.isalnum())

#atividade 14
#letra(b)
codigo2=input('Digite o código: ')
if codigo2.isalnum():
    print(f'Válido. {codigo2}')
else:
    print('Inváldio. (Não é permitido caracteres especiais)')

#atividade 15
#letra(a)
space= input('Digite: ')
print(space.isspace())

#atividade 15
#letra(b)
space2= input('Digite:')
if space2.isspace():
    print(f'Você digitou apenas espaços')
else:
    print('Válido')

#atividade 16
#letra(a)
maiusc= input("Digite uma sigla: ")
print(maiusc.isupper())

#atividade 16
#letra(b)
codigomaiusc= input('Digite o código (apenas letras maiúsculas): ')
if codigomaiusc.isupper:
    print('Válido')
else:
    print('Digite apenas letras maiúsculas!!')

#atividade 17
#letra(a)
comando= input('Digite o comando: ')
if comando.islower():
    print('Válida')
else:
    print('Digite apenas letras minúsculas!!')

#atividade 17
#letra(b)
user= input("Digite nome de usuário: ")
if user.islower():
    print(f'Válida. {user}')
else:
    print('Digite apenas letras minúsculas!!')

#atividade 18
#letra(a)
senha= input('Digite uma senha: ')
print(senha.zfill(5))

#atividade 18
#letra(b)
nota= input('Digite sua nota: ')
print(nota.zfill(8))