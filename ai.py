import google.generativeai as genai
import os
from constants import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_ai(topic):
    prompt = f'''
        Create a detailed roadmap for becoming or learning {topic} in 2024.
        Remember to keep it short and effective.
        Let the subheadings sizes be bigger than the actual content below it.
        Compulsorily make it into tables or interactive.
        Include the following:
        1. Essential Skills and Technologies.
        2. Learning Resources for FREE.
        3. Practical Projects.
        4. Certification Options.
        5. Salary Range in India.
    '''
    response = model.generate_content(prompt)
    return response


def generate_ai_for_topics(topic):
    prompt = f'''
        Create a detailed learning plan for learning {topic}.
        Remember to keep it very short and effective.
        Compulsorily make it into tables or other structures to make it more interactive.
        Include the following:
        1. Basic one line introduction.
        2. Learning Resources for FREE.
        3. Practical Projects.
    '''
    response = model.generate_content(prompt)
    return response

def generate_ai_for_headings(topic):
    prompt = f'''
        As a {topic}, provide a comprehensive list of 10 most essential technologies needed to learn to master {topic}. 
        Format the response as a comma-separated list beginner to advanced with no additional explanations or sentences.
        Don't use any other text like "examples", "libraries" etc, just the technologies, and also don't use any extra commas.
        The list should include technologies, frameworks, concepts, and best practices relevant to front-end engineering.
    '''
    response = model.generate_content(prompt)
    return response

def generate_ai_for_domains(topic):
    prompt = f'''
        As a {topic}, provide a comprehensive list of most famous roles in the field {topic}. 
        Format the response as a comma-separated list beginner to advanced with no additional explanations or sentences.
        Don't use any other text like "examples", "libraries" etc, just the roles, and also don't use any extra commas. 
        Include "Others" as the last value. Dont forget that.
    '''
    response = model.generate_content(prompt)
    return response

def extract_useful_content(response):
    content = response.candidates[0].content.parts[0].text
    # useful_content = content.split('\n*')
    # return [line.strip() for line in useful_content if line.strip()]
    return content
