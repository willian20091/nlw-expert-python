from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "Errors": [{
                "Totle": "Server error",
                "Detail": str(error)
            }]
        }
    )
