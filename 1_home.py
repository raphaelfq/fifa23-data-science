import streamlit as st
import pandas as pd
import webbrowser
import datetime

if "data" not in st.session_state:
  df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
  df_data = df_data[df_data["Contract Valid Until"] >= datetime.date.today().year]
  df_data = df_data[df_data["Value(£)"] > 0]
  df_data = df_data.sort_values(by="Overall", ascending=False)
  st.session_state["data"] = df_data

st.write("# FIFA 23 DATASET OFICIAL")
st.sidebar.markdown("Desenvolvido pelo Raphinha")

btn = st.button("Acesse os dados do Kaggle")
if btn: 
  webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/")

