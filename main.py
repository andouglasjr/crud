import streamlit as st

import page.insert as insert
import page.select as select
import page.delete as delete
import page.update as update

st.header('Sistema CRUD Básico')
#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox = st.sidebar.selectbox('Ação', ['Inserir', 'Consultar','Deletar', 'Atualizar'])

if selectbox == 'Inserir':
    insert.inserir()

if selectbox == 'Consultar':
    select.consultar()

if selectbox == 'Deletar':
    delete.deletar()
    
if selectbox == 'Atualizar':
    update.alterar()