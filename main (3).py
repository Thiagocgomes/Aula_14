#Exercício 1: Remova o último elemento de uma lista e imprima a lista resultante.

lista = [1,2,3,4,5]
lista1 = lista.pop()
print(lista)

#Exercício 2: Remova o elemento de índice 2 de uma lista e imprima a lista resultante

lista = [10,20,30,40,50]
lista1 = lista.pop(2)
print(lista)

#Exercício 3: Crie uma pilha usando uma lista e implemente a operação pop().

lista = [1,2,3,4,5]
lista.pop()
print(lista)

#Exercício 4: Remova o primeiro elemento de uma lista e o último elemento usando pop() e imprima a lista resultante.

lista = [1,2,3,4,5]
lista1 = lista.pop(0)
lista2 = lista.pop(3)
print(lista)

#Exercício 5: Acesse os três primeiros caracteres de uma string.

minha_string = "Bom dia, tudo bem?"
part1 = minha_string[:3]
print(part1)

#Exercício 6: Acesse todos os elementos de uma lista, exceto o primeiro e o último.

string = "Welcome"
part2 = string[1:-1]
print(part2)

#Desafio Calculadora

nota = float(input("Por favor, insira a primeira nota: "))
nota1 = float(input("Por favor, insira a segunda nota: "))
nota3 = float(input("Por favor, insira a terceira nota: "))
media = (nota + nota1 + nota3) / 3
if 0 <= media <= 10:
  if media >= 7:
      resultado = "Aprovado"
  elif media >= 5:
      resultado = "Recuperação"
  else:
      resultado = "Reprovado"

  print(f"Sua média é {media} e você está em {resultado}.")
else:
  print("Você está reprovado")
    
