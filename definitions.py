import os
from pathlib import Path

try:
    config = os.environ['CFG_FILE']
except KeyError as e:
    config = "api_tests/config/config.ini"
    print('Excepting key error for cfg file running due to running locally "%s"' % str(e))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = Path(ROOT_DIR) / config
