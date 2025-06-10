import re
from datetime import datetime

import streamlit as st
import pandas as pd
import ipeadatapy as ipea

codSerie = st.selectbox("Selecione", ipea.metadata())
# df = ipea.timeseries(codSerie).iloc[:, -1]
# df = df.iloc[::-1]
# atualizacaoNova = float(df.iloc[0])
# atualizacaoAnterior = float(df.iloc[1])
# margem = (((atualizacaoNova-atualizacaoAnterior)/abs(atualizacaoAnterior))*100)
# f"Valor atual: {atualizacaoNova:.2f}"
# f"Valor anterior: {atualizacaoAnterior:.2f}"
# f"{'Subiu' if margem > 0 else 'Desceu'} {margem:.2f}%"


df = ipea.timeseries(codSerie).iloc[::-1]

# Armazena a data de última atualização da série
ultimaAtualizacao = df.iloc[0]["RAW DATE"]
ultimaAtualizacao = re.sub(r"[a-zA-Z].*", "", ultimaAtualizacao)
ultimaAtualizacao = datetime.strptime(ultimaAtualizacao, "%Y-%m-%d").date()
ultimaAtualizacao
valores = df.iloc[:, -1]
f"Valor atual: {atualizacaoNova:.2f}"
f"Valor anterior: {atualizacaoAnterior:.2f}"
f"{'Subiu' if margem > 0 else 'Desceu'} {margem:.2f}%"

