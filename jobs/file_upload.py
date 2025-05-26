from nautobot.apps.jobs import (
    FileVar,
    register_jobs,
    Job,
)
from nautobot.dcim.models import (
    Device,
    DeviceType,
    Location,
)
from nautobot.extras.models import (
    Role,
    Status,
)

name = "File Upload Jobs"

class FileUpload(Job):
    class Meta:
        name = "CSV File Upload"
        description = "Please select a CSV file for upload"

    file = FileVar(
        description="CSV file to upload",
    )

    def run(self, file):

        contents = str(file.read())
        self.logger.info(f"File Contents: {contents}")
        self.logger.info("Job didn't crash!")

        return "Great Job!"

class FileUploadWithProcessing(Job):
    class Meta:
        name = "CSV File Upload and Process"
        description = "Please select a CSV file for upload"
    
    file = FileVar(
        description="CSV File to upload",
    )

    def run(self, file):
        file_contents = file.read().decode("utf-8")
        self.logger.info(file_contents)
        lines = file_contents.splitlines()
        self.logger.info(lines)

        self.logger.info("Parsing the lines...")

        for line in lines[1:]:
            device_name, role_name, model_name, location_name = line.split(',')
            self.logger.info(f"Name: {device_name}")
            self.logger.info(f"Role: {role_name}")
            self.logger.info(f"Device Type: {model_name}")
            self.logger.info(f"Location: {location_name}")

            role = Role.objects.get(name=role_name)
            device_type = DeviceType.objects.get(model=model_name)
            location = Location.objects.get(name=location_name)
            status = Status.objects.get(name="Active")
            device = Device(
                name=device_name,
                device_type=device_type,
                location=location,
                status=status,
                role=role,
            )
            res = device.validated_save()
            self.logger.info(f"Device {device_name} created: {res}")
        return "Execution completed successfully!"

register_jobs(
    FileUpload,
    FileUploadWithProcessing,
)