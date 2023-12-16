import requests
from bs4 import BeautifulSoup
import pandas as pd

# Assuming you have a pandas DataFrame named 'df' with a column 'url'
df = pd.read_csv('data/devpost_data_updateClicks.csv') # Load your dataset

def extract_description(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            description_element = soup.find(id='challenge-description')
            content = description_element.get_text(strip=True)
            print(content)
            return content if description_element else "Description not found"
    except requests.RequestException:
        return "Failed to retrieve content"

# Apply the function to each URL in the DataFrame
df['description'] = df['url'].apply(extract_description)

# Now df has a new column 'description' with the extracted content
df.to_csv('data/devpost_data_update3.csv', index=False)