from django.http import HttpResponse

class InterceptMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/":
            return HttpResponse("The Project is now on live", content_type="text/plain")
        
        if request.path == "/health":
            return HttpResponse("The API is live. Please check and test the api.", content_type="text/plain")
        
        return self.get_response(request) 