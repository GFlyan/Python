from datetime import datetime, timedelta
import pandas as pd
import re
import ipeadatapy as ipea
from dateutil.relativedelta import relativedelta
from data.connect import supabase
from operacoes_bd import alterar_proxima_checagem, alterar_ultimo_alerta


def atualizar_datas(serie: dict):

    try:
        # Armazena a data de hoje
        hoje = datetime.today().date()

        # Armazena a data da próxima checagem a ser realizada
        proximaChecagem = datetime.strptime(serie["next_check"], "%Y-%m-%d").date()

        # Atualiza a data de proxima checagem
        if(serie["frequency"] == "Diária"):
            proximaChecagem = proximaChecagem + timedelta(days=1)
        elif(serie["frequency"] == "Mensal"):
            proximaChecagem = proximaChecagem + relativedelta(months=1)
        elif(serie["frequency"] == "Trimestral"):
            proximaChecagem = proximaChecagem + relativedelta(months=3)
        elif(serie["frequency"] == "Anual"):
            proximaChecagem = proximaChecagem + relativedelta(years=1)

        alterar_proxima_checagem(str(proximaChecagem), serie["idSerie"])

        #Atualiza a data de envio do último alerta
        alterar_ultimo_alerta(str(hoje), serie["idSerie"])

        print("Datas atualizadas!")

    except Exception as error:
        raise error


def calcular_margem(valorNovo: float, valorAnterior: float):
    margem = (((valorNovo - valorAnterior) / abs(valorAnterior)) * 100)
    return margem


def enviar_alerta(serie: dict, valorNovo: float, valorAnterior: float):
    if(serie["margin"] <= calcular_margem(valorNovo, valorAnterior)):
        pass
    else:
        pass



def verificar_atualizacao_series():
    series = supabase.table("series").select("*").execute()

    # Para cada serie na tabela series
    for serie in series.data:

        try:
            #Caso seja uma nova serie qual a última checagem é NULL, realiza o envio do alerta de imediato.
            if serie["last_alert"] is None:
                enviar_alerta(serie)

            else:

                # Armazena a data de hoje
                hoje = datetime.today().date()

                # Armazena a data do último alerta enviado
                ultimoAlerta = datetime.strptime(serie["last_alert"], "%Y-%m-%d").date()

                # Armazena a data da próxima checagem a ser realizada
                proximaChecagem = datetime.strptime(serie["next_check"], "%Y-%m-%d").date()

                # Caso a serie não tenha sido alertada hoje e a proxima checagem seja hoje ou antes
                if(ultimoAlerta != hoje and proximaChecagem <= hoje):

                        # Armazena o dataframe de atualizações da série de forma descendente
                        dfSerie = ipea.timeseries(serie["code_serie"]).iloc[::-1]

                        # Armazena a data de última atualização da série
                        ultimaAtualizacao = dfSerie.iloc[0]["RAW DATE"]
                        ultimaAtualizacao = re.sub(r"[a-zA-Z].*", "", ultimaAtualizacao)
                        ultimaAtualizacao = datetime.strptime(ultimaAtualizacao, "%Y-%m-%d").date()

                        # Realiza o envio de alerta caso a última atualização seja mais recente que o último alerta enviado
                        if(ultimaAtualizacao > ultimoAlerta):

                            # Armazena o valor da última e penúltima atualização no dataframe
                            valores = dfSerie.iloc[:, -1]
                            valorNovo = float(valores.iloc[0])
                            valorAnterior = float(valores.iloc[1])
                            enviar_alerta(serie, valorNovo, valorAnterior)
        except Exception as error:
                raise error
