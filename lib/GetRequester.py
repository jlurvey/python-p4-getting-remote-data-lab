import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_data_list = []
        response_data = json.loads(self.get_response_body())
        for data in response_data:
            response_data_list.append(data)

        return response_data_list
