from fastapi import APIRouter, BackgroundTasks, Depends

from auth.base_config import current_user

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    """Using Celery to Send Registration Confirmation Emails"""

    # 1400 ms - The client is waiting
    send_email_report_dashboard(user.username)
    # 500 ms - The task is executed against the background of FastAPI in the event loop or in another thread
    background_tasks.add_task(send_email_report_dashboard, user.username)
    # 600 ms - The task is executed by the Celery worker in a separate process
    send_email_report_dashboard.delay(user.username)
    return {"status": 200, "data": "Письмо отправлено", "details": None}
