import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Hey|hey|Hi|hi|hello|Hello",
        ["Hello there,how can I help","Hey","Hi","Welcome"]
    ],
    [
        r'(.*) (hungry|sleepy)',
        ["%1 %2"]
    ],
    [
        r"quit",
        ["Bye Bye it was Nice meeting  you"]
    ]
]




def chatty():
    print("Hey I'm your navigator\ntype quit to leave")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()