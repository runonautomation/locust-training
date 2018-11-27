# git clone https://github.com/locustio/locust.git
# cd locust/
# git checkout geventhttpclient 
# pip install .
from locust import HttpLocust, TaskSet, task
from locust.contrib.fasthttp import FastHttpLocust

class UserBehavior(TaskSet):
    @task(1)
    def get(self):
        self.client.get("/", name="Get index")
class WebsiteUser(FastHttpLocust):
    task_set = UserBehavior
    max_wait = 0
    min_wait = 0