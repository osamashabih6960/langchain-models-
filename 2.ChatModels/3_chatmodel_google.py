# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# result = model.invoke('What is the capital of India')

# print(result.content)


import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

genai.configure(api_key="AIzaSyANcY-CNPQ37mgXjVVgps4jaKSJkPuNy5c")


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # v1 models
result = model.invoke("What is the capital of India?")
print(result)