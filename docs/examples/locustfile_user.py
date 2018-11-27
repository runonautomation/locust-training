from locust import Locust, HttpLocust, TaskSet, task 

# TaskSet is a collection of tasks a user (Locust) should
class DemoHttpTaskSet(TaskSet):
    @task
    def index(self):
        self.client.get("/") # session-aware client provided by HttpLocust

class DemoTaskSet(TaskSet):
    @task
    def Demo_task(self):
        print("Locust instance (%r) does a specific task" % (self.locust))

class DemoHttpLocust(HttpLocust): # HttpLocust - user with HTTP client (self.client)
    weight = 2 # DemoHttpLocust with be spawned twice more often than DemoLocust
    task_set = DemoHttpTaskSet
    # minimum and maximum time in milliseconds, that a simulated user will wait 
    # between executing each task (randomized)
    min_wait = 1000
    max_wait = 3000

    def setup(self):
        print("(%r) Locust setup - first action")

    def teardown(self):
        print("(%r) Locust teardown - last action")

class DemoLocust(Locust): # Locust class rappresents 1 simulated user
    weight = 1 # DemoLocust with be spawned twice less often than DemoHttpLocust
    # Tasks that user needs to execute
    task_set = DemoTaskSet