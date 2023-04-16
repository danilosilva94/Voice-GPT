import openai

# Set up your OpenAI API key
openai.api_key = ""

# List to store conversation history
conversation_history = []

# Function to generate response from GPT-3
def generate_response(prompt):
    try:
        # Add the prompt to the conversation history
        conversation_history.append({'role': 'user', 'content': prompt})
        
        # Call the OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=1024,
            n=1,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        
        # Get the response text from the API response
        response_text = response['choices'][0]['message']['content']
        
        # Add the response to the conversation history
        conversation_history.append({'role': 'assistant', 'content': response_text})
        
        return response_text
    
    except openai.error.InvalidRequestError as e:
        print(f"Error: {e.message}")
