# =================================================
#             LIBRARY MANAGEMENT SYSTEM            
# =================================================

class Library:

    def __init__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price

    def show_records(self):
        print("\n==================== BOOK DETAILS ===================")
        print("Book Name:", self.book_name)
        print("Author Name:", self.author_name)
        print("Price:", self.price)
        print()

    def issue_book(self):
        print(self.book_name, "book has been issued for ₹", self.price)

    def return_book(self):
        print("The book must be returned within 1 month of the issue date")


book1 = Library("The Indian Struggle", "Subhas Chandra Bose", 299)
book2 = Library("Cricket My Style", "Kapil Dev", 499)

book1.show_records()
book1.issue_book()
book1.return_book()

book2.show_records()
book2.issue_book()
book2.return_book()



# =================================================
#                 FOOD DELIVERY APP                
# =================================================

class Food:

    def __init__(self, food_name, price, rating):
        self.food_name = food_name
        self.price = price
        self.rating = rating

    def show_details(self):
        print("\n==================== FOOD DELIVERY DETAILS ====================")
        print("Food Name:", self.food_name)
        print("Price:", self.price)
        print("Rating:", self.rating)
        print()

    def place_order(self):
        print(self.food_name, "is placed for order")

    def cancel_order(self):
        print("If you want to cancel order do it within 5 minutes of order placed")


food1 = Food("Biryani", 399, 4.5)
food2 = Food("Pizza", 199, 4.2)
food3 = Food("Momos", 249, 4.7)

food1.show_details()
food1.place_order()
food1.cancel_order()

food2.show_details()
food2.place_order()
food2.cancel_order()

food3.show_details()
food3.place_order()
food3.cancel_order()



# =================================================
#            MOVIE TICKET BOOKING SYSTEM           
# =================================================

class Movie: 

    def __init__(self, movie_name, ticket_price, timing):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.timing = timing

    def show_details(self):
        print("\n==================== MOVIE TICKET DETAILS ====================")
        print("Movie Name:", self.movie_name)
        print("Ticket Price:", self.ticket_price)
        print("Timing:", self.timing)
        print()

    def book_ticket(self):
        print(self.movie_name, "movie ticket is booked")

    def cancel_ticket(self):
        print("If you want to cancel ticket please cancel it before 1 hour of movie timing")


movie1 = Movie("Bhoot Bangla", 199, "5pm-7pm")
movie2 = Movie("Avatar: The Way of Water", 399, "8pm-10pm")

movie1.show_details()
movie1.book_ticket()
movie1.cancel_ticket()

movie2.show_details()
movie2.book_ticket()
movie2.cancel_ticket()



# =================================================
#               GYM MEMBERSHIP SYSTEM                      
# =================================================

class Gym:

    def __init__(self, member_name, age, membership_plan):
        self.member_name = member_name
        self.age = age
        self.membership_plan = membership_plan

    def show_details(self):
        print("\n==================== GYM MEMBERSHIP DETAILS ====================")
        print("Member Name:", self.member_name)
        print("Age:", self.age)
        print("Membership Plan:", self.membership_plan)
        print()

    def start_workout(self):
        print(self.member_name, "has started the workout")

    def renew_membership(self):
        print(self.member_name, "'s membership has been renewed")

member1 = Gym("Yash", 19, 7999)
member2 = Gym("Utsav", 17, 5999)

member1.show_details()
member1.start_workout()
member1.renew_membership()

member2.show_details()
member2.start_workout()
member2.renew_membership()



# =================================================
#          ONLINE SHOPPING PRODUCT SYSTEM                      
# =================================================

class Shopping:

    def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category

    def show_details(self):
        print("\n==================== SHOPPING PRODUCT DETAILS ====================")
        print("Product Name:", self.product_name)
        print("Product Price:", self.product_price)
        print("Product Category:", self.product_category)
        print()

    def add_to_cart(self):
        print(self.product_name, "has been added to cart")

    def buy_product(self):
        print("You bought", self.product_name, "for ₹", self.product_price)


product1 = Shopping("Mobile", 14999, "Electronics")
product2 = Shopping("T-shirt", 499, "Fashion")

product1.show_details()
product1.add_to_cart()
product1.buy_product()

product2.show_details()
product2.add_to_cart()
product2.buy_product()