# Recommendation Engine

## Overview
This project is a rule-based recommendation engine that suggests on job role, skills, experience level, and industry.

## Technologies Used
- Python
- Flask
- REST API

## How It Works
The system matches user input with assessment metadata and ranks results using weighted scoring logic.

## How to Run
1. Install dependencies: pip install flask
2. Run server: python app.py
3. Test endpoint:
   POST http://127.0.0.1:5000/recommend

## Sample Input
{
    "role": "Software Developer",
    "skills": ["Python"],
    "level": "Fresher",
    "industry": "IT"
}

## Sample Output
{
    "recommended_assessments": [
        "Python Coding Test",
        "Cognitive Ability Test"
    ]
}
