from services import *
import streamlit as st
from utils2 import gerar_relatorio as gr

st.title("Análise de Série Temporal Financeira do IPEA")
codSerie = st.text_input("Digite o código da série IPEA (exemplo: 21634):")

if st.button("Gerar análise"):
    if not codSerie.strip():
        st.error("Informe o código da série.")
    else:
        try:
            dfSerie = obter_dados_serie(codSerie)
            if dfSerie.empty:
                st.error("Nenhum dado encontrado para o código informado.")
            else:
                st.subheader("Dados da série")

                graphSerie = plotar_grafico_periodo(codSerie, "Últimos 5 anos")
                st.plotly_chart(graphSerie)

                with st.spinner("Gerando análise..."):
                    response = gr(codSerie, dfSerie)

                st.write(response)

                with open(gerar_pdf(codSerie=codSerie, dfSerie=dfSerie, iaText=response), "rb") as file:
                    pdf_bytes = file.read()

                st.download_button(
                    label="Baixar PDF",
                    data=pdf_bytes,
                    file_name="relatorio.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"Erro ao buscar dados ou gerar análise: {e}")


