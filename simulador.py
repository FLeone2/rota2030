import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados do Excel
def carregar_dados():
    try:
        dados = pd.read_excel('dados_veiculos.xlsx', sheet_name='Veiculos')
        st.success("Arquivo Excel carregado com sucesso!")
        return dados
    except FileNotFoundError:
        st.error("Erro: Arquivo 'dados_veiculos.xlsx' não encontrado.")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo Excel: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# Função para calcular a eficiência final
def calcular_eficiencia_final(veiculo, volume_vendas):
    eficiencia_base = veiculo['Eficiência Energética (MJ/km)']
    if veiculo['Tipo Combustível'] == 'FLEX':
        creditos_flex = 0.04 + (0.416 * (veiculo['Fator Etanol'] - 1))
        eficiencia_final = eficiencia_base - creditos_flex
    else:
        eficiencia_final = eficiencia_base
    return eficiencia_final * volume_vendas

# Interface do Streamlit
st.title('Simulador de Eficiência Energética de Veículos')

# Carregar dados dos veículos
dados_veiculos = carregar_dados()

# Verificar se os dados foram carregados corretamente
if not dados_veiculos.empty:
    # Exibir tabela de veículos
    st.subheader('Dados dos Veículos')
    st.write(dados_veiculos)

    # Inserir volumes de vendas
    st.subheader('Inserir Volumes de Vendas')
    volumes_vendas = {}
    for modelo in dados_veiculos['Modelo']:
        volumes_vendas[modelo] = st.number_input(f'Volume de vendas para {modelo}', min_value=0, value=100)

    # Simular
    if st.button('Simular'):
        resultados = []
        for index, veiculo in dados_veiculos.iterrows():
            eficiencia_final = calcular_eficiencia_final(veiculo, volumes_vendas[veiculo['Modelo']])
            resultados.append({
                'Modelo': veiculo['Modelo'],
                'Eficiência Final (MJ/km)': eficiencia_final,
                'Volume de Vendas': volumes_vendas[veiculo['Modelo']]
            })
        
        # Converter resultados em DataFrame
        resultados_df = pd.DataFrame(resultados)

        # Exibir resultados
        st.subheader('Resultados da Simulação')
        st.write(resultados_df)

        # Gráfico de barras
        st.subheader('Gráfico de Eficiência Energética')
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Modelo', y='Eficiência Final (MJ/km)', data=resultados_df)
        plt.xlabel('Modelo')
        plt.ylabel('Eficiência Final (MJ/km)')
        plt.title('Eficiência Energética por Modelo')
        st.pyplot(plt)

        # Gráfico de dispersão (Volume de Vendas vs Eficiência)
        st.subheader('Relação entre Volume de Vendas e Eficiência')
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Volume de Vendas', y='Eficiência Final (MJ/km)', hue='Modelo', data=resultados_df, s=100)
        plt.xlabel('Volume de Vendas')
        plt.ylabel('Eficiência Final (MJ/km)')
        plt.title('Relação entre Volume de Vendas e Eficiência')
        st.pyplot(plt)
else:
    st.warning("Não foi possível carregar os dados dos veículos. Verifique o arquivo Excel.")
