def desafio001():
  print('Olá, Mundo!')


def desafio002():
  nome = input('Digite seu nome: ')
  print('É um prazer te conhecer, {}!'.format(nome))


def desafio003():
  n1 = int(input('Digite um valor: '))
  n2 = int(input('Digite outro valor: '))
  soma = n1 + n2
  print(soma)


def desafio004():
  a = input('Digite algo: ')
  print('O tipo primitivo desse valor é', type(a))
  print('Só tem espaços?', a.isspace())
  print('É um número?', a.isnumeric())
  print('É alfabético?', a.isalpha())
  print('É alfanumérico?', a.isalnum())
  print('Está em maiúsculas?', a.isupper())
  print('Está em minúsculas?', a.islower())
  print('Está capitalizada?', a.istitle())


def desafio005():
  n = int(input('Digite um número: '))
  print('analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))