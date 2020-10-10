# Backend REST API with Python and Django

Test Driven Development (TDD) improves:
- code quality
- comprehension
- confidence

## API
- authentication
- creating objects
- filtering
- uploading images

## tools
- pytho vers >= 3.7
- django
- django-rest-framework
- docker
- travis-ci (automate testing and linting)
- postgres

## Test Driven Development

first write the test then write then implement the feature.

## Unit Tests
- check that your code works
- isolate specific code:
    1. function
    2. class

## Test Stages
### Setup
- create sample database objects

### Execution
- call the code

### Assertion
- configrm expected ouput

## Why writing tests?
- expected in most professional dev teams
- makes it easier to change code
- save time
- testable, better code quality

## Why use TDD?
- increase test coverage
- ensure tests work
- encourages quality code
- stay focused

## Django in Docker

Start a django project app in docker after creating Dockerfile and docker-compose.yaml file.

```bash
docker-compose run app sh -c "django-admin.py startproject app ."
```

## Travis-CI on gitlab

url: https://travis-ci.org