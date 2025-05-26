from nautobot.dcim.models import Location
from nautobot.apps.jobs import (
    Job,
    register_jobs,
    MultiChoiceVar,
    ObjectVar,
    StringVar,
    TextVar,
    IntegerVar,
)

name = "Day 6 Variables"
description = "Example of using variables in Nautobot Jobs"

class HelloVariables(Job):

    location = ObjectVar(model=Location)
    message = TextVar()
    days = IntegerVar(default="10")
    CHOICES = (
        ('h', 'Happy'),
        ('s', 'Sad'),
        ('a', 'Excited'),
        ('n', 'Neutral'),
    )
    feelings = MultiChoiceVar(choices=CHOICES)

    class Meta:
        name = "Hello Variables"
        description = "Jobs Variable Examples"

    def run(self, message, days, feelings, location):
        self.logger.info(f"Please give the message: {message} in {days}")
        self.logger.info(f"I am feeling {feelings}!")
        self.logger.info(f"Pick a location: {location}")

        
register_jobs(
    HelloVariables,
)
