import requests
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "addEmployee" in scenario.tags:
        url = getConfig()['API']['endpoint'] + ApiResources.deleteEmployee + str(context.employeeId)
        context.response = requests.delete(url,  headers=context.headers,)
        assert context.response.status_code == 200
        res_json = context.response.json()
        assert res_json["message"] == "Successfully! Record has been deleted"
