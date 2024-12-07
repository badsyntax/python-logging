import logging
import sys
from models import CostingsModelWithDecorator, ExpensesModelWithDecorator

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

models_to_run = [CostingsModelWithDecorator, ExpensesModelWithDecorator]

for model in models_to_run:
    instance = model()
    instance.run_model()
