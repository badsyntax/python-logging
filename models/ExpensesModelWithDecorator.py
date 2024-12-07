from random import randint
from time import sleep
from .Model import Model
from decorators import timed

class ExpensesModelWithDecorator(Model):
    def __init__(self):
        super().__init__("Expenses")

    @timed
    def run_model(self):
        self.logger.info("Running model")
        sleep(randint(10, 100) / 100)
