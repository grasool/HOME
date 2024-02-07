
# This script is testing local llms using LM Studio and langchain_openai
# The text was copied from Dr. Andrew Ng's course on Coursera/DeepLearning.AI


from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(temperature=0.0, base_url="http://localhost:1234/v1", api_key="not-needed")


template_string = """Translate the text that is delimited by triple backticks \
into a style that is {style}. text: ```{text}``` """

new_style = """American English in a calm and respectful tone """

customer_email = """ Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help right now, matey! """

prompt_template = ChatPromptTemplate.from_template(template_string)


customer_messages = prompt_template.format_messages(
                    style=new_style,
                    text=customer_email)

print(customer_messages)

customer_response = chat(customer_messages)

print(customer_response.content)

