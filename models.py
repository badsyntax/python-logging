import logging
from random import randint
from time import sleep
from decorators import timed


class Model:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(__name__ + ":" + name)

    def get_name(self):
        return self.name

    def run_model(self):
        self.logger.info("Running model")


# Basic Models


class CostingsModel(Model):
    def __init__(self):
        super().__init__("Costings")

    def run_model(self):
        super().run_model()
        sleep(randint(10, 100) / 100)


class ExpensesModel(Model):
    def __init__(self):
        super().__init__("Expenses")

    def run_model(self):
        super().run_model()
        sleep(randint(10, 100) / 100)


# Decorated Models


class CostingsModelWithDecorator(Model):
    def __init__(self):
        super().__init__("Costings")

    @timed
    def run_model(self):
        super().run_model()
        sleep(randint(10, 100) / 100)


class ExpensesModelWithDecorator(Model):
    def __init__(self):
        super().__init__("Expenses")

    @timed
    def run_model(self):
        super().run_model()
        sleep(randint(10, 100) / 100)
