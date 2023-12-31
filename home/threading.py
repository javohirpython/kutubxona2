from threading import Thread
import requests
import json


class HttpRequestThread(Thread):
    def __init__(self, library: dict, name) -> None:
        super().__init__()
        self.library = library
        self.name=name
        self.results = []
        self.status_code = None
    

    def run(self) -> None:
        try:
            response = requests.get(self.library['url'], params={'name':self.name})
            if response.status_code == 200:
                self.status_code = 200
                data = json.loads(response.content)
                for i in data:
                    front_url = self.library['url'].replace('http://127.0.0.1:8', 'http://127.0.0.1:3')
                    i['name'] = self.library['name']
                    i['location'] = self.library['location']
                    i['url']=front_url+"/book/"+str(i['id'])
                    
                self.results +=data

        except ConnectionError:
            pass

