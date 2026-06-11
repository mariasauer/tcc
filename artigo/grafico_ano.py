import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo = 'data_extraction.xls'

try:
    df = pd.read_excel(caminho_arquivo)

    if 'Ano de publicação' not in df.columns:
        print("The 'Ano de publicação' column was not found in the spreadsheet.")
    else:
        contagem_por_ano = df['Ano de publicação'].value_counts().sort_index()
        plt.figure(figsize=(8, 5))
        
        plt.plot(contagem_por_ano.index, contagem_por_ano.values, marker='o', linestyle='-', color='b')
        
        for x, y in zip(contagem_por_ano.index, contagem_por_ano.values):
            plt.text(
                x, 
                y + 0.8,          
                str(y),           
                ha='center',      
                va='bottom',      
                fontsize=11,      
                fontweight='light' 
            )
        
        plt.title('Number of Articles per Year', fontsize=14, fontweight='normal') 
        plt.xlabel('Year', fontsize=12, fontweight='light')                        
        plt.ylabel('Number of Articles', fontsize=12, fontweight='light')          
        
        plt.ylim(0, max(contagem_por_ano.values) + 4)
        
        plt.xticks(contagem_por_ano.index, fontweight='light')                     
        plt.yticks(fontweight='light')                                             
        
        plt.grid(True, linestyle='--', alpha=0.5)
        
        plt.show()

except FileNotFoundError:
    print(f"Error: The file '{caminho_arquivo}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")