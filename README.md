## Hello World Generative Task using Hugging Face API

# Overview
This project demonstrates how to use the Hugging Face API to generate a creative "Hello, World!". 
The application sends a request to the Hugging Face API, which processes the input prompt and returns a generated message.

# Features
- Uses Hugging Face's GPT-2 model to generate creative text.
- Configurable parameters to adjust the output, such as temperature, top_k, and top_p.
- Simple and modular Python application.
- Can handle any number of prompts

# Prerequisites
Before running the application, ensure you have the following:
- Python 3 installed on your machine.
- Hugging Face API Token: You need a Hugging Face account and an API token for authentication.
- requests library: This Python library is used to make HTTP requests to the API.

# Setup
1. Obtain a Hugging Face API Token
    - Sign up for a Hugging Face account at Hugging Face.
    - After logging in, navigate to Settings → Tokens and create a new token.
    - Copy the generated token as you will need it to authenticate your requests.

2. Clone the Repository or Save the Code

3. Install Dependencies
Ensure you have the following libraries installed:
pip install requests
pip install huggingface_hub

4. Add your token:
    - Option 1: add it to your environment variables:
        - open Terminal in mac
        - Run: nano ~/.zshrc
        - add the following in the file: "export HF_API_TOKEN=<token>"
        - Run: source ~/.zshrc
        - make sure you restart your ide for changes to take affect
    - Option 2: paste it in the code directly (not recommended)
        - Feel free to use this option, if you are running locally
        - Do not post your token online
        - USE THIS OPTION IF OPTION 1 DID NOT WORK FOR TESTING PURPOSES

5. Run the code:
    - HCAIProj2.ipynb: is a jupyter notebook version that you can run (I prefer Visual Studio Code)
        - One of the outputs is already saved on the last executed run.
    - HCAIProj2.py: It is a python file that you can run from the command line: "python HCAIProj2.py"