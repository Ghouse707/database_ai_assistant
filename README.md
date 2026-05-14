<img width="2702" height="1478" alt="Screenshot 2026-05-14 161036" src="https://github.com/user-attachments/assets/5cc24702-ccd5-4e14-8deb-e77f434dde17" />AI Database Assistant 
Overview

This project is an AI-powered SQL Database Assistant built using Python, Streamlit, SQLite, and Google Gemini API.
The application converts natural language questions into SQL queries using Gemini AI and retrieves data from the SQLite database automatically.

Features
Natural Language to SQL conversion
SQLite database integration
Google Gemini API integration
Streamlit interactive UI
Automatic query execution
Displays database results dynamically
Technologies Used
Python
Streamlit
SQLite
Google Gemini API
dotenv
Project Structure
ai_db_assistant/
│
├── app.py
├── sql.py
├── student.db
├── requirements.txt
├── .env
└── README.md
Installation
Clone Repository
git clone <your-github-repo-link>
cd ai_db_assistant
Create Virtual Environment
conda create -p venv python=3.10

Activate Environment

conda activate ./venv
Install Dependencies
pip install -r requirements.txt
Requirements.txt
streamlit
google-generativeai
python-dotenv
Setup API Key

Create a .env file and add:

GOOGLE_API_KEY=your_google_api_key

Get API Key from:

Google AI Studio

Run the Application
python -m streamlit run app.py
Example Queries
Show all students
How many students are present?
Show students with marks greater than 80
Give students name whose class is Web Development
Database Schema
STUDENT Table
Column	Type
NAME	VARCHAR(25)
CLASS	VARCHAR(25)
SECTION	VARCHAR(25)
MARKS	INT

Screenshots
Application Interface
<img width="2702" height="1478" alt="Screenshot 2026-05-14 161036" src="https://github.com/user-attachments/assets/357da374-bc83-4c7b-9a3b-1b84c4ce3085" />
<img width="2494" height="1364" alt="Screenshot 2026-05-14 160914" src="https://github.com/user-attachments/assets/9d410f68-22a9-4888-ba0a-33fc0c2471b1" />




Future Improvements
Multiple table support
Chat history
CSV upload support
Advanced SQL generation
Database visualization
LangChain integration


Author
Ghouse Pasha
