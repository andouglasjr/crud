import streamlit as st

import page.insert as insert

#criando a barra lateral do menu
st.sidebar.title('Menu')
page = st.sidebar.selectbox('Cliente',['Inserir', 'Consultar', 'Alterar','Deletar'])

if page=='Inserir':
    insert.inserir()


st.sidebar.markdown('PABD')
