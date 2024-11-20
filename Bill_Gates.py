def resumo():
    mensagem = "Bill Gates foi, por muitos anos, a pessoa mais rica do mundo, acumulando sua fortuna principalmente com o crescimento exponencial da Microsoft. Ele é frequentemente elogiado por sua visão empresarial e capacidade de antecipar você. Fundação da Microsoft (1975) :MS-DOS ,Windows."
    return mensagem


def doutorado():
    mensagem = "Bill Gates não possui doutorado formal"
    return mensagem


def contribuicoes():
<<<<<<< HEAD
    mensagem = "opularização dos computadores pessoais, Avanço da indústria de software,Soluções climáticas e agrícolas"
=======
    mensagem = "As contribuições de Bill Gates abrangem a tecnologia, a filantropia e a transformação social. Ele é considerado uma figura chave no avanço tecnológico."
>>>>>>> origin/branch-iago
    return mensagem


def artigos():
    mensagem = "Bill Gates não é conhecido por publicar artigos acadêmicos, mas frequentemente escreve e compartilha análises, reflexões e ideias sobre tecnologia, filantropia, saúde pública e mudanças climáticas. Esses textos são publicados em seu blog oficial, Gates Notes"
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
