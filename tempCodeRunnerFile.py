from transformers import pipeline, Conversation

# Initialize a conversational pipeline
chatbot = pipeline('conversational', model='facebook/blenderbot-400M-distill')

# Create a Conversation object with the user input
conversation = Conversation("How are you?")

# Get the response
response = chatbot([conversation])

# Print the response text
print(type(response))