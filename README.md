# python-logging

Exploring different approaches to logging.

## Examples

Example1:

```shell
❯ python example1_explicit.py
INFO:models:Costings:Running model
INFO:root:CostingsModel took 0.3s
INFO:models:Expenses:Running model
INFO:root:ExpensesModel took 0.4s
```

Example2:

```shell
❯ python example2_decorators.py 
INFO:models:Costings:Running model
INFO:models:Costings:run_model took 0.56s
INFO:models:Expenses:Running model
INFO:models:Expenses:run_model took 0.13s
```

Example 3:

```shell
❯ python example3_funcname.py
2024-12-07 11:22:49,508 - INFO - CostingsModel.py - run_model - Running model
2024-12-07 11:22:50,253 - INFO - example3_funcname.py - <module> - CostingsModel took 0.75s
2024-12-07 11:22:50,253 - INFO - ExpensesModel.py - run_model - Running model
2024-12-07 11:22:50,698 - INFO - example3_funcname.py - <module> - ExpensesModel took 0.45s
```
