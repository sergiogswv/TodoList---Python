from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix='/task',
    responses={404: {'description': 'Not found'}}
)

class Task(BaseModel):
    id: int
    name: str
    finished: str

tasks = [{'id': 1, 'name': "Rick", 'finished': 'false'}, {'id': 2, 'name': "Morty", 'finished': 'true'}]

@router.get("/")
async def getAllTasks():
    return tasks

@router.get('/{task_id}')
async def getOneTask(task_id: int):
    for obj in tasks:
        if task_id != obj['id']:
            if task_id > len(tasks):
                raise HTTPException(status_code=404, detail='Task not found')
        else:
            return obj

@router.post('/', response_model=Task)
async def createNewTask(task: Task):
    if(task.name == ''):
        raise HTTPException(status_code=400, detail='The field name is empty')
    tasks.append(task)
    return task

@router.delete('/{task_id}')
async def deleteTask(task_id: int):
    for obj in tasks:
        if task_id != obj['id']:
            raise HTTPException(status_code=404, detail='Task not found')
        else:
            return {'detail': 'The task '+str(task_id)+' was eliminated successfuly'}

@router.put('/{task_id}')
async def updateTask(task_id: int, task: Task):
    for obj in tasks:
        if task_id != obj['id']:
            raise HTTPException(status_code=404, detail='Task not found')
        else:
            obj = dict(task)
            return {'detail': 'The task ' + str(task_id) + ' was updated successfuly'}