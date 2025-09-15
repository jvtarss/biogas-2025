import pandas as pd

# Define o nome do arquivo de entrada
file_path = 'final-medatata.csv'

try:
    # Lê o arquivo .csv, usando ';' como separador e ignorando as linhas de comentário que começam com '#'
    # O Pandas é inteligente o suficiente para pegar o cabeçalho mesmo que ele comece com '#'
    df = pd.read_csv(file_path, sep=';', comment='#')

    # Remove o caractere '#' do nome da primeira coluna, se existir
    df.rename(columns={'#SampleID': 'SampleID'}, inplace=True)

    # 1. Calcular a contagem total de amostras para cada autor no dataset completo
    author_total_counts = df['author'].value_counts().to_dict()

    # 2. Agrupar os dados pela coluna 'condition1' (biomassa)
    grouped = df.groupby('condition1')

    # Lista para armazenar os dados da tabela final
    table_data = []

    # 3. Iterar sobre cada grupo de biomassa para construir as linhas da tabela
    for biomass, group_df in grouped:
        # Pega os autores únicos dentro do grupo de biomassa
        unique_authors_in_group = group_df['author'].unique()
        
        # Formata a string de autores com sua contagem total de amostras
        authors_formatted = []
        for author in unique_authors_in_group:
            # Pega a contagem total do dicionário criado anteriormente
            total_count = author_total_counts.get(author, 0)
            authors_formatted.append(f"{author}({total_count})")
        
        authors_string = ", ".join(authors_formatted)
        
        # Conta o número de amostras no grupo atual
        total_in_group = len(group_df)
        
        # Adiciona a linha formatada à nossa lista de dados
        table_data.append({
            'biomass': biomass,
            'authors': authors_string,
            'valor total': total_in_group
        })

    # 4. Criar o DataFrame final a partir dos dados coletados
    result_df = pd.DataFrame(table_data)

    # 5. Calcular o número total de amostras
    grand_total = len(df)

    # --- Imprimir a saída ---
    print("Tabela de Amostras por Biomassa:")
    # Imprime o DataFrame como uma string formatada e sem o índice
    print(result_df.to_string(index=False))
    print("-" * 40) # Linha separadora
    print(f"Número total de amostras: {grand_total}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")
