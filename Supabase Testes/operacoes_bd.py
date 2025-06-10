import datetime

from reportlab.lib.validators import isNumber

from data.connect import supabase


def inserir_nova_serie(codeSerie: str, userEmail: str, frequency: str, margin: int):
    if codeSerie == "" or userEmail == "" or frequency == "" or isNumber(margin) == False:
        raise ValueError('Dados insuficientes.')

    try:
        # Tentativa de inserção
        resposta = (
            supabase.table("series")
            .insert({
                "code_serie": codeSerie,
                "user_email": userEmail,
                "frequency": frequency,
                "margin": margin,
                "last_check": str(datetime.datetime.today().date())
            })
            .execute()
        )

        return resposta.data  # Dados inseridos com sucesso

    except Exception as error:
        raise error

def alterar_proxima_checagem(proximaData: str, idSerie: str):
    if(proximaData == "" or idSerie == ""):
        raise ValueError('Dados insuficientes.')
    try:
        resposta = supabase.table("series").update({"next_check": proximaData}).eq("id", idSerie).execute()
        return resposta.data
    except Exception as error:
        raise error

def alterar_ultimo_alerta(data: str, idSerie: str):
    if (data == "" or idSerie == ""):
        raise ValueError('Dados insuficientes.')
    try:
        resposta = supabase.table("series").update({"last_alert": data}).eq("id", idSerie).execute()
        return resposta.data
    except Exception as error:
        raise error