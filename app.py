import streamlit as st 
st.write("Hello World :fire:")
st.balloons()
st.snow()

option = st.selectbox(
    'Comment souhaitez-vous être contacté?',
    ('E-mail', 'Téléphone fixe', 'Téléphone mobile')
)
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")