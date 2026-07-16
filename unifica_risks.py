import pandas as pd

df = pd.read_excel("nome_planilha.xlsx", sheet_name="nome_tabela", header=0)

# não altera
chave = [
    "nomes_colunas"
]

# junta tudo e concatena os campos que variam
grouped = (
    df.groupby(chave, dropna=False, sort=False)
    .agg(
        **{"Coluna 1": ("Coluna 1", lambda x: ", ".join(x.dropna().astype(str)))},
        **{"Coluna 2": ("Coluna 2", lambda x: ", ".join(x.dropna().astype(str)))},
    )
    .reset_index()
)

# reordena as colunas
result = grouped[[
    "nomes_colunas"
]]

result.to_excel("saida_consolidada_impact.xlsx", index=False)

#Validando os dados
print(f"Concluído: {len(result)} registros.")
print(f"Linhas originais: {len(df)}")
print(f"Grupos distintos: {df[chave].drop_duplicates().shape[0]}")
print(f"Linhas finais: {len(result)}")

# Verifica duplicados
duplicados = result[result.duplicated(subset=chave, keep=False)]
print(f"Duplicados após consolidação: {len(duplicados)}")

if len(result) == df[chave].drop_duplicates().shape[0]:
    print("Validação ok")
else:
    print("Encontrado erros")