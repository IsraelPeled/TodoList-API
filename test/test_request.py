import requests
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
ENDPOINT = os.getenv("DOMAIN_DEV")
'''
response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)
'''

def test_can_call_endpoint():
    response  = requests.get(ENDPOINT)
    assert response.status_code == 200


#FIXME: need fix create_task
def test_can_create_character():
    payload = new_task_payload()
    create_response = create_task(payload)
    assert create_response.status_code == 200

    data = create_response.json()
    #print(data)




def create_task(payload: dict):
    return requests.post(ENDPOINT+'/create', json=payload)

def get_task(task_id: str):
    return requests.get(ENDPOINT + f"/{task_id}")

def update_task(task_id: str, payload: dict):
    return requests.put(ENDPOINT + f'/update/{task_id}', json=payload)

def delete_task(task_id: str):
    return requests.delete(ENDPOINT + f'/delete/{task_id}')


def new_task_payload(
        title="a",
        description="b",
        is_completed=False,
        is_deleted=False,
        created_at = int(datetime.timestamp(datetime.now())),
        updated_at = int(datetime.timestamp(datetime.now()))):
    payload = {
        "id": id,
        "title": title,
        "description": description,
        "is_completed": is_completed,
        "is_deleted": is_deleted,
        "created_at": created_at,
        "updated_at": updated_at
    }
    return payload