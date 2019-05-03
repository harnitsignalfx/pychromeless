import time
import random
import json

from webdriver_wrapper import WebDriverWrapper


def lambda_handler(event, context):
    driver = WebDriverWrapper()

    driver.get_url('http://35.236.100.236:8080')

    number = int(random.random()*100)%4

    if number == 0:
        driver.click("//span[@data-customer='123']")
    elif number == 1:
        driver.click("//span[@data-customer='392']")
    elif number == 2:
        driver.click("//span[@data-customer='731']")
    else:
        driver.click("//span[@data-customer='567']")

    print("--------------------------")
    print("Success")
    print("--------------------------")

    time.sleep(1)

    driver.close()

    return { 
        'statusCode': 200,
        'body': json.dumps({'message': 'Success - Clicked HotRod link'+' '+str(number)})
    }
