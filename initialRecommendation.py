import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data/devpost_data_update5.csv')

selected_columns = ['title', 'open_state',
    '1_Blockchain', '2_DevOps', '3_Fintech', '4_Gaming', '5_AR/VR', '6_Machine Learning/AI', '7_IoT', '8_Voice skills', 
    '9_Cybersecurity', '10_Communication', '11_Productivity', '12_Lifehacks', '13_Social Good', '14_COVID-19', '15_Music/Art', 
    '16_Health', '17_Low/No Code', '18_Design', '19_Education', '20_E-commerce/Retail','21_Enterprise', '22_Open Ended', 
    '23_Beginner Friendly', '24_Quantum', '25_Web', '26_Mobile', '27_Robotic Process Automation', '28_Databases'
]

df = df[selected_columns]

# Filter out closed projects
df = df[df['open_state'] != 'closed']

df = df.drop(columns=['open_state'])

df.to_csv('data/item_matrix.csv', index=False)

user_data = pd.read_csv('data/user_matrix.csv', index_col='username')
item_data = pd.read_csv('data/item_matrix.csv', index_col='title')

user_matrix = user_data.values
item_matrix = item_data.values

similarity_matrix = cosine_similarity(user_matrix, item_matrix)

num_recommendations = 5
recommendations = {}

for i, user in enumerate(user_data.index):
    # Get sorted similar items' indices for the ith user
    similar_items_indices = np.argsort(similarity_matrix[i, :])[::-1]
    # Recommend top 5 similar items to this user
    recommendations[user] = [item_data.index[j] for j in similar_items_indices[:num_recommendations]]

recommendations_df = pd.DataFrame.from_dict(recommendations, orient='index', columns=[f'Recommendation{i+1}' for i in range(num_recommendations)])

recommendations_df.to_csv('data/initial_recommendations.csv')
