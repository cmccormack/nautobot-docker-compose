from nautobot.apps.jobs import Job, register_jobs, JobHookReceiver
import requests

name = "Job Hook Receivers"


class HelloWorldJobHook(JobHookReceiver):
    class Meta:
        name = "This is my first Job Hook Receiver"

    def receive_job_hook(self, change, action, changed_object):
        self.logger.info(
            "Launching Job Hook Receiver.", extra={"object": change}
        )
        self.logger.info(
            "Launching Job Hook Receiver.", extra={"object": action}
        )
        self.logger.info(
            "Launching Job Hook Receiver.", extra={"object": changed_object}
        )

        response = requests.get("https://httpbin.org/get")
        if response.status_code == 200:
            self.logger.info("Job Hook Launched.")


register_jobs(
    HelloWorldJobHook,
)
