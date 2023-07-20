from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os


llm = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
def generate_restaurant_name_and_items(cuisine):
    # Chain 1:饭店名
    

    return {
        'restaurant_name': '同湘会',
        'menu_items': '臭鳜鱼， 小炒黄牛肉'
    }