# copy this file as `config.py`

import os

# EDIT
USERNAME = 'princeton.wong@alphamind.edu.hk'
PASSWORD = 'wiwjof-Nibban-kyhto6'
COURSES = ["advanced-python", "using-python-for-automation", "python-working-with-predictive-analytics", "python-advanced-design-patterns",
           "python-data-structures-stacks-queues-and-deques", "faster-python-code", "sql-server-machine-learning-services-python",
           "python-parallel-and-concurrent-programming-part-1", "learning-regular-expressions-2", "python-parallel-and-concurrent-programming-part-2",
           "python-data-structures-linked-lists", "advanced-design-patterns-design-principles", "ai-algorithms-for-gaming", "advanced-python-working-with-databases",
           "design-patterns-creational", "effective-serialization-with-python", "advanced-pandas", "python-essential-training-2", "python-for-data-science-essential-training",
           "python-automation-and-testing", "programming-foundations-design-patterns-2", "learning-python-gui-programming", "python-gui-development-with-tkinter-2",
           "python-xml-json-and-the-web", "django-forms", "learning-django-2018", "python-for-data-science-essential-training-part-2", "python-object-oriented-programming",
           "data-ingestion-with-python", "full-stack-web-development-with-flask", "dynamo-for-revit-python-scripting-2", "building-tools-with-python", "grasshopper-and-rhino-python-scripting",
           "building-restful-apis-with-flask", "python-3-ssh-network-automation-quick-start", "web-scraping-with-python", "introduction-to-graphic-design-3", ]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None