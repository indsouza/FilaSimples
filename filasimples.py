
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

# Implementação da senha normal

    if opcao == "1":
        contador_normal += 1
        senha = f"N{contador_normal:03d}"
        fila_normal.append(senha)
        print(f"Senha normal emitida: {senha}")

# Implementação da senha prioritária

    elif opcao == "2":
        contador_prioritario += 1
        senha = f"P{contador_prioritario:03d}"
        fila_prioritaria.append(senha)
        print(f"Senha prioritária emitida: {senha}")

# Implementação da chamada de senha

    elif opcao == "3":
        if len(fila_prioritaria) > 0:
            senha = fila_prioritaria.pop(0)
            total_atendidos += 1
            print(f"Senha chamada: {senha}")

        elif len(fila_normal) > 0:
            senha = fila_normal.pop(0)
            total_atendidos += 1
            print(f"Senha chamada: {senha}")

        else:
            print("Não existem senhas aguardando atendimento.")

#Consulta às senhas pendentes

    elif opcao == "4":
        print("\n===== SENHAS PENDENTES =====")
        print(f"Senhas normais: {len(fila_normal)}")
        print(f"Senhas prioritárias: {len(fila_prioritaria)}")
        print(f"Total de atendimentos realizados: {total_atendidos}")


    elif opcao == "5":
        print("Encerrando o FilaSimples...")
        executando = False

    else:
        print("Opção inválida. Tente novamente.")
