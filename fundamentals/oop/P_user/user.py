class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(
                f"You are now a member! You have {self.gold_card_points} gold card points."
            )

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"You have {self.gold_card_points} points remaining.")
        else:
            print("Not enough member points")


user1 = User("Bobby", "Coleman", "bobby@email.com", 32)

user1.display_info()
user1.enroll()
user1.enroll()  # BONUS

user2 = User("Ashlee", "Coleman", "ashlee@email.com", 32)
user3 = User("Joe", "Dirt", "mulletsrcool@hotrod.com", 45)

user1.spend_points(50)
user2.enroll()
user2.spend_points(80)
user1.display_info()
user2.display_info()
user3.display_info()
user3.enroll()
user3.spend_points(150)
user3.spend_points(60)  # BONUS - not enough points
