# HOW TO
### This project utilizes `pipenv`

* To install depencencies
```
pipenv install --ignore-pipfile 
```
* To run script
```
pipenv run python -m predictor
```



## Description
The idea is simple. Each speciality has it's "wages" for every subject. And each speciality has `N` points to assign to wages. Then the student grades are multiplied by wages resulting in some score number. As a result we can compare score numbers for different subjects and choose the best match. 