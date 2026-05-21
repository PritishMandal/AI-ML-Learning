# Logic:
# 1. Create Book class
# 2. Store title, author and reviews
# 3. Create methods to add and display reviews
# 4. Create object and call methods

class Book:

    # Constructor
    def __init__(self, title, author):

        # Book details store ki
        self.title = title
        self.author = author
        self.reviews = []

    # Review add method
    def add_review(self, review):

        # Review list me add kiya
        self.reviews.append(review)

    # Total reviews count method
    def count_reviews(self):

        print("Total Reviews =", len(self.reviews))#len() tabhi use karte hai jab hume kisi list ke total items count karne ho

    # Display reviews method
    def display_reviews(self):

        print("Book Reviews:")

        # Loop lagaya
        for review in self.reviews:
            print(review)


# Object create kiya
b1 = Book("Python Basics", "Pritish")

# Methods call kiye
b1.add_review("Very Good Book")
b1.add_review("Easy to Understand")

b1.count_reviews()
b1.display_reviews()


# Q2:
# Create a class Book with attributes:
# title, author and list of reviews
# Add methods to add review, count reviews and display reviews