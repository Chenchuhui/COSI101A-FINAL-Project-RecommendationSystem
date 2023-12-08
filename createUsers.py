import csv
from faker import Faker
import random

all_themes = [
    '1_Blockchain', '2_DevOps', '3_Fintech', '4_Gaming', '5_AR/VR', '6_Machine Learning/AI', '7_IoT', '8_Voice skills',
    '9_Cybersecurity', '10_Communication', '11_Productivity', '12_Lifehacks', '13_Social Good', '14_COVID-19', '15_Music/Art',
    '16_Health', '17_Low/No Code', '18_Design', '19_Education', '20_E-commerce/Retail', '21_Enterprise', '22_Open Ended',
    '23_Beginner Friendly', '24_Quantum', '25_Web', '26_Mobile', '27_Robotic Process Automation', '28_Databases'
]

# Random generator
fake = Faker()
Faker.seed(0)

# Generate random users with random selected themes
def generate_random_users(count):
    users = []
    for _ in range(count):
        user = {
            'username': fake['en-US'].name(),
            'selectedThemes': random.sample(all_themes, random.randint(1, len(all_themes)))
        }
        users.append(user)
    return users

# Save user data to csv
def save_to_csv(users, filename):
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['username', 'selectedThemes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow(user)

number_of_users = 5000

random_users = generate_random_users(number_of_users)

save_to_csv(random_users, 'user_data.csv')
print("User data created")
