from locust import TaskSet
from locust import task
from locust import HttpLocust

class DemoHttpTaskSet(TaskSet):
    @task
    def demo_task(self):
        res = self.client.get("/", name="Debugging Example")
        print(str(res))

class DemoHttpLocust(HttpLocust):
    task_set = DemoHttpTaskSet

if __name__ == '__main__':
    from argparse import Namespace
    from locust import runners as r
    opts = Namespace()
    opts.host = "http://google.com"
    opts.num_clients = 1
    opts.hatch_rate = opts.num_clients
    opts.reset_stats=False
    r.locust_runner = \
        r.LocalLocustRunner(locust_classes=[DemoHttpLocust],
                            options=opts)
    r.locust_runner.start_hatching(wait=True)
    r.locust_runner.greenlet.join()