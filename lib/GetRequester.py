import requests
import json

class GetRequester:


    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response =requests.get(self.url)
      
        return json.loads(response.content)

    def load_json(self):
        program_list=[]
        programs =json.loads(self.get_response_body())
        for program in programs:
            program_list.append(program)
        return program_list
    

# Create an instance of GetRequester with your URL
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

response_body = get_requester.get_response_body()

print(json.dumps(response_body,indent=4,sort_keys=True))