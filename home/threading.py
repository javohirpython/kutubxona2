from threading import Thread
import requests
import json


class HttpRequestThread(Thread):
    def __init__(self, url: str, name) -> None:
        super().__init__()
        self.url = url
        self.name=name
        self.results = []
        self.status_code = None
    

    def run(self) -> None:
        try:
            response = requests.get(self.url, params={'name':self.name})
            if response.status_code == 200:
                self.status_code = 200
                data = json.loads(response.content)
                for i in data:
                    i['url']=self.url+'/book/'+str(i['id'])
                self.results +=data

        except ConnectionError:
            pass

