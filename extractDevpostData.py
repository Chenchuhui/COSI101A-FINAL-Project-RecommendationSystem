import requests
import json
import csv

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w', newline='')
        self.writer = csv.writer(self.file)

    def write_col(self, *headers):
        self.writer.writerow(headers)

    def write_data(self, data):
        self.writer.writerow(data)

    def close(self):
        self.file.close()

def extract_api(page: int) -> list:
    html_text = requests.get(f'https://devpost.com/api/hackathons?page={str(page)}').text
    html_dict: dict = json.loads(html_text)
    return html_dict["hackathons"]

if __name__ == "__main__" :
    max_page: int = 969
    writer = CSVWriter('devpost_data.csv')
    writer.write_col("id", "title", "open_state", "url", "time_left_to_submission", "submission_period_dates", "themes", "prize_amount", "registrations_count", "featured", "organization_name", "winners_announced")
    for i in range(1, max_page+1):
        api_content = extract_api(i)
        for item in api_content:
            data = [item["id"], item["title"], item["open_state"], item["url"], item["time_left_to_submission"], item["submission_period_dates"], item["themes"], item["prize_amount"], item["registrations_count"], item["featured"], item["organization_name"], item["winners_announced"]]
            print(data)
            writer.write_data(data)
        print("page %d done" %i)