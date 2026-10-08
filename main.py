import analisadorlexico

texttemp = analisadorlexico.readFile("linguagemp.txt")
meu_analisador = analisadorlexico.reconheceLexema(texttemp)
tokens = meu_analisador.executarLeitura()
tokensatualizado = analisadorlexico.identificarPalavrasReservadas(tokens)
print(tokensatualizado)