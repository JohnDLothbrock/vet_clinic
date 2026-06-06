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

from auth.current_user import (
    require_authenticated_user
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
        current_user=Depends(
            require_authenticated_user
        ),
        dashboard_service: DashboardService = Depends(
            get_dashboard_service
        )
):

    return (
        dashboard_service
        .get_dashboard_data()
    )