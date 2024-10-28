from huggingface_hub import InferenceApi
import os
import requests
import random

# API configuration
token = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/gpt2"

# headers for authentication
headers = {
    "Authorization": f"Bearer {token}"
}

# List of prompts. Feel free to edit
prompts = ["Hello World, this is a test of the API. The response should be:", "How is your day?", "Is the Earth flat?"]

# Parameters to control text generation behavior
params = {
        "temperature": 0.35, #creativity controller
        "top_k": 50,
        "repetition_penalty": 1.2,
        "max_length": 50
    }


def generate_text(api_url, headers, data):
    """
    Send an API request (POST) to Hugging Gace API

    Args:
        api_url (str): The API URL for the model
        headers (dict): The headers for the API request
                including the authorization token
        data (dict): The data containing the prompt and 
                        params
    
    Returns:
        str: The generated text or the error message
    """

    try:
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()[0]['generated_text']

    except requests.exceptions.RequestException as e:
        print('Please verify that your token is getting passed in correctly.')
        return f'Error: {response.status_code} - {response.text}'



#calling the function on each prompt
for prompt in prompts:
    data = {
        "inputs": prompt,
        "parameters": params
    }

    result = generate_text(API_URL, headers, data)

    print(result, "\n")