import time
from locust import Locust, events

class CustomClient(object):
    def do_actual_request(self, remote, request_type, request_name):
        time.sleep(1)
        return 

    # Locust custom client wrapper function
    def request(self, remote, request_type, request_name):
        result = None
        start_time = time.time()
        try:
            result = self.do_actual_request(remote, request_type, request_name)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type=request_type, name=request_name,
                response_time=total_time, exception=e
            )
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(result.response.to_text())
            events.request_success.fire(
                request_type=request_type, name=request_name,
                response_time=total_time, response_length=length
            )
        return result

class CustomLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(CustomLocust, self).__init__(*args, **kwargs)
        self.client = CustomClient(self.host)

