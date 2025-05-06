import pandas as pd 

class Dados:

    def __init__(self, path, type):
        self.path = path
        self.type = type
        self.data = None

    def leitura_dados(self):
        if self.type == "json":
            self.data = pd.read_json(self.path)
        elif self.type == "csv":
            self.data = pd.read_csv(self.path, sep = ",")
        else:
            print("tipo não encontrado")
        return self.data
    
    def renomear(self):
        if self.data is not None:
            self.data.rename(columns={"Valor em Reais (R$)":"Preço do Produto (R$)",
                                "Nome do Item":"Nome do Produto",
                                "Classificação do Produto":"Categoria do Produto",
                                "Nome da Loja":"Filial"}, inplace=True)
        return self.data
    
class Unificar: 

    def __init__(self, dados1, dados2):
        self.df1 = dados1.data
        self.df2 = dados2.data
        self.df_completo = None

    def fusion(self):
        self.df_completo = pd.concat([self.df1, self.df2], ignore_index=True)
        self.df_completo["Data da Venda"] = self.df_completo["Data da Venda"].fillna("Não fornecido")
        return self.df_completo   

    def load(self):
        self.df_completo.to_csv("data_processed/Dados_completos.csv", index=False)

    
if __name__ == "__main__":
    dados_json = Dados("raw/dados_empresaA.json", "json")
    dados_json.leitura_dados()

    dados_csv = Dados("raw/dados_empresaB.csv", "csv")
    dados_csv.leitura_dados()
    dados_csv.renomear()

    df_completo = Unificar(dados_json, dados_csv)
    df_completo.fusion()
    df_completo.load()
