# Neoro Net - Test

Ths project is to calculate distance between MKAD to specific address using Yandex Geo API. 

System will automatically pick the first from address that has multiple result.

[Demo site](http://taqin.pythonanywhere.com/)

## Project Structure

- app.py   : Main flask server script
- geo.py   : Blueprint script
- utils.py : Utility script containing Yandex API and Logging class
- requirement.txt : depedency pip package
- testing.py : Unit Test
- Dockerfile : Dockerfile for building images
- .log : System log file


## System Requirement

1. Python 3.8
2. Flask

## Installation

1. Clone and Unzip the repo.

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package depedency.

```bash
pip install -r requirements.txt
```

## Usage

1. Add app.py to Flask environment variable
```bash
export FLASK_APP=app.py
```
2. Run flask
```
flask run
```
3. When the server is running, open browser and go to [http://localhost:5000/mkad/?address=NAME](http://localhost:5000/mkad/?address=NAME)

&ensp;&ensp;&ensp;&ensp;NAME is string/text and it can be a specific address, example : [http://localhost:5000/mkad/?address=Аэропорт%20Внуково](http://localhost:5000/mkad/?address=Аэропорт%20Внуково) or longitude,lattitude, example : [http://localhost:5000/mkad/?address=37.34868,55.708019](http://localhost:5000/mkad/?address=37.34868,55.708019)

4. If the address inside MKAD, then system will return the address longitude/lattitude without calculating distance. If the address outside MKAD, then system will return distance in kilometer using Haversine formula.


## Installation Docker

1. Clone and Unzip the repo.

2. Build docker image.

```bash
docker build --tag neuronet-test .
```


## Run Docker
```bash
docker run --network='host' neuronet-test
```


## Unit Test
Make sure the server is running
```bash
python testing.py
```