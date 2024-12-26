# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import os
from dotenv import load_dotenv

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "baf5b460-1478-4a11-90c7-84a4ea5036c6"
FLOW_ID = "982d4184-8457-46c2-b2e1-ab85051a7446"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "customer_test" # The endpoint name of the flow


def run_flow(message: str) -> dict:
   
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
  
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

result = run_flow("what are the shipment times")
print(result)