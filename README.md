🌱 Welcome to the mulch command line interface. 

The purpose of this software:
- Add new projects to an existing modular file structure.

The file structure in question is the pavlovian template:
- https://github.com/City-of-Memphis-Wastewater/pavlovian

This project is designed to be accessed via:
- pip install mulchcli
- .whl
- poetry add mulchcli

✅ Usage(After Installation)
Once published or locally installed, you can run:

mulchcli init my-new-project

mulchcli config my-new-project db_host 127.0.0.1

mulchcli list-projects

✅ Or, if developing locally:

python -m mulchcli init my-new-project