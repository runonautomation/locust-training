from locust import HttpLocust, TaskSet, task 
import datetime 
class DemoHttpTaskSet(TaskSet):
    def setup(self):
        print("(%r) DemoHttpTaskSet setup (once per class)" % datetime.datetime.now())

    def teardown(self):
        print("(%r) DemoHttpTaskSet teardown (once per class)" % datetime.datetime.now())

    def on_start(self): 
        print("(%r) DemoHttpTaskSet on_start" % datetime.datetime.now())

    def on_stop(self): 
        print("(%r) DemoHttpTaskSet on_stop" % datetime.datetime.now())   

    @task(3)
    def demo_task(self):
        self.client.get("/", name="Demo Task")

    @task(1)
    class DemoHttpSubTaskSet(TaskSet):
        # setup teardown and on_start also applicable
        @task
        def demo_sub_task(self):
            self.client.get("/", name="Demo Sub Task")
            
        @task
        def stop(self):
            self.interrupt() # Required to terminate the TaskSet execution

class DemoHttpLocust(HttpLocust):
    task_set = DemoHttpTaskSet
