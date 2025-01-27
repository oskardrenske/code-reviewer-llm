# Code review with LLM

## Review local code with a local LLM.


# Prerequisites
### Ollama
[Ollama](https://ollama.com) runs the LLM. Download and install it.

### UV
[UV](https://docs.astral.sh/uv/) is used for Python dependencies. Download and install it.

## venv + install
Create a virtual environment with `uv venv`
Install Python dependencies with `uv sync`

# Configure
## Model
Download a suitable model ([list of models](https://github.com/ollama/ollama))



Create a file named `.env` with entries like this:
```
LLM_MODEL="the-name-of-the-model"
PROG_LANG="python"
FILE_SUFFIX=".py"
PATH_TO_CHECK="absolut/path/to/the/code"


```

download the model you want to use 

PRINT = os.getenv("PRINT", "True").lower() == "true"


# Run it
- Make sure ollama is running
- Python main.py <local/path/to/code>


# Output
The report is saved in a folder named `reviews/repo-path/timestamp`


