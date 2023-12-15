import csv
from faker import Faker

# Random generator
fake = Faker()
Faker.seed(0)

# Generate random users with random selected themes
def generate_random_users(count):
    users = []
    for _ in range(count):
        user = {
            'username': fake['en-US'].name(),
        }
        users.append(user)
    return users

# Save user data to csv
def save_to_csv(users, filename):
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['username']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow(user)

number_of_users = 1000

random_users = generate_random_users(number_of_users)

save_to_csv(random_users, './data/users.csv')
