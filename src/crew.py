from crewai import Crew, Process
from agents import researcher, writer, editor
from tasks import research_task, write_task, editor_task

#Form a tech focused crew with enhanced configuration
crew= Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, editor_task],
    process= Process.sequential,

)

# starting execution process
result= crew.kickoff(inputs= {'topic': 'Generative AI'} )
print(result)