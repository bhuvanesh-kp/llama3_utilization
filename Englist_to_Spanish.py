#translation app English to spanish
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


api_key = "" #enter API key


llm = ChatGroq(
    model='llama3-70b-8192',
    temperature=0.1,
    api_key=api_key
)


system_template = "Translate the following text input into {language}:"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_template),
        ("user","{text_input}")
    ]
)



parser = StrOutputParser()


chain = prompt | llm | parser

response  = chain.invoke({
    "language": "spanish",
    "text_input":"Hi my name is bhuvanesh"
})

print(response)