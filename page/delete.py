# função para a página de deletar dados
# carregando as bibliotecas
import streamlit as st
# carregando as funções em outros arquivos .py
import controller.cliente as cliente

def deletar():  
    st.session_state.dele = False 
    st.title('Deletar Dados')

    delete_id = st.number_input(label='Insira o Id', format='%d', step=1)
    button_delete_select = st.button('Deletar')

    if button_delete_select:        
        try:
            data  = cliente.excluir(delete_id)
        except:
            st.error('Não foi possível deletar!')
        finally:        
            st.success('Cliente deletado com sucesso!!!')
            st.write(data)