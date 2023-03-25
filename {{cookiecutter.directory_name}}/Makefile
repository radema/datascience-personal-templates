.ONESHELL:

SHELL = /bin/zsh
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

activate-env:
	@echo "Activating virtual environment ..."
	conda env update --prune -f config/environment.yml
	$(CONDA_ACTIVATE) <<env_name>>

initialize-git:
	@echo "Initializing Git..."
	git init

setup: activate-env initialize-git

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache