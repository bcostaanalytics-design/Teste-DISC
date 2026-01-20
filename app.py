import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Meu App IA", layout="centered")

# Título
st.title("🤖 Assistente da Minha Equipe")

# Configuração da Chave de API (Pega dos 'Segredos' do Streamlit)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Cria o modelo (ajuste o nome do modelo se necessário, ex: gemini-1.5-pro)
model = genai.GenerativeModel('gemini-1.5-flash')

# Caixa de texto para o usuário
user_input = st.text_area("Digite sua solicitação aqui:", height=150)

# Botão de enviar
if st.button("Gerar Resposta"):
    if not user_input:
        st.warning("Por favor, digite algo antes de enviar.")
    else:
        with st.spinner("A IA está pensando..."):
            try:
                # Envia para a IA
                response = model.generate_content(user_input)
                # Mostra o resultado
                st.write("### Resposta:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
