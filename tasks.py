from textwrap import dedent
from crewai import Task
json="/Users/siddarth.r/Desktop/Code/PDFParserBot/sample1.json"
class ReadingTasks():
    def reading_task(self,agent,input_file):
        return Task(
            description  = dedent(f"""\
                Read the given input file carefully, making use of the appropriate tool if required. 
                File: {input_file}"""),
            expected_output = dedent(f"""\
                A detailed report of ALL the data present in the file, in text format, without missing ANY data."""),
            agent = agent
        )
    
    def data_conversion_task(self, agent):
        return Task(
			description=dedent(f"""\
				Carefully read the given information, understand it completely and convert it to a .json format. 
				Information that needs to be converted will be passed as context by your coworker.
                Here is a sample .json file for you to understand how the output should be formatted: {json}. It can be read with the FileRead_tool."""),
			expected_output=dedent("""\
				A .json file that contains ALL of the information passed to you, making sure to not leave out anything. You can output the JSON file in the current folder."""),
			agent=agent
		)