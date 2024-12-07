from random import randint
from time import sleep
from .Model import Model

class CostingsModel(Model):
    def __init__(self):
        super().__init__("Costings")

    def run_model(self):
        self.logger.info("Running model")
        sleep(randint(10, 100) / 100)
