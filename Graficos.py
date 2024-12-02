import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.clf()  # Limpa qualquer figura ou configuração anterior

def Grafico_Barras_Modelos_Dispositivos(dispositivos):
    fig, ax = plt.subplots(figsize=(10, 5))
    dispositivos.plot(kind='barh', color='skyblue', edgecolor='black', ax=ax)
    ax.set_title('Quantidade de cada modelo de dispositivo')
    ax.set_xlabel('Contagem')
    ax.set_ylabel('Modelo de dispositivo')
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels(dispositivos.index, rotation=45)
    ax.set_xlim(120, None)
    return fig

def Tempo_Médio_de_Uso_por_Faixa_Etária(df, idade_min, idade_max):
    df_filtrado = df[(df['Age'] >= idade_min) & (df['Age'] <= idade_max)]
    media = df_filtrado.groupby("Age", observed=False)["App Usage Time (min/day)"].mean()  # Verifique o nome da coluna
    media_em_horas = media / 60
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.bar(media_em_horas.index, media_em_horas.values, color='salmon')
    ax.set_title("Tempo Médio de Uso por Faixa Etária (horas)")
    ax.set_xlabel("Faixa Etária")
    ax.set_ylabel("Tempo Médio de Uso (horas/dia)")
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    return fig

def Grafico_Pizza_Classe_5(df):
    df_classe_5 = df['User Behavior Class'].value_counts()
    classe_5_count = df_classe_5.get(5, 0)
    outras_classes_count = df_classe_5.sum() - classe_5_count
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.pie([classe_5_count, outras_classes_count], labels=["Classe 5", "Outras Classes"], autopct='%1.1f%%', startangle=90, colors=['purple', 'lightgray'])
    ax.set_title('Distribuição de Classe 5 e Outras Classes de Comportamento')
    return fig

def Grafico_Barras_Genero_Classe_5(df):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.countplot(data=df, x='Gender', ax=ax, palette='pastel')
    ax.set_title('Distribuição de Gênero nas Classes')
    ax.set_xlabel('Gênero')
    ax.set_ylabel('Contagem')
    return fig

def Grafico_Tempo_Tela_Dispositivos(df):
    df_agrupado = df.groupby('Device Model')['Screen On Time (hours/day)'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Screen On Time (hours/day)', y='Device Model', data=df_agrupado, palette='Blues', edgecolor='black', ax=ax)
    ax.set_title('Média entre Tempo de Uso por Modelos de Dispositivo', fontsize=16, pad=20)
    ax.set_xlabel('Tempo de Uso (h/dia)', fontsize=12, labelpad=20)
    ax.set_ylabel('Modelos', fontsize=12)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha="right")
    ax.set_xlim(4, None)
    plt.tight_layout()
    return fig


def Grafico_Consumo_Bateria(df):
    df_battery_drain = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Battery Drain (mAh/day)', y='Device Model', data=df_battery_drain, palette='Greens', edgecolor='black', ax=ax)
    ax.set_title('Média de Consumo de Bateria por Modelo', fontsize=16, pad=20)
    ax.set_xlabel('Consumo de Bateria (mAh/dia)', fontsize=12, labelpad=20)
    ax.set_ylabel('Modelo de Dispositivo', fontsize=12)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha="right")
    ax.set_xlim(1400, None)
    plt.tight_layout()
    return fig


def Grafico_Sistemas_Operacionais(df):
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.countplot(data=df, x='Operating System', palette='muted', ax=ax)
    ax.set_title('Distribuição por Sistema Operacional')
    ax.set_xlabel('Sistema Operacional')
    ax.set_ylabel('Contagem')
    return fig

def Grafico_Classes_Comportamento(df):
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.countplot(data=df, x='User Behavior Class', ax=ax, palette='Set2')
    ax.set_title('Distribuição de Classes de Comportamento')
    ax.set_xlabel('Classe de Comportamento')
    ax.set_ylabel('Contagem')
    return fig
