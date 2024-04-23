import logging
import requests
import user_agents

from django.http import HttpResponse
from django.conf import settings


logger = logging.getLogger('fancy-shop-logger')


class SetUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        request.user_agent = user_agents.parse(request.META.get("HTTP_USER_AGENT"))
        logger.info("Current user-agent for {} is {}".format(request.user, request.user_agent))
        return self.get_response(request)


class BlockEdgeBrowserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.user_agent.is_mobile == 'mobile':
            logger.error("Mobile browsers are  not allowed")
            return HttpResponse("<h3>Mobile browsers is not allowed</h3>", status=400)
        return self.get_response(request)


class ErrorHandlerHelperMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if settings.DEBUG:
            excetion_classname = exception.__class__.__name__

            url = "https://api.stackexchange.com/2.3/search"
            params = {
                "order": "desc",
                "sort": "votes",
                "pagesize": 3,
                "site": "stackoverflow",
                "intitle": excetion_classname,
                "tagged": "django"
            }
            resp = requests.get(url, params=params)
            if resp.ok:
                questions = resp.json()

            for question in questions["items"]:
                print(question["title"])
                print(question["link"])
                print(" ")
        return None

# class Middleware:
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
#     def process_views(self, view_func, *args, **kwargs):
#         pass
#
#     def process_exceptions(self, request, exception):
#         pass
#
#     def process_response(self, request, response):
#         pass
