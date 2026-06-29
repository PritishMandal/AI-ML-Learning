# Logic:
# 1. Create User, Message and ChatRoom classes
# 2. Add methods for joining and leaving chatroom
# 3. Add method for sending messages
# 4. Display chat history

# Message class
class Message:

    # Message counter
    message_counter = 1

    # Constructor
    def __init__(self, sender, content):

        # Sender store kiya
        self.sender = sender

        # Message content store kiya
        self.content = content

        # Message id store ki
        self.id = Message.message_counter

        # Counter increase kiya
        Message.message_counter += 1

    # Message display method
    def __str__(self):

        return f"({self.id}) {self.sender.username}: {self.content}"


# User class
class User:

    # Constructor
    def __init__(self, username):

        # Username store kiya
        self.username = username

        # Chatroom initially none rakha
        self.chatroom = None

    # Join chatroom method
    def join_chatroom(self, chatroom):

        # Check kiya user already chatroom me hai ya nahi
        if self.chatroom:

            print(f"{self.username} is already in a chatroom.")

        else:

            # User add kiya
            chatroom.add_user(self)

            # Chatroom assign kiya
            self.chatroom = chatroom

            print(f"{self.username} joined {chatroom.name}")

    # Leave chatroom method
    def leave_chatroom(self):

        # Check kiya user kisi chatroom me hai ya nahi
        if not self.chatroom:

            print(f"{self.username} is not in any chatroom.")

        else:

            # User remove kiya
            self.chatroom.remove_user(self)

            print(f"{self.username} left {self.chatroom.name}")

            # Chatroom none kiya
            self.chatroom = None

    # Message send method
    def send_message(self, content):

        # Check kiya user chatroom me hai ya nahi
        if not self.chatroom:

            print(f"{self.username} cannot send message.")

        else:

            # Message broadcast kiya
            self.chatroom.broadcast(self, content)


# ChatRoom class
class ChatRoom:

    # Constructor
    def __init__(self, name):

        # Chatroom name store kiya
        self.name = name

        # Empty users list
        self.users = []

        # Empty messages list
        self.messages = []

    # User add method
    def add_user(self, user):

        # User list me add kiya
        self.users.append(user)

    # User remove method
    def remove_user(self, user):

        # User list se remove kiya
        self.users.remove(user)

    # Message broadcast method
    def broadcast(self, sender, content):

        # Message object create kiya
        message = Message(sender, content)

        # Message list me add kiya
        self.messages.append(message)

        # Message print kiya
        print(message)

    # Chat history method
    def show_chat_history(self):

        print("\nChat History:")

        # Loop lagaya
        for msg in self.messages:

            print(msg)


# Chatroom object create kiya
room = ChatRoom("Python Lounge")

# User objects create kiye
u1 = User("Alice")
u2 = User("Bob")
u3 = User("Charlie")

# Users join kiye
u1.join_chatroom(room)
u2.join_chatroom(room)

# Messages send kiye
u1.send_message("Hello everyone!")
u2.send_message("Hi Alice!")

# User join kiya
u3.join_chatroom(room)

# Message send kiya
u3.send_message("Hey guys, what's up?")

# Chat history show ki
room.show_chat_history()

# Users leave kiye
u1.leave_chatroom()
u2.leave_chatroom()
u3.leave_chatroom()


# Q10: Create a Chat System using User, Message and ChatRoom classes with sending messages and chat history features