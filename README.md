# Resume Screener

## Project Overview
The Resume Screener is a tool designed to streamline the hiring process for recruiters by automatically screening resumes and providing rankings based on predefined criteria. It uses advanced algorithms to analyze candidate qualifications and match them with job descriptions, saving time and increasing the chances of finding the right candidate.

## Tech Stack
- **Programming Language:** Python
- **Web Framework:** Flask
- **Database:** PostgreSQL
- **Frontend:** React
- **Libraries:** scikit-learn for machine learning, SQLAlchemy for ORM, Jinja2 for templating

## Setup Instructions
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/lekieunhic1k56-collab/resume-screener.git
   cd resume-screener
   ```  
2. **Install dependencies:**  
   Make sure you have Python and pip installed. Then run:  
   ```bash
   pip install -r requirements.txt
   ```  
3. **Set up the database:**  
   Ensure that PostgreSQL is installed and run the following commands:  
   ```bash
   sudo -u postgres psql
   CREATE DATABASE resume_screener;
   CREATE USER yourusername WITH PASSWORD 'yourpassword';
   GRANT ALL PRIVILEGES ON DATABASE resume_screener TO yourusername;
   ```  
   Replace `yourusername` and `yourpassword` with your PostgreSQL credentials.
4. **Run the application:**  
   ```bash
   flask run
   ```  
   The application will start at `http://127.0.0.1:5000/`.

## Features
- Automated resume parsing and analysis
- Candidate ranking system based on qualifications
- User-friendly web interface
- Responsive design for accessibility on all devices
- Extensive search functionality to filter candidates
- Ability to export results and candidate data in various formats

---  
Designed for efficiency and effectiveness, the Resume Screener aims to enhance the hiring process for organizations of all sizes.  
