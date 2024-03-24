import gradio as gr
import cohere
import os
from dotenv import load_dotenv, find_dotenv

# load the .env file
_ = load_dotenv(find_dotenv()) # read local .env file
cohere_api_key = os.environ['COHERE_API']
co = cohere.Client(cohere_api_key)


def generate_data(data_src):

    command_prompt= f'''This is a sample dataset in csv below, and I want you to help me generate more data in csv format with different variations (at least 100 examples).

    ```csv
    {data_src}
    ```'''

    response = co.generate(
                  model='command',
                  prompt=command_prompt,
                  max_tokens=260,
                  temperature=0.9,
                  k=0,
                  stop_sequences=[],
                  return_likelihoods='NONE')
    
    data_text = response.generations[0].text

    return data_text


data_example = '''QUERY_TEXT,POSITIVE,NEGATIVE
desserts, shakes,veggie burger with cheeese
sushi, thai chef fresh rolls, meat lasagna
acai bowl, acai bowl delivered, mint chocolate chip polar pizza
cupcake, carrot, buffalo chicken'''


demo = gr.Interface(fn=generate_data,
                    inputs=[gr.Textbox(label="Paste your sample data here", lines=3)],
                    outputs=[gr.Textbox(label="Data Generated Here", lines=5)],
                    title="Data Generator with Cohere",
                    description="Generating new dataset using the Cohere API under the hood!",
                    allow_flagging="never",
                    #Here we introduce a new tag, examples, easy to use examples for your application
                    examples=[data_example])
demo.launch()