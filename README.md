# fastapi-project

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage Section](#usage-section)

## Project Desription
The project aims to act as a server endpoint for a python library.

## Installation

## Project Setup
1. To clone GitHub repo:
```bash
git clone https://github.com/MujtabaNasir/fastapi-project.git
```

2. To create virtual environment:
```bash
python -m venv fastapi_env
```

3. To activate virtual environment:
```bash
. fastapi_env/Scripts/activate
```

4. To deactivate go into the folder where .bat files exists:
```bash
cd ./fastapi_env/Scripts/
deactivate
```

5. Install necessary dependancies
```bash
pip install -r requirements.txt
```

6. Install mujtaba-charm package:
```bash
pip install git+https://github.com/MujtabaNasir/mujtaba-charm.git
```

7. To run black and isort:
```bash
black .
isort .
```

7.Run FastAPI application
```bash
uvicorn main:app --reload
```
or
```bash
python main.py
```

