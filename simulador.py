import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Simulador de Eficiência Energética para Carros")

# Lista para armazenar os carros
if 'carros' not in st.session_state:
    st.session_state.carros = []

# Função para calcular a meta de eficiência
def calcular_meta_eficiencia(curva, peso):
    if curva == "Curva 1":
        return 1.028297 + (0.000528 * peso)
    elif curva == "Curva 2":
        return 0.790141 + (0.000801 * peso)
    elif curva == "Curva 3":
        return 0.566827 + (0.001103 * peso)
    return 0

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
            "Curva": curva,
            "Meta de Eficiência": calcular_meta_eficiencia(curva, peso)
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
            "Curva": curva,
            "Meta de Eficiência": calcular_meta_eficiencia(curva, peso)
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
            st.write(f"- Meta de Eficiência: {carro['Meta de Eficiência']:.4f} km/L")
            if st.button(f"Editar Carro {i}"):
                st.session_state.editar_index = i - 1
            st.write("---")

# Função para exibir resultados em uma tabela
def exibir_resultados():
    st.subheader("Resultados por Curva")
    
    # Separar carros por curva
    curva_1 = [carro for carro in st.session_state.carros if carro['Curva'] == "Curva 1"]
    curva_2 = [carro for carro in st.session_state.carros if carro['Curva'] == "Curva 2"]
    curva_3 = [carro for carro in st.session_state.carros if carro['Curva'] == "Curva 3"]
    
    # Criar DataFrames para cada curva
    df_curva_1 = pd.DataFrame(curva_1)
    df_curva_2 = pd.DataFrame(curva_2)
    df_curva_3 = pd.DataFrame(curva_3)
    
    # Exibir tabelas
    if not df_curva_1.empty:
        st.write("**Curva 1**")
        st.dataframe(df_curva_1)
    if not df_curva_2.empty:
        st.write("**Curva 2**")
        st.dataframe(df_curva_2)
    if not df_curva_3.empty:
        st.write("**Curva 3**")
        st.dataframe(df_curva_3)

# Menu principal
def menu():
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Escolha uma opção:", ["Adicionar Carro", "Listar Carros", "Resultados"])
    
    if opcao == "Adicionar Carro":
        adicionar_carro()
    elif opcao == "Listar Carros":
        listar_carros()
        if 'editar_index' in st.session_state:
            editar_carro(st.session_state.editar_index)
    elif opcao == "Resultados":
        exibir_resultados()

# Iniciar o aplicativo
if __name__ == "__main__":
    menu()
