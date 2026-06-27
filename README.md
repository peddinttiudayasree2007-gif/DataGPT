# DataGPT  

###### Intelligent LLM Agent for Database Interaction \& Visualization



###### **Overview**



DataGPT is an AI-powered conversational application that allows users to query databases using natural language. The system converts user questions into SQL queries, executes them on a SQLite database, and displays results with charts, explanations, ER diagrams, and dashboards.



###### **Features**



\- ChatGPT-like chat interface

\- Natural language to SQL

\- SQLite database integration

\- Database schema viewer

\- ER Diagram generation

\- Flowchart generation

\- Dashboard with charts

\- Pie Chart

\- Line Chart

\- CSV upload

\- CSV export

\- Query history

\- Data explanation

\- AI-ready architecture



###### **Technical Stack**

Backend:

\- FastAPI

\- Python



Frontend:

\- HTML

\- JavaScript

\- CSS



Database:

\- SQLite



Visualization:

\- Matplotlib

\- Chart.js



AI:

\- Google Gemini API (Optional)



###### **Installation**



```bash

git clone <repository-url>



cd backend



python -m venv venv



venv\\Scripts\\activate



pip install -r requirements.txt



uvicorn main:app --reload

```



Open:



```

http://127.0.0.1:8000

```



###### **Project Structure**



```

backend/

│

├── main.py

├── sql\_agent.py

├── chart\_tool.py

├── explain\_tool.py

├── diagram\_tool.py

├── schema\_tool.py

├── flowchart\_tool.py

├── history.py

├── dashboard.html

├── flowchart.html

├── index.html

├── database.db

└── requirements.txt

```



###### **PRESENTED BY**



PEDDINTI UDAYA SREE

DASI SAI CHARAN TEJA

EMANI LAKSHMI MEGHANA

