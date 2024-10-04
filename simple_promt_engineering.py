import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


load_dotenv()  # Load the environment

information = """Virat Kohli (Hindi pronunciation: [ʋɪˈɾɑːʈ ˈkoːɦli] ⓘ; born 5 November 1988) is an Indian international cricketer who plays Test and ODI cricket for the Indian national team. A former captain in all formats of the game, Kohli retired from the T20I format following India's win at the 2024 T20 World Cup. He's a right-handed batsman and an occasional unorthodox right arm medium bowler. Kohli is regarded as one of the greatest batsmen of all time and the greatest in the modern era. He holds the highest IPL run-scorer record, ranks third in T20I, third in ODI, and stands the fourth-highest in international cricket.[4] He also holds the record for scoring the most centuries in ODI cricket and is second in the list of most international centuries scored.

Kohli was a key member of the Indian team that won the 2011 Cricket World Cup, 2013 Champions Trophy"""


if __name__ == "__main__":

    summary_template = """
        On given information {information} about a person, create:
        1. a short summary 
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")    #temperature defines the creativity in the responses, 0 represents no creativity

    # llm =  ChatOllama(model="llama3")   # using  llama3 MOdel

    llm = ChatOllama(model="mistral")  # using  mistral MOdel

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)
