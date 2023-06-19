import streamlit as st

import page.insert as insert
import page.select as select

#criando a barra lateral do menu
st.sidebar.title('Menu')
bt_menu_insert = st.sidebar.button('Inserir', 'insert_menu')
bt_menu_select = st.sidebar.button('Consultar', 'select_menu')

if bt_menu_insert:
    insert.inserir()

if bt_menu_select:
    select.consultar()