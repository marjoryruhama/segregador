import glob
import pandas as pd

# Encontra todos os arquivos .csv na pasta atual
arquivos_csv = glob.glob("*.csv")

if not arquivos_csv:
    print("Nenhum arquivo .csv encontrado na pasta.")
    exit()

print(f"{len(arquivos_csv)} arquivo(s) encontrado(s): {arquivos_csv}")

# Lê cada arquivo e empilha em uma lista de DataFrames
# sep=";" para ponto e vírgula — troque por "," se necessário
# on_bad_lines="skip" ignora linhas malformadas sem interromper a leitura
dataframes = [
    pd.read_csv(f, sep=";", encoding="utf-8", on_bad_lines="skip")
    for f in arquivos_csv
]

# Concatena todos os DataFrames verticalmente (empilha as linhas)
df_consolidado = pd.concat(dataframes, ignore_index=True)

print(f"Total de linhas antes da deduplicação: {len(df_consolidado)}")

# Remove linhas completamente duplicadas
df_consolidado.drop_duplicates(inplace=True)

print(f"Total de linhas após a deduplicação:  {len(df_consolidado)}")

# Exporta o resultado final; index=False omite a coluna de índice do pandas
df_consolidado.to_csv("dados_consolidados.csv", sep=";", index=False, encoding="utf-8")

print("Arquivo 'dados_consolidados.csv' gerado com sucesso.")
