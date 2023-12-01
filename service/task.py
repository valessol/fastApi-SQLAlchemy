from sqlalchemy.orm import Session

from models.models import Task as TaskModel
from models.schemas import TaskCreate

def save_task(db: Session, task: TaskCreate, user_id: int):
    db_item = TaskModel(**task.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_tasks(db: Session, skip: int = 0, limit: int = 100, search: str | None = None):
    if search: return db.query(TaskModel).filter(TaskModel.title.icontains(search.lower()))
    return db.query(TaskModel).offset(skip).limit(limit).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id)


