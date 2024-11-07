import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool, BaseTool
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub


def lookup(name:str) -> str:
    """
    Function for returning the linkedin url page of the person given as name in the parameter
    """
     

    
