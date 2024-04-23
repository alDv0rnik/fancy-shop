import logging
import user_agents
from django.http import HttpResponse


logger = logging.getLogger('fancy-shop-logger')


class SetUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        request.user_agent = user_agents.parse(request.META.get('HTTP_USER_AGENT', ''))
        msg = "Current User Agent for {} is {}".format(request.user, request.user_agent)
        logger.info(msg)
        return self.get_response(request)


class BlockMobileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.user_agent.browser.family == 'Chrome':
            logger.error("Mobile devices are not supported")
            return HttpResponse("Mobile devices are not supported", status=400)
        return self.get_response(request)