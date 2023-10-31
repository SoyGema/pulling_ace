# Beyond-the-Nest

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.



### Builds

This is right now intented to be a python library 
Uninstall the Previous Version: If you have a previous version of the package installed, you can uninstall it first to avoid conflicts. You can use the following command for that:

bash
Copy code
pip uninstall your_package_name
Replace your_package_name with the name of your package.

Increment the Version Number: If you've made changes that you want to distribute, it's a good practice to increment the version number in your setup.py file.

python
Copy code
setup(
    name='your_package_name',
    version='0.2',  # Increment this number
    # ...
)
Clear Old Build Directories: Remove old build artifacts to make sure you're starting fresh. Navigate to the folder containing setup.py and run:

bash
Copy code
rm -rf build dist your_package_name.egg-info
Replace your_package_name with the name of your package.

Rebuild the Package: Navigate to the folder where your setup.py file is located and run:

bash
Copy code
pip install .
This will rebuild the package and install it.

Check Installation: You can check if the package is installed correctly by running:

bash
Copy code
pip list