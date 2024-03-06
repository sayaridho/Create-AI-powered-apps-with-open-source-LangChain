import os
from langchain_openai import ChatOpenAI
import gradio as gr
# Memasukkan API key
os.environ["OPENAI_API_KEY"] = "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"
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )
def chatbot(prompt):
    return gpt3.invoke(prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)