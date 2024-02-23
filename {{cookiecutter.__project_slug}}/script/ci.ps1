pip-compile --upgrade
pip-compile --upgrade --extra dev -o requirements-dev.txt
pip-compile --upgrade --extra docs -o docs/requirements.txt