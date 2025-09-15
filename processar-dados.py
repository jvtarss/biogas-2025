import pandas as pd

file_path = 'final-medatata.csv'

try:
    df = pd.read_csv(file_path, sep=';', comment='#')
    df.rename(columns={'#SampleID': 'SampleID'}, inplace=True)
    author_total_counts = df['author'].value_counts().to_dict()
    grouped = df.groupby('condition1')
    table_data = []

    for biomass, group_df in grouped:
        unique_authors_in_group = group_df['author'].unique()
        
        authors_formatted = []
        for author in unique_authors_in_group:
            total_count = author_total_counts.get(author, 0)
            authors_formatted.append(f"{author}({total_count})")
        
        authors_string = ", ".join(authors_formatted)
        
        total_in_group = len(group_df)
        
        table_data.append({
            'biomass': biomass,
            'authors': authors_string,
            'valor total': total_in_group
        })

    result_df = pd.DataFrame(table_data)

    grand_total = len(df)

    print("Tabela de Amostras por Biomassa:")
    print(result_df.to_string(index=False))
    print("-" * 40)
    print(f"numero total de amostras: {grand_total}")

except FileNotFoundError:
    print(f"arquivo faltante '{file_path}'.")
except Exception as e:
    print(f"erro de processamento {e}")
