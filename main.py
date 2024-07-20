from dotenv import load_dotenv
from crewai import Crew
from tasks import ReadingTasks
from agents import FileAgents

def main():
    load_dotenv()
    print("File Reading Crew")
    print('-------------------------------')
    input_file = input("Input the file that needs to be read and converted.\n")

    tasks = ReadingTasks()
    agents = FileAgents()

    #create agents
    retrieval_agent = agents.data_retrieval_agent()
    converter_agent = agents.data_converter_agent()

    #create tasks
    reading_task = tasks.reading_task(retrieval_agent, input_file)
    conversion_task = tasks.data_conversion_task(converter_agent)

    #giving context
    conversion_task.context = [reading_task]

    crew = Crew(
      agents=[
        retrieval_agent,
        converter_agent
      ],
      tasks=[
        reading_task,
        conversion_task
      ]
    )

    result = crew.kickoff()
    print(result)
    
if __name__=="__main__":
    main()