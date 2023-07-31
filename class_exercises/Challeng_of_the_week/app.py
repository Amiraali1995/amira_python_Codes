# app.py
#Flask = To create the web application and render HTML templates.
from flask import Flask, render_template, request
#Opeanai = The Python module for accessing the ChatGPT API
import openai
#Create the Flask app and set up the ChatGPT API key
#Initialize the Flask app
app = Flask(__name__)
#Set up your ChatGPT API key
openai.api_key = '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'
#Define the route for the index page
@app.route('/', methods=['GET', 'POST'])    #On a GET request, the user sees a blank input form, and chatbot_response is empty.
def chatbot():
#On a POST request (when the user submits the form), the user input is retrieved from the form using request.form['user_input']
    if request.method == 'POST':
        user_message = request.form['user_input']
        chatbot_response = generate_chatbot_response(user_message)
#The user input and chatbot response are then passed to the HTML template
        return render_template('index.html', user_input=user_message, chatbot_response=chatbot_response)
    else:
        return render_template('index.html', user_input='', chatbot_response='')
#function is called with the user input to generate a response from the ChatGPT API.
def generate_chatbot_response(user_message):
# Call the ChatGPT API to generate a response to the user's message
#method is used to make an API call.
    response = openai.Completion.create(
        engine="text-davinci-002", #parameter specifies which GPT-3 engine to use
        prompt=user_message,       #parameter is set to the user's input
        max_tokens=150             #parameter determines the maximum number of tokens in the response.
    )
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    app.run(debug=False)
