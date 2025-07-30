from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Carrega os dados uma vez ao iniciar a API
df = pd.read_excel("baseficticiarubbycx.xlsx")

@app.get("/dados")
def consultar_dados(cpf: str = Query(..., description="Digite o CPF sem pontos ou traços")):
    resultado = df[df['CPF'].astype(str) == cpf]
    
    if resultado.empty:
        return {"erro": "CPF não encontrado"}
    
    dados = resultado[[
        'Consumo',
        'Geração',
        'Credito',
        'Fatura',
        'Saldo'
    ]].to_dict(orient="records")
    
    return {"cpf": cpf, "dados": dados}

