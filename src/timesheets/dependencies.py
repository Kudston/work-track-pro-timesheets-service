from sqlalchemy.orm import Session
from fastapi import Depends
from src.database import get_db_sess
from src.dependencies import get_current_active_user
from src.security import oauth2_scheme
from src.service import get_settings
from src.config import Settings
from src.timesheets.schemas import User
from src.timesheets.service import TimesheetService


def initiate_timesheet_service(
    db: Session = Depends(get_db_sess),
):
    return TimesheetService(db=db)
