#!/usr/bin/env python3

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", 
                    "Legal", "Finance", "Sales", "General Management", 
                    "Research & Development", "Marketing", "Purchasing"]

    def __init__(self, name="John Doe", job="Admin"):
        self._name = None
        self._job = None
        # Only validate name if it's not the default
        if name != "John Doe":
            self.name = name
        else:
            self._name = name.title()
        # Only validate job if it's not the default
        if job != "Admin":
            self.job = job
        else:
            self._job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")