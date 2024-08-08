from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool

llm= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose= True,
    temperature= 0.5,
    google_api_key= os.getenv("GOOGLE_API_KEY")
)

#research agent
researcher= Agent(
    role= "Senior Researcher",
    goal= "Discover application layer uses of {topic}",
    verbose= True,
    memory= True,
    backstory= (
        "A curious and ever learning individual who is always"
        "seeking knowledge about how things get executed in real world"
        "and how tools and technologies are leveraged to achieve state of the art results"
        "in various industries. Always ready to go in depth and discover"
        "pros and cons of application side of a technology in different domains"
        "and uncovers new insights"
    ),
    tools=[],
    llm= llm,
    allow_delegation=True
)

#content planner to plan and write content in a standard layout
writer = Agent(
    role='Writer',
    goal='Create a well-detailed and insightful report about application layer uses of {topic}',
    verbose=True,
    memory=True,
    backstory=(
        'A dedicated and experienced writer who has been crafting content'
        'for various publications and platforms for over a decade'
        'with a keen eye for detail and a strong understanding of the technical landscape'
    ),
    tools=[tool],
    llm=llm,
    allow_delegation= False
)

#content editor to edit and refine the written content
editor= Agent(
    role='Content Editor',
    goal= 'Edit and refine the written content to improve clarity, conciseness, and accuracy',
    verbose= True,
    memory= True,
    backstory= (
        'A skilled and experienced content editor who has worked in various'
        'content creation and editing roles for over a decade'
        'with a strong focus on ensuring the quality and relevance of the content'

    ),
    tools=[],
    llm= llm,
    allow_delegation=False
)



