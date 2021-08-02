import logging
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response, responses
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

from django.db import DatabaseError
from redis.exceptions import RedisError

#获取配置文件
logger = logging.getLogger(__name__)


def exception_handler(exc,context):
    """
    自定义异常处理
    :param exec:异常
    :param context:抛出异常上下文
    :param Response 响应对象
    """
    #调用drf异常处理
    response = drf_exception_handler(exc,context)

    if response is None:
        #获取异常视图对象
        view = context['view']

        #判断数据异常
        if isinstance(exc,DatabaseError)   or isinstance(exc,RedisError):
            logger.error('【%s】%s'%(view,type(exc)))
            respone=Response({'messgae':'服务器内部错误'},status=HTTP_500_INTERNAL_SERVER_ERROR)
    return respone    