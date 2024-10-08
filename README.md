# Cinema App
Simple Python application for Cinema booking

## Assumptions

 - When col is even, prioritize the left middle seat over right middle seat. 
 - Data is not persistent ( i.e. in a database) 

## Design

* Cinema.py: Core functionality: seat map; book ammend and saving booking; retrieve booking 
* Helper.py: Class-less generic function
* booking_flow: Class base, menu operation 
* Display: drived by Jinjia2 Template
* Minimum code based on the requirement and TDD priciple, but add basic checks

## files

src
├── booking_flow.py
├── cinema.py
├── helper.py
├── __init__.py
└── templates
    ├── map.j2
    └── menu.j2

tests
├── __init__.py
├── test_booking_end_to_end.py
├── test_booking_flow.py
├── test_cinema.py
└── test_helper.py


## internal function docs

**Refer to pydoc.md.**

# Usage

* CI/CD - Including Unit Test, End to End Test. Package and upload as Docker Image. 
* Run docker image in [Packages] (https://github.com/weidong-zhou/python-tdd/pkgs/container/cinema) 