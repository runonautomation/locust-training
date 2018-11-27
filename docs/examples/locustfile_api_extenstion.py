from locust import HttpLocust, TaskSet, web, task

@web.app.route("/extension")
def custom_stats():
    return "Locust extension"

class DemoTaskSet(TaskSet):
    @task
    def login(self):
        self.client.get("/", name="Login")
        
class DemoHttpLocust(HttpLocust):
    task_set = DemoTaskSet