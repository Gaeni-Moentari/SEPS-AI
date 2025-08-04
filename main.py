from AI_Component.Crew import *
from AI_Component.validator.validator import *
import Component.Logo as Img
import streamlit as st

Img.image(["./Image/gema.png", "./Image/SEAQIS.png", "./Image/SEPS.png", "./Image/PENS.png"])
st.title("AI Informasi SEAMEO SEPS")
st.write("This is first AI SEAMEO SEPS model. Prepared by GEMA foundation")
st.write("Official Site SEAMEO SEPS - https://www.seameoseps.org ")
st.write("Koordinator Gatot HP - www.gaeni.org ")

#input
col1, col2 = st.columns(2)

with col1:
    input = st.text_input("Masukkan pertanyaan ")
with col2:
    lang = st.selectbox("Language", ["English", "Indonesia"])

submit = st.button("Mulai Pencarian")

if submit:
    # Validasi pertanyaan
    if fisheries_validator(input):
        # Jika valid, lanjutkan ke proses utama
        result = KokoaCrew(input, lang).generalCrew().kickoff()
        st.markdown(result)
    else:
        # Jika tidak valid, tampilkan pesan kesalahan
        st.error("Pertanyaan Anda tidak berkaitan dengan topik SEAMEO SEPS. Silakan ajukan pertanyaan yang relevan.")