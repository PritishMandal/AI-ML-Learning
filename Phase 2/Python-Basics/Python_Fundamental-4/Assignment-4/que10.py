# Logic:
# 1. Create User, Message and ChatRoom classes
# 2. Add methods for joining and leaving chatroom
# 3. Add method for sending messages
# 4. Display chat history 

# User class
class User:

    # Constructor
    def __init__(self, name):

        # User name store kiya
        self.name = name


# Message class
class Message:

    # Constructor
    def __init__(self, sender, text):

        # Sender aur text store kiya
        self.sender = sender
        self.text = text

    # Message display method
    def display_message(self):

        print(self.sender.name + ":", self.text)


# ChatRoom class
class ChatRoom:

    # Constructor
    def __init__(self):

        # Empty lists banayi
        self.users = []
        self.messages = []

    # User join method
    def join_user(self, user):

        # User add kiya
        self.users.append(user)

        print(user.name, "joined the chatroom")

    # User leave method
    def leave_user(self, user):

        # User remove kiya
        self.users.remove(user)

        print(user.name, "left the chatroom")

    # Message send method
    def send_message(self, message):

        # Message list me add kiya
        self.messages.append(message)

    # Chat history method
    def show_chat_history(self):

        print("Chat History:")

        # Loop lagaya
        for msg in self.messages:

            msg.display_message()


# Objects create kiye
u1 = User("Shanku")
u2 = User("Pitu")

# ChatRoom object
chat = ChatRoom()

# Users join kiye
chat.join_user(u1)
chat.join_user(u2)

# Messages create kiye
m1 = Message(u1, "Hello")
m2 = Message(u2, "Hi nenenene ")

# Messages send kiye
chat.send_message(m1)
chat.send_message(m2)

# Chat history display ki
chat.show_chat_history()

# User leave_user method call kiya
chat.leave_user(u2)


# Q10: Create an OOP Chat System using User, Message and ChatRoom classes