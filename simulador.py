# Lista para armazenar os carros
carros = []

# Função para adicionar um carro
def adicionar_carro():
    print("\n--- Adicionar Novo Carro ---")
    
    # Solicitar informações do carro
    nome = input("Nome do carro: ")
    peso = float(input("Peso do carro (em kg): "))
    eficiencia = float(input("Eficiência energética (em km/L): "))
    valor_bin = float(input("Valor de bin: "))
    tipo_combustivel = input("Tipo de combustível (Diesel, Gasolina, Flex): ").capitalize()
    
    # Criar um dicionário para o carro
    carro = {
        "Nome": nome,
        "Peso": peso,
        "Eficiência": eficiencia,
        "Valor Bin": valor_bin,
        "Tipo de Combustível": tipo_combustivel
    }
    
    # Adicionar o carro à lista
    carros.append(carro)
    print(f"Carro '{nome}' adicionado com sucesso!")

# Função para listar todos os carros
def listar_carros():
    print("\n--- Lista de Carros ---")
    for i, carro in enumerate(carros, start=1):
        print(f"Carro {i}:")
        for chave, valor in carro.items():
            print(f"  {chave}: {valor}")
        print()

# Menu principal
def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar Carro")
        print("2. Listar Carros")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_carro()
        elif opcao == "2":
            listar_carros()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    menu()
