#Criando Cardapio de Marmitas
print('----- Bem vindo a Loja de Marmitas do Ronald Gabriel Costa Silva -----')
l=(len('----- Bem vindo a Loja de Marmitas do Ronald Gabriel Costa Silva -----'))
print('Cardápio de Marmitas'.center(l, '-'))
print('-'.center(l, '-'))
print('| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |'.center(l, '-'))
print('|    P    |       R$ 16,00      |       R$ 15,00      |'.center(l, '-'))
print('|    M    |       R$ 18,00      |       R$ 17,00      |'.center(l, '-'))
print('|    G    |       R$ 22,00      |       R$ 21,00      |'.center(l, '-'))
print()  

total = 0  #variável para acumular o valor total do pedido
while True: # Loop para permitir múltiplos pedidos
  print('-' * l)  
  while True:
     sabor =  input('Qual o sabor da marmita? (BA/FF): ').strip().upper()
     if sabor not in ['BA', 'FF']:
        print('Sabor inválido. Por favor, escolha BA ou FF.')
        continue
     else:
        break
  while True: 
     tamanho = input('Qual o tamanho da marmita? ( P/ M/ G): ').strip().upper() 
     if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Por favor, escolha P, M ou G.')
        continue
     else:
        break
  valor = 0 
  if sabor == 'BA':
     if tamanho == 'P':
        valor = 16.00
        print(f'Você escolheu Bife Acebolado tamanho P. O valor é R$ 16,00.')
     elif tamanho == 'M':
        valor = 18.00
        print(f'Você escolheu Bife Acebolado tamanho M. O valor é R$ 18,00.')
     else:
        if tamanho == 'G':
           valor = 22.00
           print(f'Você escolheu Bife Acebolado tamanho G. O valor é R$ 22,00.')         
  if sabor == 'FF':
     if tamanho == 'P':
        valor = 15.00
        print(f'Você escolheu Filé de Frango tamanho P. O valor é R$ 15,00.')
     elif tamanho == 'M':
        valor = 17.00  
        print(f'Você escolheu Filé de Frango tamanho M. O valor é R$ 17,00.')
     else:
        if tamanho == 'G':
           valor = 21.00
           print(f'Você escolheu Filé de Frango tamanho G. O valor é R$ 21,00.')
  total += valor  # Acumula o valor do pedido
  print()  
  continuar=(input('Deseja fazer outro pedido?(S/N): ')).strip().upper() # Verifica se o usuário deseja continuar e retoma o loop ou encerra
  print()  
  if continuar == 'S':
        continue
  else:
     if continuar == 'N':
        break
print('-' * l)
print(f'O valor total do seu pedido é R$ {total:.2f}.')
