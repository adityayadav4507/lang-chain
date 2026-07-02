import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv



load_dotenv()

model=GoogleGenerativeAI(model="gemini-2.5-flash")

st.header("research assistant")

user_input=st.selectbox("select the research paper topic", ["Artificial Intelligence","Machine Learning","Natural Language Processing","Computer Vision","Robotics"])
style=st.selectbox("Select your style",["Formal","Informal","Humorous","Professional"])
length=st.slider("Select the length of the response",min_value=50,max_value=500,value=200,step=10)

template=load_prompt("template.json")

if st.button("Generate Response"):
    chain = template|model
    result=chain.invoke({"paper_input":user_input,"style_input":style,"length_input":length})
    st.write(result)

