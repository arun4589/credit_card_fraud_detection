import os
import sys
import logging
from datetime import datetime


File=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
File_path=os.path.join(os.getcwd(),'logs',File)

os.makedirs(File_path,exist_ok=True)
log_file_path=os.path.join(File,File_path)

logging.basicConfig(
    filename=log_file_path,
    format='%(acstime)s %(message)s %(levelname)s %(lineno)s',
    level=logging.INFO()

)