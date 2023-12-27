from sqlalchemy.orm import Session
from fastapi import Depends
from src.database import get_db

from src.timesheets.schemas import User
from src.timesheets.service import TaskService, UserService, TimesheetService


def initiate_task_service(
    db: Session = Depends(get_db),
):
    return TaskService(db=db)


def initiate_user_service(
    db: Session = Depends(get_db),
):
    return UserService(db=db)


def initiate_timesheet_service(
    db: Session = Depends(get_db),
):
    return TimesheetService(db=db)
