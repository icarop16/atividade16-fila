# Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não.
print("Em qual situação você se encontra?")
print("""1: Gestante;
2: Idoso;
3: Cadeirante;
4: Nenhuma das anteriores.""")
situacao = int(input("Eu me enquadro na situação n° "))
if (situacao == 1) or (situacao == 2) or (situacao == 3) :
    print("""Você é cliente prioritário.
    Por favor, vá até a fila preferencial.""")
else :
    print("""Você não é cliente prioritário.
    Por favor, vá até a fila comum.""")