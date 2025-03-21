class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.username = name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Matt")

# user_1.id = "001"
# user_1.username = 'Matt'

user_2 = User("002", "Jack")

# user_2.id = "002"
# user_2.username = 'Jack'
user_1.follow(user_2)
print(user_1.username, user_1.user_id, user_1.followers, user_1.following)
print(user_2.username, user_2.user_id, user_2.followers, user_2.following)