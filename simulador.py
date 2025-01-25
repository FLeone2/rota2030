import streamlit as st

# Título do aplicativo
st.title("Simulador de Eficiência Energética para Carros")

# Lista para armazenar os carros
if 'carros' not in st.session_state:
    st.session_state.carros = []

# Função para adicionar um carro
def adicionar_carro():
    st.subheader("Adicionar Novo Carro")
    
    # Campos de entrada de dados
    nome = st.text_input("Nome do carro")
    peso = st.number_input("Peso do carro (em kg)", min_value=0.0)
    eficiencia = st.number_input("Eficiência energética (em km/L)", min_value=0.0)
    valor_bin = st.number_input("Valor de bin", min_value=0.0)
    tipo_combustivel = st.selectbox("Tipo de combustível", ["Diesel", "Gasolina", "Flex"])
    
    # Botão para adicionar o carro
    if st.button("Adicionar Carro"):
        carro = {
            "Nome": nome,
            "Peso": peso,
            "Eficiência": eficiencia,
            "Valor Bin": valor_bin,
            "Tipo de Combustível": tipo_combustivel
        }
        st.session_state.carros.append(carro)
        st.success(f"Carro '{nome}' adicionado com sucesso!")

# Função para listar todos os carros
def listar_carros():
    st.subheader("Lista de Carros")
    if not st.session_state.carros:
        st.write("Nenhum carro cadastrado.")
    else:
        for i, carro in enumerate(st.session_state.carros, start=1):
            st.write(f"**Carro {i}:**")
            st.write(f"- Nome: {carro['Nome']}")
            st.write(f"- Peso: {carro['Peso']} kg")
            st.write(f"- Eficiência: {carro['Eficiência']} km/L")
            st.write(f"- Valor Bin: {carro['Valor Bin']}")
            st.write(f"- Tipo de Combustível: {carro['Tipo de Combustível']}")
            st.write("---")

# Menu principal
def menu():
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Escolha uma opção:", ["Adicionar Carro", "Listar Carros"])
    
    if opcao == "Adicionar Carro":
        adicionar_carro()
    elif opcao == "Listar Carros":
        listar_carros()

# Iniciar o aplicativo
if __name__ == "__main__":
    menu()
