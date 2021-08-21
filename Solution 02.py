import requests
import json


# Function definition
def UserCount(total_pages):
    """
    function to go through all pages and find the total number of users

    Parameters:
    total_pages (int): total number of pages to go through

    Returns:
    int: Total number of users registered

    """
    total_users=0
    for page in range(total_pages):
        response_users = requests.get("https://reqres.in/api/users?page="+str(page+1)).text
        users = json.loads(response_users)
        total_users= total_users+ len(users['data'])
    return total_users
        
# Function usage
user_count= UserCount(12)
print(user_count)