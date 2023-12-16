import pandas as pd

df = pd.read_csv('data/devpost_data_raw_data.csv')
# Remove winners_announced. Not important data
df = df.drop(columns=['winners_announced'])
df = df.drop(columns=['prize_amount'])
# Remove any data that doesn't have any themes
df = df[df['themes'].apply(lambda x: len(eval(x)) != 0 if isinstance(x, str) and x.startswith('[') else True)]
# Remove trash data that is used for test purpose
df = df[(df['title'].str.strip() != 'test') & (df['title'].str.strip() != 'Test')]

# Seperate submission_period_dates to start data and end date
df[['start_date', 'end_date']] = df['submission_period_dates'].str.split(' - ', expand=True)
df['year'] = df['end_date'].str.extract(r'(\d{4})')
df['missing_month'] = df['start_date'].str.extract(r'([a-zA-Z]+)')
df['start_date'] = df.apply(lambda row: row['start_date'] + ', ' + row['year'] if ',' not in row['start_date'] else row['start_date'], axis=1)
df['end_date'] = df.apply(lambda row: row["missing_month"] + " " + row['end_date']
                          if pd.notna(row['end_date']) and row['end_date'][0].isdigit()
                          else row['end_date'], axis=1)

df.drop(columns=['submission_period_dates'], inplace=True)
df.drop(columns=['year'], inplace=True)
df.drop(columns=['missing_month'], inplace=True)

# Remove any data that start_date year is before 2018 ,4397
start_date_frame = pd.to_datetime(df['start_date'])
df = df[start_date_frame.dt.year >= 2018]

# Modify the data to make most of them up to date
# pending
df.to_csv('data/devpost_data_update1.csv', index=False)