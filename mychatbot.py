import re
import random
import long_responses as long
import json

responses = {
    'hello_responses': ['Hello, human.', 'Hi there!', 'Hey, how are you?', 'Greetings!'],
    'goodbye_responses': ['Goodbye, human.', 'Farewell!', 'See you later.'],
    # Add more responses as needed
}

# File to store learned responses
LEARNED_RESPONSES_FILE = "learned_responses.json"

# Placeholder for learned responses
learned_responses = {}

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses based on keywords
    response(random.choice(responses['hello_responses']), ['hello', 'hi', 'hey', 'sup', 'heyo', 'morning', 'afternoon', 'evening'], single_response=True)
    response(random.choice(responses['goodbye_responses']), ['bye', 'goodbye'], single_response=True)

    # Add more responses here based on the structure of your bot's conversations

    # Include learned responses
    for response_text, _ in learned_responses.items():
        response(response_text, learned_responses[response_text]['keywords'], learned_responses[response_text]['single_response'], learned_responses[response_text]['required_words'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return best_match if highest_prob_list[best_match] > 0 else long.unknown()

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def learn_response(user_input, bot_response):
    # Ask user for additional information
    keywords = input("What are the keywords for this response? (comma-separated): ").lower().split(',')
    single_response = input("Is this a single-response answer? (yes/no): ").lower() == 'yes'
    required_words = input("Are there any required words? (comma-separated, leave blank if none): ").lower().split(',')

    # Store learned response
    learned_responses[bot_response] = {
        'keywords': [word.strip() for word in keywords],
        'single_response': single_response,
        'required_words': [word.strip() for word in required_words if word.strip()]
    }

def load_learned_responses():
    try:
        with open(LEARNED_RESPONSES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_learned_responses():
    with open(LEARNED_RESPONSES_FILE, 'w') as file:
        json.dump(learned_responses, file)

# Load learned responses when the bot starts
learned_responses = load_learned_responses()

while True:
    user_input = input('You: ')
    bot_response = get_response(user_input)
    if bot_response:
        print('Bot:', bot_response)
        # Ask user if the response was helpful and learn if necessary
        user_feedback = input("Was my response helpful? (yes/no): ").lower()
        if user_feedback == "no":
            new_response = input("What would be a better response?: ")
            learn_response(user_input, new_response)
            # Save learned responses
            save_learned_responses()
    else:
        print('Bot:', long.unknown())
