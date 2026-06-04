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

from api.schemas.dashboard_schema import (
    DashboardResponse
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "",
    response_model=DashboardResponse
)
def get_dashboard(
        dashboard_service: DashboardService = Depends(
            get_dashboard_service
        )
):

    return (
        dashboard_service
        .get_dashboard_data()
    )