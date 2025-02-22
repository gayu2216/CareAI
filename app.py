import streamlit as st
main = st.Page(
    "pages/0_main.py",
    title = "Mainpage",
)
alzheimers = st.Page(
    "pages/1_alzheimers.py",
    title = "alzheimers",
)
diabetes = st.Page(
    "pages/2_diabetes.py",
    title="diabetes",  
)
Heart_disease = st.Page(
    "pages/3_Heart_disease.py",
    title="Heart_disease",
)
Maternal = st.Page(
    "pages/4_Maternal.py",
    title="Maternal")

pg = st.navigation(pages=[main,alzheimers,diabetes,Heart_disease,Maternal])
pg.run()