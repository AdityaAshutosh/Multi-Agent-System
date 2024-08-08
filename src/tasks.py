from crewai import Task
from tools import tool
from agents import researcher, writer, editor

# Researcher's task
research_task = Task(
    description=(
        "Identify the application layer uses of {topic}"
        "Focus on figuring out the pros and cons and articulate key aspects"
        "Your final report should be detailed, insightful and aligned with market"
        "trends, opportunities and potential risks"
    ),
    expected_output= 'A comprehensive 3 paragraph long report on application layer uses of {topic}',
    tools= [tool],
    agent= researcher
)

write_task= Task(
    description=(
        "Write a persuasive and insightful article on application layer uses of {topic}"
        "Your article should be informative, engaging and easy to read"
        "Your article should be structured in a clear and concise manner"
        "Your article should be well researched and backed up with credible sources"
    ),
    expected_output= 'A 4 paragraph article on the application layer uses of {topic} in text format',
    tools= [tool],
    agent= writer,
    async_execution= False,
    output_file= 'new_post.txt'
)

editor_task= Task(
    description=(
        "Edit the previously written article to improve readability, clarity, and focus on the key aspects"
        "Your edited article should be well researched and backed up with credible sources"
    ),
    expected_output= 'An edited 4 paragraph article on the application layer uses of {topic}',
    tools= [tool],
    agent= editor,
    async_execution= False,
    input_file= 'new_post.txt'
)

