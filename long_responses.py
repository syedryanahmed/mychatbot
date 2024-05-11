import random

R_EATING = "I don't eat because I'm a bot!"
R_ADVICE = "The best advice I can give is to keep learning and exploring!"

def unknown():
    response = ["I'm not sure I understand.",
                "Could you please elaborate?",
                "Interesting, tell me more.",
                "I'm not programmed to answer that.",
                "I'm still learning. Can you ask another question?"]\
               [random.randrange(5)]
    return response
