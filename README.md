python -m pip install --upgrade pip
Use pipenv, which has similar interface with bundler.

$ pip install pipenv
Pipenv creates virtualenv automatically and installs dependencies from Pipfile or Pipfile.lock.

$ pipenv install           # Install dependencies from Pipfile
$ pipenv install requests  # Install `requests` and update Pipfile
$ pipenv lock              # Generate `Pipfile.lock`
$ pipenv shell             # Run shell with virtualenv activated
You can run command with virtualenv scope like bundle exec.

$ pipenv run python3 -c "print('hello!')"
Run autotest on server (Example)

pipenv run py.test task_number_three\tests\shop_phone_test.py