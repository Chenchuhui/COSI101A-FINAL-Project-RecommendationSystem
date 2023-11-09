import pandas as pd
from datetime import datetime, timedelta

def correct_date(date):
    # Function to correct the date if the day is out of range for the month
    try:
        return datetime.strptime(date, '%b %d, %Y')
    except ValueError:
        # Split the date string and convert to a list
        date_parts = date.split(' ')
        # Convert the day part to an integer and subtract one
        day = int(date_parts[1].strip(',')) - 1
        # Reconstruct the date string with the corrected day
        corrected_date = f"{date_parts[0]} {day}, {date_parts[2]}"
        # Recursively call the correct_date function until a valid date is found
        return correct_date(corrected_date)

def update_project_date(row):
    # Initialize start_date and end_date to None
    start_date = None
    end_date = None
    
    # Try to correct and update the start_date if it's not null and is a string
    if pd.notnull(row['start_date']) and isinstance(row['start_date'], str):
        try:
            start_date = correct_date(row['start_date'])
            if (start_date.day != 29):
                start_date = start_date.replace(year=2023)
            else :
                start_date = start_date.replace(day=28, year=2023)
            row['start_date'] = start_date.strftime('%b %d, %Y')
        except Exception as e:
            print(f"Error processing start_date in row {row.name}: {e}")

    # Try to correct and update the end_date if it's not null and is a string
    if pd.notnull(row['end_date']) and isinstance(row['end_date'], str):
        try:
            end_date = correct_date(row['end_date'])
            if (end_date.day != 29):
                end_date = end_date.replace(year=2023)
            else :
                end_date = end_date.replace(day=28, year=2023)
            row['end_date'] = end_date.strftime('%b %d, %Y')
        except Exception as e:
            print(f"Error processing end_date in row {row.name}: {e}")

    return row

def update_open_state(row):
    # Set 6/1/2023 as the current date to keep most data effective
    current_date = datetime.strptime('Oct 1, 2023', '%b %d, %Y') 
    last_date_of_year = datetime.strptime('Dec 31, 2023', '%b %d, %Y') 
    if pd.notnull(row['end_date']) and current_date >= correct_date(row['end_date']):
        row['open_state'] = 'closed'
    elif pd.notnull(row['start_date']) and current_date <= correct_date(row['start_date']):
        row['open_state'] = 'upcoming'
    else:
        row['open_state'] = 'open'
    if pd.notnull(row['end_date']):
        days_remaining = (correct_date(row['end_date']) - current_date).days
        if (days_remaining >= 0):
            row['time_left_to_submission'] = f'{days_remaining} days left'
        else:
            row['time_left_to_submission'] = '0 days left'
    else :
        days_remaining = (last_date_of_year - current_date).days
        row['time_left_to_submission'] = f'{days_remaining} days left'
        

    return row


df = pd.read_csv('data/devpost_data_update1.csv')
df = df.apply(update_project_date, axis=1)
df = df.apply(update_open_state, axis=1)
# Optionally, save the updated DataFrame to a new CSV
df.to_csv('data/devpost_data_update2.csv', index=False)
