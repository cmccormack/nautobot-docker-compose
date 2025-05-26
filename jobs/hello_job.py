from nautobot.apps.jobs import Job, register_jobs
import pdb


name = "Hello World Nautobot Jobs"

class HelloWorld(Job):

    class Meta:
        name = "Hello World"
        description = "Hello World for first Nautobot Jobs"

    def run(self):
        self.logger.debug("Hello, this is my first Nautobot Job.")

class HelloWorldWithLogs(Job):

    class Meta:
        name = "Hello World with Logs"
        description = "Hello World with different log types"

    def run(self):
        x = 1
        y = 2
        name = "Chris"
        self.logger.info("This is an info type log.")
        self.logger.debug("This is a debug type log.")
        self.logger.warning("This is a warning type log.")
        pdb.set_trace()
        self.logger.error("This is an error type log.")
        self.logger.critical("This is a critical type log.")

register_jobs(
    HelloWorld,
    HelloWorldWithLogs,
)