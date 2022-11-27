import requests
import json
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configurations import *


@given('the employee details needs to be added')
def step_implementation(context):
    context.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36', "Content-Type": "application/json"
    }

    context.url = getConfig()['API']['endpoint'] + ApiResources.createEmployee
    context.payLoad = addBookPayload("pedro", "123", "45")


@when('we execute the AddEmployee PostAPI method')
def step_implementation(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )


@then('employee is successfully added')
def step_implementation(context):
    # Validate the response code 200
    assert context.response.status_code == 200
    context.response = context.response.json()
    context.employeeId = context.response['data']['id']
    # validate the message received after adding the new employee
    assert context.response["message"] == "Successfully! Record has been added."
