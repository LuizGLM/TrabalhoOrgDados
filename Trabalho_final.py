import streamlit as st
import pandas as pd
from Graficos import *

# Carregar o dataset
df = pd.read_csv(r"C:\Users\thiag\OneDrive\Área de Trabalho\Trabalhos VS\Org Dados\user_behavior_dataset (1).csv")

# Barra lateral para filtros
st.sidebar.title("Filtros")

# Filtro de idade (apenas para o gráfico 2)
st.sidebar.subheader("Filtro para gráfico de Tempo Médio de Uso por Faixa Etária")
idade_min = st.sidebar.slider("Idade mínima", min_value=int(df['Age'].min()), max_value=int(df['Age'].max()), value=18)
idade_max = st.sidebar.slider("Idade máxima", min_value=int(df['Age'].min()), max_value=int(df['Age'].max()), value=50)

# Filtro combinado de gênero e classe de comportamento (aplicado ao gráfico de Distribuição de Gênero na Classe 5)
st.sidebar.subheader("Filtro para gráfico de Distribuição de Gênero na Classe 5")
genero_filtro = st.sidebar.multiselect("Selecione o(s) Gênero(s)", ['Male', 'Female'], default=['Male', 'Female'])
classe_comportamento_filtro = st.sidebar.selectbox("Selecione a Classe de Comportamento", options=df['User Behavior Class'].unique(), index=0)

# Filtro de sistema operacional (aplicado aos gráficos de Consumo de Bateria e Tempo de Tela)
st.sidebar.subheader("Filtro para gráficos de Consumo de Bateria e Tempo de Tela")
sistema_operacional_filtro = st.sidebar.multiselect(
    "Selecione o Sistema Operacional", 
    options=df['Operating System'].unique(), 
    default=df['Operating System'].unique()  # Exibe todos os sistemas operacionais por padrão
)

# Filtro de modelo de dispositivo (aplicado aos gráficos de Consumo de Bateria e Tempo de Tela)
st.sidebar.subheader("Filtro para gráficos de Consumo de Bateria e Tempo de Tela")
modelo_dispositivo_filtro = st.sidebar.multiselect(
    "Selecione o Modelo de Dispositivo", 
    options=df['Device Model'].unique(), 
    default=df['Device Model'].unique()  # Exibe todos os modelos de dispositivos por padrão
)

# Filtros de exibição dos gráficos
st.sidebar.subheader("Escolher Gráficos")
mostrar_grafico_modelos = st.sidebar.checkbox("Exibir gráfico de Modelos de Dispositivos", value=True)
mostrar_grafico_tempo_uso = st.sidebar.checkbox("Exibir gráfico de Tempo Médio de Uso por Faixa Etária", value=True)
mostrar_grafico_pizza = st.sidebar.checkbox("Exibir gráfico de Distribuição de Classe 5", value=True)
mostrar_grafico_genero = st.sidebar.checkbox("Exibir gráfico de Distribuição de Gênero na Classe 5", value=True)
mostrar_grafico_tempo_tela = st.sidebar.checkbox("Exibir gráfico de Tempo de Tela por Modelo de Dispositivo", value=True)
mostrar_grafico_bateria = st.sidebar.checkbox("Exibir gráfico de Consumo de Bateria por Modelo", value=True)
mostrar_grafico_sistemas = st.sidebar.checkbox("Exibir gráfico de Sistemas Operacionais", value=True)
mostrar_grafico_classes = st.sidebar.checkbox("Exibir gráfico de Distribuição de Classes de Comportamento", value=True)

# Título da página
st.title("Análise de Dados do Uso de Dispositivos Móveis e Comportamento do Usuário")

# Mostrar os gráficos com interações
if mostrar_grafico_modelos:
    st.subheader('1. Quantidade de Modelos de Dispositivos')
    st.write("Este gráfico mostra a quantidade de usuários para cada modelo de dispositivo.")
    dispositivos = df['Device Model'].value_counts()
    fig1 = Grafico_Barras_Modelos_Dispositivos(dispositivos)
    st.pyplot(fig1)

if mostrar_grafico_tempo_uso:
    st.subheader('2. Tempo Médio de Uso por Faixa Etária')
    st.write(f"Este gráfico exibe o tempo médio de uso de dispositivos por faixa etária, com base nas configurações de idade selecionadas. (Idade de {idade_min} a {idade_max})")
    fig2 = Tempo_Médio_de_Uso_por_Faixa_Etária(df, idade_min, idade_max)
    st.pyplot(fig2)

if mostrar_grafico_pizza:
    st.subheader('3. Distribuição de Usuários entre a Classe 5 e Outras Classes')
    st.write("Este gráfico de pizza mostra a distribuição entre os usuários da Classe 5 e outras classes de comportamento.")
    fig3 = Grafico_Pizza_Classe_5(df)
    st.pyplot(fig3)

if mostrar_grafico_genero:
    st.subheader('4. Distribuição de Gênero nas Classes')
    st.write(f"Este gráfico de barras apresenta a distribuição de gênero entre os usuários, com base nos gêneros selecionados e na classe de comportamento {classe_comportamento_filtro}.")
    df_filtrado_genero = df[(df['User Behavior Class'] == classe_comportamento_filtro) & (df['Gender'].isin(genero_filtro))]
    fig4 = Grafico_Barras_Genero_Classe_5(df_filtrado_genero)
    st.pyplot(fig4)

if mostrar_grafico_tempo_tela:
    st.subheader('5. Tempo de Tela por Modelo de Dispositivo')
    st.write(f"Este gráfico mostra o tempo de tela médio por modelo de dispositivo, filtrado para os modelos {modelo_dispositivo_filtro} e sistemas operacionais {sistema_operacional_filtro}.")
    df_filtrado_tempo_tela = df[
        (df['Device Model'].isin(modelo_dispositivo_filtro)) & 
        (df['Operating System'].isin(sistema_operacional_filtro))
    ]
    fig5 = Grafico_Tempo_Tela_Dispositivos(df_filtrado_tempo_tela)
    st.pyplot(fig5)

if mostrar_grafico_bateria:
    st.subheader('6. Consumo de Bateria por Modelo de Dispositivo')
    st.write(f"Este gráfico exibe o consumo médio de bateria por modelo de dispositivo, filtrado para os modelos {modelo_dispositivo_filtro} e sistemas operacionais {sistema_operacional_filtro}.")
    df_filtrado_bateria = df[
        (df['Device Model'].isin(modelo_dispositivo_filtro)) & 
        (df['Operating System'].isin(sistema_operacional_filtro))
    ]
    fig6 = Grafico_Consumo_Bateria(df_filtrado_bateria)
    st.pyplot(fig6)

if mostrar_grafico_sistemas:
    st.subheader('7. Quantidade de Sistemas Operacionais')
    st.write("Este gráfico mostra a quantidade de usuários por sistema operacional.")
    fig7 = Grafico_Sistemas_Operacionais(df)
    st.pyplot(fig7)

if mostrar_grafico_classes:
    st.subheader('8. Distribuição de Classes de Comportamento')
    st.write("Este gráfico exibe a distribuição de classes de comportamento dos usuários.")
    fig8 = Grafico_Classes_Comportamento(df)
    st.pyplot(fig8)
