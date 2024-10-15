def encontrar_letra_a():
    palavra = input("Digite uma palavra")
    contagem = 0
    
    for letra in palavra:
        if letra == "a" or letra == "A":
            contagem = contagem + 1
            

    if contagem == 0:
        print ("Nenhuma letra 'A' foi encontrada.")
    else:
        print ("A letra 'A' foi encontrada " + str(contagem) + " vezes")
   
encontrar_letra_a ()
    