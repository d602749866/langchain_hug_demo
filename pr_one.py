from langchain import PromptTemplate
# from langchain.llms import OpenAI
from langchain import HuggingFaceHub, LLMChain
from dotenv import load_dotenv
import os;

load_dotenv()
hub_llm = HuggingFaceHub(repo_id="mrm8488/t5-base-finetuned-wikisQL")
prompt = PromptTemplate(
    input_variables=["question"],
    template="Translate English to SQL: {question}"
)
hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
print(hub_chain.run("what is the average age of the respondents using a mobile device?"))

FileNotFoundError






# template = """Question: {question}
# Answer: """
# prompt = PromptTemplate(
#     template=template,
#     input_variables=['question']
# )

# # user question
# question = "when the Google build?"

# from langchain import HuggingFaceHub, LLMChain

# # initialize Hub LLM
# hub_llm = HuggingFaceHub(
#     repo_id='google/flan-t5-large',
#     model_kwargs={'temperature': 0},
#     huggingfacehub_api_token='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'
# )

# # create prompt template > LLM chain
# llm_chain = LLMChain(
#     prompt=prompt,
#     llm=hub_llm
# )

# # ask the user question about the capital of France
# print(llm_chain.run(question))