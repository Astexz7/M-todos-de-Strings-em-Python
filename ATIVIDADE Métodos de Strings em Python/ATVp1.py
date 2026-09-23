#atividade 1 
#letra (a)
n=input('Digite seu nome: ')
print(n.strip())

#atividade 1
#letra(b)
termo = input("Digite o termo de busca: ").strip()
if termo:
    print(f"Pesquisando por: '{termo}'")
else:
    print("Digite algo para pesquisar.")

#atividade 2
#letra (b)
s=input('digite o comando: ')
s_m= s.lower()
print(s_m)

#atividade 2
#letra (b)
email= input('digite seu email: ')
email_m= (email.lower())
print(email_m)

#atividade 3
#letra (a)
c= input('Digite o código do produto: ')
c_M= c.upper()
print(c_M)

#atividade 3
#letra (b)
e= input('Digite a sigla do estado: ')
e_M= e.upper()
print(e_M)

#atividade 4
#letra (a)
name=input('digite seu nome: ')
name_1M= name.title()
print(name_1M)

#atividade 4
#letra (b)
evento=input('Digite o nome do seu evento: ')
evento_1M= evento.title()
print(evento_1M)
print('será as 19:00 no marco zero')

#atividade 5
#letra (a)
numero= input('Digite seu número: ')
numero_r= numero.replace('-',' ')
print(numero_r)

#atividade 5
#letra (b)
valor= input('Digite um valor: ')
valor_p= valor.replace(',','.')
print(valor_p)

#atividade 6
#letra(a)
nic= input('Digite nome; idade; cidade: ')
nic_s= nic.split(';')
print(nic_s)

#atividade 6
#letra(b)
entrada = input("Digite as palavras-chave separadas por vírgulas: ")
lista_termos = entrada.split(",")
print("Lista de termos:")
print(lista_termos)

#atividade 7
#letra(a)
integrantes = ["Ana", "Bruno", "Carla", "Diego"]
print(", ".join(integrantes))

#atividade 7
#letra(b)
caminho = ["Configurações", "Rede", "Wi-Fi", "Avançado"]
print(" > ".join(caminho))

#atividade 8
#letra(a)
frase = input("Digite uma frase: ")
print(frase.lower().count("a"))

#atividade 8
#letra(b)
anotacao = input("Digite a anotação: ")
print(anotacao.lower().count("erro"))

#atividade 9
#letra(a)
comando = input("Digite o comando: ")
print(comando.startswith("/"))

#atividade 9
#letra(b)
codigo = input("Digite o código do produto: ")
print(codigo.startswith("PROD-"))