"""
Este script em Python realiza a consolidação de linhas duplicadas em uma planilha Excel utilizando a biblioteca Pandas. 
Ele agrupa a tabela com base em uma coluna de referência (Control Description) e, para todas as outras colunas, 
concatena os valores preenchidos em uma única célula de texto, eliminando duplicados internos e preservando a ordem original.
O script também conta com uma etapa robusta de validação ao final para garantir 
que nenhum dado foi perdido ou corrompido durante o processo de agrupamento.

"""


import pandas as pd

df = pd.read_excel(
    "nome_planilha.xlsx",
    sheet_name="nome_tabela",
    header=0
)

# Coluna de referência
chave = ["nome_coluna_referencia"]

# Todas as outras colunas serão agrupadas
colunas_agrupar = [col for col in df.columns if col not in chave]

# Função para concatenar valores únicos preservando a ordem
def concat_unicos(x):
    return ", ".join(pd.unique(x.dropna().astype(str)))

# Cria o dicionário de agregação automaticamente
agg_dict = {col: (col, concat_unicos) for col in colunas_agrupar}

grouped = (
    df.groupby(chave, dropna=False, sort=False)
      .agg(**agg_dict)
      .reset_index()
)

result = grouped

result.to_excel("saida_consolidada_impact.xlsx", index=False)

print(f"Concluído: {len(result)} registros.")
print(f"Linhas originais: {len(df)}")
print(f"Grupos distintos: {df[chave].drop_duplicates().shape[0]}")
print(f"Linhas finais: {len(result)}")

# Verifica duplicados
duplicados = result[result.duplicated(subset=chave, keep=False)]
print(f"Duplicados após consolidação: {len(duplicados)}")

# Validação colunas agrupadas
for coluna in colunas_agrupar:
    orig = sorted(df[coluna].dropna().astype(str).tolist())
    novo = sorted(
        result[coluna]
        .str.split(", ")
        .explode()
        .dropna()
        .astype(str)
        .tolist()
    )
    print(f"{coluna}: {orig == novo}")

if (
    len(result) == df[chave].drop_duplicates().shape[0]
    and len(duplicados) == 0
):
    print("Validação OK")
else:
    print("Dados incorretos")