#  Agentic system for creating research article with crewAI

This system leverages an agentic flow for creating a research article based on application layer usecases of Generative AI. Agents are based on Google's 
`gemini-1.5-flash` model.

It comprises of three instances of `Agent` - `researcher`, `writer` and `editor` to plan, write and proofread the article content
and perform relevant research and collaboratively work in a sequential process (https://docs.crewai.com/how-to/Sequential), interdependently.

##Project Structure
- Agents are defined in `agents.py`. The workflow utilizes three agents as mentioned above.
- Tasks for each of the agents are defined in `tasks.py`. As a final output, at the end of the chain,
system will output a final research article in `new_post.txt` 
- Crew execution happens in `crew.py` file. 
- Agents utilize <b>SERPER API</b> to perform web-search queries to assist assigned actions.


## Setup and Installation

To set up and run the project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/AdityaAshutosh/Multi-Agent-System
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your `GOOGLE_API_KEY` for using Google Gemini and
   `SERPER_API_KEY` for using Google Search queries.
   
4. Run `crew.py` using `python crew.py` and the results will be stored in a text file `new-post.txt`.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
