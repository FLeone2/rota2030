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
    curva = st.selectbox("Curva", ["Curva 1", "Curva 2", "Curva 3"])
    
    # Botão para adicionar o carro
    if st.button("Adicionar Carro"):
        carro = {
            "Nome": nome,
            "Peso": peso,
            "Eficiência": eficiencia,
            "Valor Bin": valor_bin,
            "Tipo de Combustível": tipo_combustivel,
            "Curva": curva
        }
        st.session_state.carros.append(carro)
        st.success(f"Carro '{nome}' adicionado com sucesso!")

# Função para editar um carro
def editar_carro(index):
    st.subheader(f"Editar Carro: {st.session_state.carros[index]['Nome']}")
    
    # Campos de entrada de dados com os valores atuais
    nome = st.text_input("Nome do carro", value=st.session_state.carros[index]['Nome'])
    peso = st.number_input("Peso do carro (em kg)", min_value=0.0, value=st.session_state.carros[index]['Peso'])
    eficiencia = st.number_input("Eficiência energética (em km/L)", min_value=0.0, value=st.session_state.carros[index]['Eficiência'])
    valor_bin = st.number_input("Valor de bin", min_value=0.0, value=st.session_state.carros[index]['Valor Bin'])
    tipo_combustivel = st.selectbox("Tipo de combustível", ["Diesel", "Gasolina", "Flex"], index=["Diesel", "Gasolina", "Flex"].index(st.session_state.carros[index]['Tipo de Combustível']))
    curva = st.selectbox("Curva", ["Curva 1", "Curva 2", "Curva 3"], index=["Curva 1", "Curva 2", "Curva 3"].index(st.session_state.carros[index]['Curva']))
    
    # Botão para salvar as alterações
    if st.button("Salvar Alterações"):
        st.session_state.carros[index] = {
            "Nome": nome,
            "Peso": peso,
            "Eficiência": eficiencia,
            "Valor Bin": valor_bin,
            "Tipo de Combustível": tipo_combustivel,
            "Curva": curva
        }
        st.success(f"Carro '{nome}' atualizado com sucesso!")

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
            st.write(f"- Curva: {carro['Curva']}")
            if st.button(f"Editar Carro {i}"):
                st.session_state.editar_index = i - 1
            st.write("---")

# Menu principal
def menu():
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Escolha uma opção:", ["Adicionar Carro", "Listar Carros"])
    
    if opcao == "Adicionar Carro":
        adicionar_carro()
    elif opcao == "Listar Carros":
        listar_carros()
        if 'editar_index' in st.session_state:
            editar_carro(st.session_state.editar_index)

# Iniciar o aplicativo
if __name__ == "__main__":
    menu()
