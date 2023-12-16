import pandas as pd

df = pd.read_csv('data/user_data.csv')

all_themes = ['1_Blockchain', '2_DevOps', '3_Fintech', '4_Gaming', '5_AR/VR', '6_Machine Learning/AI', '7_IoT', '8_Voice skills', 
            '9_Cybersecurity', '10_Communication', '11_Productivity', '12_Lifehacks', '13_Social Good', '14_COVID-19', '15_Music/Art', 
            '16_Health', '17_Low/No Code', '18_Design', '19_Education', '20_E-commerce/Retail','21_Enterprise', '22_Open Ended', 
            '23_Beginner Friendly', '24_Quantum', '25_Web', '26_Mobile', '27_Robotic Process Automation', '28_Databases']

matrix = pd.DataFrame(0, index=range(len(df)), columns=all_themes)

matrix.insert(0, 'username', df['username'])

for idx, row in df.iterrows():
    selected_themes = row['selectedThemes']
    themes_list = selected_themes[1:-1].replace("'", "").split(", ")  # 将原string分隔成theme string list
    for theme in themes_list:
        matrix.loc[idx, theme] = 1

matrix.to_csv('data/user_matrix.csv', index=False)

