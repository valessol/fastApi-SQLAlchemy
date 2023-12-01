from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from service.db_connection import get_db
from models.schemas import TaskCreate, Task, TaskBase
from service import task as crud

router = APIRouter()

@router.post("/todos/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.save_task(db=db, task=task)


@router.get("/todos/", response_model=list[Task])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), search: str | None = None):
    tasks = crud.get_all_tasks(db, skip=skip, limit=limit, search=search)
    return tasks


@router.get("/todos/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put('/todos/{task_id}', response_model=Task)
def update_task(task_id: int, task: TaskBase, db: Session = Depends(get_db)):
    ...


@router.delete('/todos/{task_id}', response_model=Task)
def update_task(task_id: int, db: Session = Depends(get_db)):
    ...