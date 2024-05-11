# Conversational Bot with Learned Responses

This project implements a conversational bot in Python. The bot is capable of responding to user input with predefined responses as well as learned responses. It utilizes regular expressions and probabilistic matching to determine appropriate responses.

## Overview

The conversational bot is designed to engage in conversations with users. It comes with predefined responses for common greetings and goodbyes. Additionally, users can teach the bot new responses based on their feedback.

## How It Works

- **Predefined Responses**: The bot responds to common greetings and goodbyes with predefined responses stored in the `responses` dictionary.
- **Learned Responses**: Users can teach the bot new responses by providing feedback when the bot's response is not helpful. The bot then learns and stores these responses in a JSON file (`learned_responses.json`).
- **Matching Algorithm**: The bot uses a matching algorithm to determine the most appropriate response based on the user input and the predefined and learned responses.

## Usage

1. Run the `mychatbot.py` script using Python.
2. Enter your message when prompted by "You: ".
3. The bot will respond based on predefined responses or learned responses.
4. Provide feedback if the response was not helpful to teach the bot new responses.

## Contributing

Contributions to this project are welcome! If you have ideas for improving the bot or adding new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
