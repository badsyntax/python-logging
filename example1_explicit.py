import logging
import time
import sys
from models.CostingsModel import CostingsModel
from models.ExpensesModel import ExpensesModel

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logger = logging.getLogger()

models_to_run = [CostingsModel, ExpensesModel]

for model in models_to_run:
    instance = model()

    start = time.perf_counter()
    instance.run_model()
    end = time.perf_counter()

    logger.info("%s took %ss", model.__name__, round(end - start, 2))
