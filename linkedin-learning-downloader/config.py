# copy this file as `config.py`

import os

# EDIT
USERNAME = 'princeton.wong@alphamind.edu.hk'
PASSWORD = 'wiwjof-Nibban-kyhto6'
COURSES = ["python-3-ssh-network-automation-quick-start", "web-scraping-with-python", "introduction-to-graphic-design-3", ]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None