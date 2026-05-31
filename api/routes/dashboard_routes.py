from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def get_dashboard():

    return {

        "total_owners": 2,
        "total_pets": 4,
        "total_appointments": 3
    }

