import streamlit as st
from shape import Circle, Rectangle

def GetInputs():
    shape_type = st.selectbox("Select shape", ["Circle", "Rectangle"])
    
    if shape_type == "Circle":
        radius = st.number_input("Enter radius", min_value=0.0, format="%.2f")
        shape = Circle(radius)
    else:
        length = st.number_input("Enter length", min_value=0.0, format="%.2f") 
        width = st.number_input("Enter width", min_value=0.0, format="%.2f")
        shape = Rectangle(length, width)
        
    if shape.GetArea() > 0:
        st.success(f"The area of the {shape_type} is {shape.GetArea():.2f}")

if __name__ == "__main__":
    st.set_page_config(page_title="App to calculate area", layout="centered")
    GetInputs()