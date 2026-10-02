import streamlit as st

st.title("first streamlit application")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("Streamlit is an open source python library")

agree = st.checkbox("I agree with Bhavesh")

if agree:
    st.write("Great!")

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"]
    
)

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")


num1 = st.number_input("Enter a number")
num2 = st.number_input("Enter another number")

print("The sum of two numbers is:", num1+num2)

if st.button("Add"):
    st.write("The sum of two numbers is:", num1+num2)



