from meiduo.apps import contents
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django_redis import get_redis_connection
from rest_framework import status
import random
from meiduo.utils.smscode import Ccp
from verifications import constants

# Create your views here.
class SMSCode(APIView):
    """
    短信验证码
    """
    def get(self,request,mobile):
        """

        获取短信验证码

        """
        #判读图片验证码,判断是否在60秒内
        redis_conn = get_redis_connection('verify_codes')
        send_flag  = redis_conn.get('send_flag_%s'%mobile)
        if send_flag:
            return Response({'message':'请求次数过于频繁'},status=status.HTTP_400_BAD_REQUEST)


        #生成短信验证码
        sms_code = '%06d'%random.randint(0,999999)

        #存入短信验证码
        #  创建redis管道对象
        p1 = redis_conn.pipeline()
        #存入一些记录信息
        p1.setex('sms_%s'%mobile,constants.SMS_CODE_REDIS_EXPIRES,sms_code)
        p1.setex("send_flag_%s" % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)

        #一次执行redis管道命令
        p1.execute()

        #发送短信验证码
        sms_code_expire = constants.SEND_SMS_CODE_INTERVAL//60
        try:
            ccp = Ccp()
            #调用发送短信
            tid = '001'
            datas = sms_code
            res = ccp.sdk.sendMessage(tid,mobile, datas)
            
         
        except Exception as e:
            return Response({'message':'短信发送异常'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if res != 0:
          return Response({"message": "发送短信失败"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({"message": "短信验证码发送成功"})     





