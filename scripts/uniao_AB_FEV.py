import pandas as pd

##caminho dos arquivos
path_json = 'raw/dados_empresaA.json'
path_csv = 'raw/dados_empresaB.csv'

#leitura dos arquivos, criando dataframes
def leitura_data(path_json, path_csv):
    df = pd.read_json(path_json)
    df2 = pd.read_csv(path_csv, sep = ',')
    return df2, df

#renomenado algumas colunas
def renomear(df2):
    df2.rename(columns={"Valor em Reais (R$)":"Preço do Produto (R$)"}, inplace=True)
    df2.rename(columns={"Nome do Item":"Nome do Produto"},inplace= True)
    df2.rename(columns={"Classificação do Produto":"Categoria do Produto"},inplace= True)
    df2.rename(columns={"Nome da Loja":"Filial"},inplace= True)
    return df2

#criação do df completo, com a união dos dados da emp A e B + Tratamento coluna Data da Venda
def uniao (df2, df):
    df_completo = pd.concat([df, df2], ignore_index=True)
    df_completo["Data da Venda"] = df_completo["Data da Venda"].fillna("Não fornecido")
    return df_completo

if __name__ == "__main__":
    df2, df = leitura_data(path_json, path_csv)
    df2 = renomear(df2)
    df_completo = uniao(df2, df)

    # Salvando em CSV
    df_completo.to_csv("data_processed/Dados_completos.csv", index=False)
    print("Arquivo salvo com sucesso em: data_processed/Dados_completos.csv")