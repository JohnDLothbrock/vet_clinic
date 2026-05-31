from fastapi import (
    APIRouter,
    Depends
)

from services.dashboard_service import (
    DashboardService
)

from app.dependencies import (
    get_dashboard_service
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def get_dashboard(
        dashboard_service: DashboardService = Depends(
            get_dashboard_service
        )
):

    return (
        dashboard_service
        .get_dashboard_data()
    )