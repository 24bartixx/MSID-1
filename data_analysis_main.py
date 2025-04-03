
import sys
if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import sys, os
from pathlib import Path
import subprocess
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

NOTEBOOKS_PATH = Path("./notebook/")
DEFAULT_OUTPUT_PATH = Path("./data_analysis_generated/")
KERNEL_NAME = "msid_project1"

def data_analysis_main():
    
    output_path = Path(sys.argv[1] if len(sys.argv) >= 2 else DEFAULT_OUTPUT_PATH)
    
    os.makedirs(output_path, exist_ok = True)

    for path in filter(lambda p: (p.is_file() and p.suffix == ".ipynb"), NOTEBOOKS_PATH.iterdir()):
        
        try:
            # Load notebook
            with path.open('r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)

            # Execute notebook
            ep = ExecutePreprocessor(timeout=600, kernel_name=KERNEL_NAME)
            ep.preprocess(nb, {'metadata': {'path': str(NOTEBOOKS_PATH)}})

            # Save executed notebook
            executed_path = output_path / f"executed_{path.name}"
            with executed_path.open('w', encoding='utf-8') as f:
                nbformat.write(nb, f)

            print(f"✅ Executed and saved to: {executed_path}")

        except Exception as e:
            print(f"❌ Error processing {path.name}: {e}")
        
        # # Load notebook
        # with open(path, 'r', encoding='utf-8') as f:
        #     nb = nbformat.read(f, as_version=4)

        # # Execute notebook with specific kernel
        # ep = ExecutePreprocessor(timeout=600, kernel_name="msid_project1")
        # ep.preprocess(nb, {'metadata': {'path': NOTEBOOKS_PATH}})

        # # Save executed notebook if needed
        # executed_path = os.path.join(NOTEBOOKS_PATH, f"executed_{str(path)}")
        # with open(executed_path, 'w', encoding='utf-8') as f:
        #     nbformat.write(nb, f)
        
        # print(path)
        
        # with open(path) as notebook:
        #     notebook_node = nbformat.read(notebook, as_version = 4)
            
        # execute_preprocessor = ExecutePreprocessor(timeout = 600, kernel_name="msid_project1")
        
        # try:
        #     # execute_preprocessor.preprocess(notebook_node, {"metadata": {"path": NOTEBOOKS_PATH}})
        #     # print(os.path.splitext(path)[0])
            
        #     subprocess.run([
        #         "conda", "run",
        #         "-n", "msid_project1",
        #         "jupyter", "nbconvert",
        #         "--to", "notebook",
        #         "--execute",
        #         "--output", str(output_path),
        #         str(path)
        #     ], check=True)
            
        # except Exception as e:
        #     print(f"Error: {e}")
        #     return

if __name__ == "__main__":
    data_analysis_main()