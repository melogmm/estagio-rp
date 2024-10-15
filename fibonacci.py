def checa_fibonacci():
    escolha_usuario = input('Insira um número: ')
    numero_usuario = int(escolha_usuario)
    
    if numero_usuario == 0 or numero_usuario == 1:
        print("Está na sequência de Fibonacci!")
        return
    
 
    soma_atual = 0
    primeiro_numero_da_sequencia = 0
    segundo_numero_da_sequencia = 1

    
    while soma_atual < numero_usuario:
        soma_atual = primeiro_numero_da_sequencia + segundo_numero_da_sequencia
        if soma_atual > numero_usuario:
            print("Não está na sequência de Fibonacci!")
            return
        
        print("Soma atual:", soma_atual)

        if soma_atual == numero_usuario:
            print("Está na sequência de Fibonacci!")
            return

        primeiro_numero_da_sequencia = segundo_numero_da_sequencia
        segundo_numero_da_sequencia = soma_atual
        
checa_fibonacci()

