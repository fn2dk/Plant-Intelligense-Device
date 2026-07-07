from fastapi import APIRouter

router = APIRouter()


@router.get("")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "engineering-intelligence-api",
        "version": "0.3.0",
    }
