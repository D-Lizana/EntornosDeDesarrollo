import streamlit as st

st.set_page_config(page_title="Reto 3 - Entornos de desarrollo", page_icon="R3", layout="wide")

st.title("Ciudades del mundo")
st.header("Imágenes y descripción")

columna1, columna2, columna3 = st.columns(3)
with columna1:
    st.image("https://toledoendulce.com/wp-content/uploads/2020/11/historia-toledo-i-1-1080x675.jpg", caption="Toledo")
    with st.expander("Toledo"):
        st.write("Antigua capital del Imperio Español.")

with columna2:
    st.image("https://imgs.search.brave.com/o4X-FKnq9pxUgFSEgsvz5_mPtpU7ZKg3MkKTgEwFYHA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly92aWFq/ZXMubmF0aW9uYWxn/ZW9ncmFwaGljLmNv/bS5lcy9tZWRpby8y/MDI1LzAzLzExL2J1/ZGFwZXN0XzhkODUy/NjVhXzEyODU3NjA5/NzFfMjUwMzExMTIy/MTA4XzEyODB4ODU0/LndlYnA", caption="Budapest")
    with st.expander("Budapest"):
        st.write("Maravilla del Imperio Austrohúngaro.")

with columna3:
    st.image("https://imgs.search.brave.com/ryHBEdme6tzDZW4O62My512iLZhrkcmQdGxku_gT8LQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/anJhaWxwYXNzLmNv/bS9ibG9nL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDE2LzEwL2tv/eWFzYW4tZGFuam9n/YXJhbi10ZW1wbGUu/anBn", caption="Koya")
    with st.expander("Koya"):
        st.write("Pueblo budista en los alto del monte Koya.")