## Using locust.io for performance analysis
This repository contains example code used for locust trainings

## Using the examples

### Presentation: runonautomation_locust.pdf

THe directory examples contains annotated examples of locustfiles
for experimentation

- locustfile_user.py - Base definition of HttpLocust

- locustfile_api_extenstion.py - Creating an additional API endpoint in locust

- locustfile_custom_client.py - Writing a custom client

- locustfile_debug.py - Example of using IDE debugger with locust

- locustfile_fasthttp.py - Using gevent http client for reaching higer RPS with locust

- locustfile_html.py - Example of HTLM parsing with PyQuery

- locustfile_sequence.py - Usage of Task Sequence

- locustfile_taskset.py - Overview of TaskSet capabilities


## Setting UP Continuos integration
- Provision a debian/ubuntu linux server machine on cloud provider
- Install docker following instructions: https://docs.docker.com/install/linux/docker-ce/debian/
- Install pip and locust
- Go to docs/ci directory and run ./build_example.sh to build a sample Jenkins container
- Execute ./run_example.sh to start a sandbox Jenkins instance
- Fork/copy the content of https://github.com/runonautomation/locust-framework repository to your private repository

#### In Jenkins
- Create new multibranch pipeline job
- Under Branch sources add Git and add url to the private repository
- Leave build configuration default: By Jenkinsfile