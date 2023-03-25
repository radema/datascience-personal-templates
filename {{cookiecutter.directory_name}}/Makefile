.ONESHELL:

SHELL = /bin/zsh
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

activate-env:
	conda env update --prune -f config/environment.yml
	$(CONDA_ACTIVATE) <<env_name>>
	
setup: activate-env