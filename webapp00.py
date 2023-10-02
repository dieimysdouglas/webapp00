#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import base64

#DB
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTmRQ-zDdaMOmBGKo81-Qy4wwr-6Vz5uUf-Est1tGFhek1FP9LLl3kyN741OkRkTGFp-x-CReLewBKU/pub?gid=1591446506&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
dfD.columns = ['opiniao', 'resumo', 'idade']
st.dataframe(dfD) 
# eliminar as colunas com valores ausentes
summary = dfD.dropna(subset=['resumo'], axis=0)['resumo']
# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "ou", "os", "ser", "só"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1280, height=720).generate(all_summary)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('FabLabBackground.PNG')  

col1, col2, col3 = st.columns((1, 1, 1))
with col1:
    st.image('LOGO - FabLLab.JPG', width=150, output_format='auto')
with col2: 
    st.write(" ") 
with col3: 
    #st.subheader("Como está sendo a sua experiência no FabLab?")
    SUB_TITULO1 = '<p style="font-family:tahoma; color:black; font-size: 28px;">Como está sendo a sua experiência no FabLab?</p>'
    st.markdown(SUB_TITULO1, unsafe_allow_html=True)
  
# mostrar a imagem final
#fig, ax = plt.subplots(figsize=(10,6))
#ax.imshow(wordcloud, interpolation='bilinear')
#ax.set_axis_off()
plt.imshow(wordcloud);
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#st.pyplot()
wordcloud.to_file("NuvemPalavras.png")

st.pyplot() #Este método faz exibirt a nuvem de palavras
st.set_option('deprecation.showPyplotGlobalUse', False)

st.info(" Desenvolvido em Linguagem Python | Equipe FabLab/Programador: prof. Massaki de O. Igarashi")

SUB_TITULO = '<p style="font-family:tahoma; color:white; font-size: 14px;">CC BY-NC-SA - Esta licença permite que outros alterem, adaptem e criem a partir desta publicação para fins não comerciais, desde que atribuam aos criadores o devido crédito e que licenciem as novas criações sob termos idênticos.</p>'
st.markdown(SUB_TITULO, unsafe_allow_html=True)
