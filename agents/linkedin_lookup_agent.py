import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool, BaseTool
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub


#Notes:
    #Output indicator: Output parser
    #Tools:
        #name
        #func
        #description

#react_prompt: tools, tool_names, agent_scratchpad
    # Answer the following questions as best you can. You have access to the following tools:

    # - `calculator`: useful for mathematical calculations.
    # - `search_engine`: helpful for finding information on the internet.
    # - `database_query`: retrieves data from a specific database.

    # Use the following format:

    # Question: the input question you must answer
    # Thought: you should always think about what to do
    # Action: the action to take, should be one of [calculator, search_engine, database_query]
    # Action Input: the input to the action
    # Observation: the result of the action
    # ... (this Thought/Action/Action Input/Observation can repeat N times)
    # Thought: I now know the final answer
    # Final Answer: the final answer to the original input question

    # Begin!

    # Question: {input}
    # Thought: I need to determine the sum of 123 and 456.
    # Action: calculator
    # Action Input: 123 + 456
    # Observation: 579
    # Thought: I now know the sum is 579.
    # Final Answer: 579

def lookup(name:str) -> str:
    """
    Function for returning the linkedin url page of the person given as name in the parameter
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )

    #prompte template followed by output indicator specifying the output format
    template = "Given the full name {name_of_person} of a person, search and return the url of his or her linkedin profile page, your answer should only contain the url and nothing else"


    #the actual prompt template to be used
    prompt_template = PromptTemplate(template=template,input_variables=["name_of_person"])


    #object holding all the tools for the agent to use performing tasks
    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin profile page",
            func="?",
            description="useful when asked of linkedin profile page given the name of the person we are looking up for"
        )
    ]


    #pulling the ReAct prompt from hub
    react_prompt = hub.pull("hwchase17/react")


    #defining the agent
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )


    agent_executor = AgentExecutor(agent=agent,
                                   tools=tools_for_agent,
                                   verbose=True)
    

    #Here we are passing in the input and populate the prompt from the template
    result = agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )


    return result["output"]
 






if __name__ == "__main__":
    lookup("Elon Musk")






    







     

    
