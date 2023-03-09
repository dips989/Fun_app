import streamlit as st

st.title(":red[Deepa] :sunglasses:")
st.snow()

btn_click = st.button("Click me!!")

st.write(btn_click)

if btn_click == True:
    st.subheader("You Clicked me  :cry:")
    st.balloons()
