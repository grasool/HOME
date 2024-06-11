
import time
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

# Setup Model
llm_model = "llama3"
chat = Ollama(model=llm_model, temperature=0.0)

# Setup prompt template
template_string = """You are a helpful assistant. \
        Answer this question: {question}. """
prompt_template = ChatPromptTemplate.from_template(template_string)


# Build prompt
my_question = "Where is Moffitt Cancer Center?"
llm_input_prompt_string = prompt_template.format_messages(question=my_question)

print(llm_input_prompt_string)

# Start timing
start_time = time.time()

# Run model
llm_answer = chat.invoke(llm_input_prompt_string)

# End timing
end_time = time.time()

# Print answer
print(llm_answer)

# Calculate and print execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
