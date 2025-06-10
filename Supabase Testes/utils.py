import re
from datetime import datetime

import ipeadatapy as ipea
import streamlit as st

from cronJob import verificar_atualizacao_series

codSerie = st.selectbox("Selecione", ipea.metadata(frequency="Diária"))
ultimaAtualizacao = ipea.timeseries(codSerie).iloc[::-1]
ultimaAtualizacao = ultimaAtualizacao.iloc[0]["RAW DATE"]
ultimaAtualizacao = re.sub(r"[a-zA-Z].*", "", ultimaAtualizacao)
ultimaAtualizacao = datetime.strptime(ultimaAtualizacao, "%Y-%m-%d").date()
ultimaAtualizacao
if st.button("Clique aqui"):
    verificar_atualizacao_series()