'''
Author: Edward Phiri Jr.
Date: 12/09/2024
'''
import openai
#import os
# Set your API key here
openai.api_key = 'your-api-key-here'

def get_gpt_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # You can also use gpt-4
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "What is the capital of Zambia?"
    response = get_gpt_response(prompt)
    print(f"Response: {response}")