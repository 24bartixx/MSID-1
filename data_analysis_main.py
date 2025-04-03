
import sys, os
from pathlib import Path
import logging
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

NOTEBOOKS_PATH = Path("./notebook/")
KERNEL_NAME = "msid_project1"

def get_logger(name = "logger"):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s\t%(message)s"))
    logger.addHandler(console_handler)
    
    return logger

def data_analysis_main():
    
    logger = get_logger()

    for notebook_path in filter(lambda path: (path.is_file() and path.suffix == ".ipynb"), NOTEBOOKS_PATH.iterdir()):
        
        logger.info(f"Saving files from {notebook_path}")
        
        try:
            with notebook_path.open("r", encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)

            ep = ExecutePreprocessor(timeout=600, kernel_name = KERNEL_NAME)
            ep.preprocess(nb, {"metadata": {"path": str(NOTEBOOKS_PATH)}})
            
            logger.info(f"Saved files from {notebook_path}")
            
        except Exception as e:
            logger.error(f"Error with notebook {notebook_path.name}: {e}")

if __name__ == "__main__":
    data_analysis_main()