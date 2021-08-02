from requests.models import Response
from ronglian_sms_sdk import SmsSDK
"""
短信验证码
"""

accId = '8a216da86e011fa3016e36b0dc5718c7' #主账号id

accToken = '263ecf546e7d4ef2ad4ff2ac82bc1b2e' #账户授权令牌
appId = '8a216da86e011fa3016e36b0dcae18cd'


def Ccp():
    sdk = SmsSDK(accId, accToken, appId) #初始化sdk
    return sdk
    

   