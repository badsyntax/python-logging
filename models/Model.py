
import logging

# Base Model

class Model:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)

    def get_name(self):
        return self.name

    def run_model(self):
        raise NotImplementedError()
