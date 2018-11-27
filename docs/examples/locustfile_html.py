from locust import HttpLocust, TaskSequence, seq_task, task
from pyquery import PyQuery #pip install pyquery
import random

class DemoTaskSequence(TaskSequence):
    @seq_task(1) 
    @task(1)
    def index_page(self):
        r = self.client.get("/", name="Get Root")
        pq = PyQuery(r.content)
        self.links = pq("a") # Get links

    @seq_task(2) 
    @task(1)
    def load_page(self, url=None):
        url = random.choice(self.links).attrib["href"]
        print(str(url))
        self.client.get(url)

class DemoHttpLocust(HttpLocust):
    task_set = DemoTaskSequence
    host = "https://github.com/"