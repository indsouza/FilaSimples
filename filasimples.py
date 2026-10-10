
# Contadores para gerar as senhas

contador_normal = 0
contador_prioritario = 0

# Listas para armazenar as senhas pendentes

fila_normal = []
fila_prioritaria = []

# Contador de atendimentos realizados

total_atendidos = 0

# Variável para controlar a execução do programa

executando = True


# Menu principal do sistema
while executando:
    print("\n===== FILASIMPLES =====")
    print("1 - Emitir senha normal")
    print("2 - Emitir senha prioritária")
    print("3 - Chamar próxima senha")
    print("4 - Consultar senhas pendentes")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu emitir uma senha normal.")

    elif opcao == "2":
        print("Você escolheu emitir uma senha prioritária.")

    elif opcao == "3":
        print("Você escolheu chamar a próxima senha.")

    elif opcao == "4":
        print("Você escolheu consultar as senhas pendentes.")

    elif opcao == "5":
        print("Encerrando o FilaSimples...")
        executando = False

    else:
        print("Opção inválida. Tente novamente.")
