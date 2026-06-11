import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo = 'data_extraction.xls'

try:
    df = pd.read_excel(caminho_arquivo)
    nome_coluna = 'Condição de iluminação'
    
    if nome_coluna not in df.columns:
        print(f"A coluna '{nome_coluna}' não foi encontrada na planilha.")
    else:
        
        dados_normalizados = df[nome_coluna].dropna().astype(str).str.split(',').explode().str.strip()
        
        contagem = dados_normalizados.value_counts()
        
        print("Dados normalizados:")
        print(contagem)
        
        plt.figure(figsize=(8, 8))
        
        patches, texts, autotexts = plt.pie(
            contagem.values, 
            labels=contagem.index, 
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.Pastel1.colors
        )
        
        for text in texts:
            text.set_fontweight('light')
            text.set_fontsize(12)
            
        for autotext in autotexts:
            autotext.set_fontweight('light')
            autotext.set_fontsize(11)
            
        plt.title('Lighting Conditions (Normalized)', fontsize=16, fontweight='light')
        
        plt.show()

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")