import pandas as pd
import random

df = pd.read_csv('data/devpost_data_updateMatrix.csv')

def generate_clicks(row):
    base_clicks = 0
    # 根据open_state生成点击量
    if row['open_state'] == 'open':
        base_clicks = random.randint(7000, 10000)
    elif row['open_state'] == 'upcoming':
        base_clicks = random.randint(1000, 7000)
    elif row['open_state'] == 'closed':
        base_clicks = random.randint(0, 3000)
    # 根据featured生成点击量
    if row['featured'] and (row['open_state'] == 'open' or row['open_state'] == 'upcoming'):
        return base_clicks + random.randint(1000, 3000)
    else:
        return base_clicks

df['clicks_count'] = df.apply(generate_clicks, axis=1)

df.to_csv('data/devpost_data_updateClicks.csv', index=False)
