from locust import HttpLocust, TaskSequence, seq_task, task 

class DemoTaskSequence(TaskSequence):
    # seq_task - Defines the order of task execution
    # login -> get_info -> get_asset
    @seq_task(1) 
    def login(self):
        self.client.get("/", name="Login")

    @seq_task(2)
    def get_info(self):
        self.client.get("/", name="Get info")

    @seq_task(3)
    @task(2) # Defines that the get asset runs twice
    def get_asset(self):
        self.client.get("/", name="Get assset")

class DemoHttpLocust(HttpLocust):
    task_set = DemoTaskSequence