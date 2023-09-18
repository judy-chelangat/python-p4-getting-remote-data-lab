import requests
import json

class GetRequester:


    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response =requests.get(self.url)
        return response.content

    def load_json(self):
        program_list=[]
        programs =json.loads(self.get_response_body())
        for program in programs:
            program_list.append(program)
        return program_list