from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntity

def handle_errors(error: Exception) -> HttpResponse:

    if isinstance(error, HttpUnprocessableEntity):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "Errors": [{
                    "Title": error.name,
                    "Detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "Errors": [{
                "Title": "Server error",
                "Detail": str(error)
            }]
        }
    )
