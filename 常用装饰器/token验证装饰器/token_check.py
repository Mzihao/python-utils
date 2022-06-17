import time
import jwt
import uuid
import functools


class Token:
    @classmethod
    def encrpyt_token(cls, username, exp_time=None, secret=None):
        """
        jwt加密
        :param username:
        :param exp_time:
        :param secret:
        :return:
        """
        if not exp_time:
            exp_time = time.time() + 60 * 30

        if not secret:
            secret = 'ngt777'

        payloads = {
            'iss': 'ngt777 Is The JWT\'s Builder',  # 该JWT的签发者，是否使用是可以选择的。
            # 'sub': '',  # sub：该JWT所面向的用户，是否使用是可选的。
            # 'aud': '',  # aud：接收该JWT的一方，是否使用是可选的。
            'iat': time.time(),  # iat（issued at）：在什么时候签发UNIX时间，是否使用是可选的。
            'username': username,
            'uuid': str(uuid.uuid1()),
            "exp": exp_time,  # exp（expires）：什么时候过期，是一个UNIX的时间戳，是否使用是可选的。默认设置为：30分钟
            # "nbf": ""  # nbf（not before）：如果当前时间在nbf的时间之前，则Token不被接受，一般都会留几分钟，是否使用是可选的。
        }
        encoded_jwt = jwt.encode(payloads, secret, algorithm='HS256')
        return encoded_jwt

    @classmethod
    def decrypt_token(cls, token, secret=None):
        """
        jwt解密
        :param token:
        :param secret:
        :return:
        """
        try:
            if not secret:
                secret = 'ngt777'
            decode_jwt = jwt.decode(token, secret, algorithms=['HS256'])

            return decode_jwt
        except jwt.exceptions.InvalidSignatureError as e:
            return {'error': 'Signature verification failed'}


def access_token_required():
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # token = "一般从请求头获取"
            token = Token().encrpyt_token('martin')
            decryptToken = Token().decrypt_token(token)
            if token and decryptToken.get('username') == '111':
                return f(*args, **kwargs)
            else:
                raise {'error': 'token verification failed!'}

        return wrapper

    return decorator


# Example
@access_token_required
def func():
    return 
