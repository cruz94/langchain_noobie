from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools 

import os

load_dotenv()

def generate_name(product_type, purpose):
    llm = OpenAI(temperature=0.7)

    prompt_tempalte_name = PromptTemplate(
        input_variables = ['product_type','purpose'],
        template="Im building a {product_type} product, that does {purpose}, give 10 cool name for it."
    ) 

    name_chain = LLMChain(llm=llm, prompt=prompt_tempalte_name, output_key="name")
    response = name_chain({'product_type': product_type, 'purpose': purpose})
    
    # name = llm.invoke("Generate a unique name for a new AI product. give me 10 cool names")
    return response

def langchain_agent(): 
    llm = OpenAI(temperature=0.1)
    tools = load_tools(['wikipedia', 'llm-math'], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
    result = agent.invoke({
        "input": "Search Wikipedia for 'domestic cat average lifespan years'. Then use the calculator to multiply the average age by 2. Only use numbers in calculator."
        })
    print (result)


if __name__ == "__main__":
#    print(generate_name("B2B","warehouse management and that does oms as well"))
     print(langchain_agent())
