import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from mcqgenerator.utils import read_file, get_table_data
from mcqgenerator.mcqgenerator import generate_evaluate_chain
from mcqgenerator.logger import logging

