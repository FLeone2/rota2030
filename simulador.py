import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

# Inserir dados dos veículos manualmente
st.subheader('Inserir Dados dos Veículos')

# Número de veículos a serem cadastrados
num_veiculos = st.number_input('Quantos veículos deseja cadastrar?', min_value=1, value=1)

# Lista para armazenar os dados dos veículos
dados_veiculos = []

# Loop para coletar os dados de cada veículo
for i in range(num_veiculos):
    st.markdown(f"### Veículo {i + 1}")
    modelo = st.text_input(f'Nome do Veículo {i + 1}', key=f'modelo_{i}')
    peso = st.number_input(f'Peso (kg) do Veículo {i + 1}', min_value=0, value=1500, key=f'peso_{i}')
    eficiencia = st.number_input(f'Eficiência Energética (MJ/km) do Veículo {i + 1}', min_value=0.0, value=1.8, key=f'eficiencia_{i}')
    tipo_combustivel = st.selectbox(f'Tipo de Combustível do Veículo {i + 1}', ['FLEX', 'GASOLINA'], key=f'tipo_{i}')
    fator_etanol = st.number_input(f'Fator Etanol do Veículo {i + 1}', min_value=0.0, value=1.5, key=f'fator_{i}')

    # Adicionar os dados do veículo à lista
    dados_veiculos.append({
        'Modelo': modelo,
        'Peso (kg)': peso,
        'Eficiência Energética (MJ/km)': eficiencia,
        'Tipo Combustível': tipo_combustivel,
        'Fator Etanol': fator_etanol
    })

# Converter a lista de veículos em um DataFrame
dados_veiculos_df = pd.DataFrame(dados_veiculos)

# Exibir tabela de veículos cadastrados
if not dados_veiculos_df.empty:
    st.subheader('Veículos Cadastrados')
    st.write(dados_veiculos_df)

    # Inserir volumes de vendas
    st.subheader('Inserir Volumes de Vendas')
    volumes_vendas = {}
    for veiculo in dados_veiculos_df['Modelo']:
        volumes_vendas[veiculo] = st.number_input(f'Volume de vendas para {veiculo}', min_value=0, value=100)

    # Simular
    if st.button('Simular'):
        resultados = []
        for index, veiculo in dados_veiculos_df.iterrows():
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
    st.warning("Nenhum veículo cadastrado. Insira os dados dos veículos acima.")
