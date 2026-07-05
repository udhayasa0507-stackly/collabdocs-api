import time


class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time.time()

        response = self.get_response(request)

        end = time.time()

        execution_time = round((end - start) * 1000, 2)

        print(
            f"""
=========================================
HTTP Method : {request.method}
Path        : {request.path}
Status Code : {response.status_code}
Time Taken  : {execution_time} ms
=========================================
"""
        )

        return response