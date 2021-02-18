<!--
  * browser: architecture
  * version: 1.2.0
  * updated: 2020-02-17T02:39:34Z
  * contact: Shuai Wang (shuai.wang.kaos@gmail.com)
-->

# Project1 unit test for GUI automation test

Use Selenium and framework unittest to make the automation test, generate the test report with HtmlTestRunner, use POM (page object module) to build the test framework.

Contents:

* [Why use unit test](#why-use-unit-test)
* [The architecture information](#the-architecture-information)
* [Configure the enviroment](#configure-the-enviroment)
* [How to run the tests](#how-to-run-the-tests)


## Why use unit test

* As the UnitTest framework comes bundled with the Python library, there is no specific configuration or additional installation required

* Provides instant reports for test analysis

* Using UnitTest is convenient, even for users not skilled at Python

* Execution of test cases is hassle-free


## The architecture information

The project has four folders to manage the project:

  * **..\Lib\Locators\locators.py**
    *  the Lib folder contains the locators from different pages
    *  the Lib folder used to contain the chrome webdriver but I have moved the web driver to the PATH with the value C:\Users\*****\AppData\Local\Programs\Python\Python39\Scripts

  * **..\Config**
    * **..\Config\config.ini** this file manage all the data for the tests for example users,url and report path, it is easy for the maintanence afterwards
    * **..\Config\config_file.py** this file is used for parsing the data from ..\Config\config.ini which can import for the tests

  * **..\Report**
    * This folder receives the reports when tests complete  
    * you can run from command line with `python test_Login.py` from the path ..\test, the report should be generated path is configured from ..\Config\config.ini

  * **..\test**
    * This folder contains all the automation tests for different functionality and pages

## Configure the enviroment:

  * Install html-testRunner
    * use `pip install html-testRunner`
    * the version is html-testRunner 1.2.1

  * Install selenium
    * use `pip install selenium`
    * the version is selenium 3.141.0

  * Install configparser
    * use `pip install configparser`
    * the version is configparser 5.0.1

  * download webdriver for Chrome (FF, IE)
    * add the drivers to the PATH C:\Users\*****\AppData\Local\Programs\Python\Python39\Scripts

## How to run the tests:
  * you can run from command line with `python test_Login.py` from the path ..\test
  * the report should be generated in the **..\Report** folder

