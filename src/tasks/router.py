from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from configuration import collection
from src.database.models import Task
from src.database.schemas import all_tasks, individual_data
from bson import ObjectId


task_router = APIRouter()

@task_router.get("/root")
async def read_root():
    return {"message": "hi"}

@task_router.get("/")
async def read_all_tasks():
    data = collection.find( )
    return all_tasks(data)

@task_router.get("/{task_id}")
async def read_task(task_id: str):
    task_id = ObjectId(task_id)
    data = collection.find_one({"_id": task_id})
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"status code":status.HTTP_200_OK,"id": individual_data(data)["id"] ,"data": individual_data(data)}


@task_router.post("/create")
async def create_task(new_task: Task):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status code":status.HTTP_201_CREATED,"id": str(resp.inserted_id), "data": new_task}
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Some error accured {e}")

@task_router.put("/update/{task_id}")
async def update_task(task_id: str, update_task: Task):
    try:
        # Convert task_id to ObjectId if necessary
        task_id = ObjectId(task_id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task ID format")

    try:
        # Check if the task exists
        data = collection.find_one({"_id": task_id})
        if data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        
        # Update the task
        update_result = collection.update_one(
            {"_id": task_id},
            {"$set": update_task.dict()}
        )
        
        # Check if the update matched any documents
        if update_result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

        # Return the updated task information
        return {
            "status_code": status.HTTP_202_ACCEPTED,
            "id": str(task_id),
            "data": update_task.dict()
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {e}"
        )
    
@task_router.delete("/delete/{task_id}")
async def delete_task():
    pass
