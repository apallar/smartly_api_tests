import pytest
import requests
import json
     
######  TC1: Verify GET Users request  #####
## Steps:
## 1. Verify 200 OK message is returned
## 2. Verify that there are 10 users in the results
@pytest.mark.parametrize('inp_URL, exp_resp_code, exp_data_count', [('https://jsonplaceholder.typicode.com/users', 200, 10)])
def test_verify_GET_users_requests(inp_URL, exp_resp_code, exp_data_count):
##def test_verify_GET_users_requests():

     #Send the GET request
     response = requests.get(inp_URL)
     #Converts to JSON
     response_body = response.json()

     #Response code should be 200
     assert response.status_code == exp_resp_code
     
     #Get the length of the response data
     response_len = len(response_body)
     assert response_len == exp_data_count

######  TC2: Verify GET User request by Id  #####
## Steps:
## 1. Verify 200 OK message is returned
## 2. Verify if user with id8 is Nicholas Runolfsdottir V 
@pytest.mark.parametrize('inp_user_id, exp_user_name', [('8', 'Nicholas Runolfsdottir V')])
def test_verify_GET_users_requests_by_id(inp_user_id, exp_user_name):
     URL = "https://jsonplaceholder.typicode.com/users" +"?id="+inp_user_id

     response = requests.get(URL)
     response_body = response.json()

     assert response_body[0]['name'] == exp_user_name

#TC 3: Verify POST Users request  #####
## Steps:
## 1. Verify 201 Created message is returned
## 2. Verify that the posted data are showing up in the result
@pytest.mark.parametrize('inp_name, inp_username, inp_email, inp_street, inp_suite, inp_city, inp_zipcode, inp_lat, inp_lng, exp_resp_code, exp_id', 
                              [('Dummy Test', 'Dummy.Test', 'dummy.test@gmail.com', 'Main Street', 'Suite 101', 'Rolleston', 
                              '7614', '-12.3456', '78910', 201, 11)])
def test_verify_POST_users_request(inp_name, inp_username, inp_email, inp_street, inp_suite, inp_city, inp_zipcode, inp_lat, inp_lng, exp_resp_code, exp_id):
     data = {
         "name": inp_name,
          "username": inp_username,
          "email": inp_email,
          "address": {
          "street": inp_street,
          "suite": inp_suite,
          "city": inp_city,
          "zipcode": inp_zipcode,
          "geo": {
               "lat": inp_lat,
               "lng": inp_lng
               }
          }
     }
     URL = "https://jsonplaceholder.typicode.com/users"
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

     response = requests.post(URL, json=data, headers = headers)

     #Response code should be 201
     assert response.status_code == exp_resp_code

     response_body = response.json()
     print('response body= ', response_body)

     #Verify that the input details are saved and the same with the data in the response
     assert response_body['name'] == inp_name
     assert response_body['username'] == inp_username
     assert response_body['email'] == inp_email
     assert response_body['address']['street'] == inp_street
     assert response_body['address']['suite'] == inp_suite
     assert response_body['address']['city'] == inp_city
     assert response_body['address']['zipcode'] == inp_zipcode
     assert response_body['address']['geo']['lat'] == inp_lat
     assert response_body['address']['geo']['lng'] == inp_lng

     #Verify the new generated ID
     assert response_body['id'] == exp_id