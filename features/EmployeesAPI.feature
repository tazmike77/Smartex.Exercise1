# Created by pedro silva at 27/11/2022

# From the page http://dummy.restapiexample.com/
# /create	POST	{"name":"test","salary":"123","age":"23"}

Feature: Verify if Employee is added and deleted using Library API

  @addEmployee
  Scenario: Verify AddEmployee API functionality
    Given the employee details needs to be added
    When we execute the AddEmployee PostAPI method
    Then employee is successfully added




