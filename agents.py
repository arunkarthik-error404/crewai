from textwrap import dedent
from crewai import Agent
from tools import Toolset
from langchain_openai import AzureChatOpenAI
import os
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()


llm = AzureChatOpenAI(
   openai_api_version="2024-02-01",
   azure_deployment="test",
   azure_endpoint="https://bits-interns.openai.azure.com/",
   api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
   model="gpt-4o",
   openai_api_type="azure"
)

llm=Ollama(model="llama3")
llm=ChatGroq(api_key="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",model="mixtral-8x7b-32768")

class FileAgents():
    def data_retrieval_agent(self):
        return Agent(
          role = "data retrieval specialist",
          goal = "Identify the filetype of the information provided and use the appropriate tool to obtain the data inside.",
          tools=[Toolset.PDF_tool,Toolset.CSV_tool, Toolset.XML_tool, Toolset.FileRead_tool],
          backstory = dedent("""\
              As a data retrieval specialist, your mission is to figure out the type of file given to you with perfect accuracy and select the appropriate tool to obtain the data.
              You are very careful in your ability to make the correct choice of tool and extract ALL the data correctly, without leaving out anything."""),
          verbose = True,
          llm=llm,
          #max_iter=3,
          allow_delegation=False
        )
    
    def data_converter_agent(self):
      return Agent(
        role='data converter',
        goal='Read the data passed to you and convert it into a .JSON format using the tool required.',
        tools=[Toolset.FileRead_tool],
        backstory=dedent("""\
            As a data conversion specialist, you must precisely convert ALL the data given into .JSON format, and take special care that NO data is left out.
            You are very proud of your ability to do this task with perfect precision and your 0 percent error rate."""),
        verbose=True,
        llm=llm,
        #max_iter=3,
        allow_delegation=False
      )