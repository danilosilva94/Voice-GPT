import openai
import os

# Set up your OpenAI API key
openai.api_key = ""

# Function to generate response from GPT-3
def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":"You are an assistant."},{'role': 'user', 'content': prompt}],
        max_tokens=1024,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    # Get the response text from the API response
    response_text = response['choices'][0]['message']['content']
    return response_text

# Main function to get input from user and return GPT-3 response
def main():
    while True:
        # Get input from user
        user_input = input("You: ")
        # If the user inputs "quit", exit the loop
        if user_input.lower() == "quit":
            break
        # Generate a response using GPT-3 and print it to the console
        response = generate_response(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()