import functools

code_msg = {
    200: "SUCCESS",
    500: "FAIL",
}


def response_json(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        code, data = f(*args, **kwargs)
        json = {
            "code": code,
            "message": get_error_msg(code),
            "data": data,
        }
        return json

    return decorator


def get_error_msg(code: int) -> str:
    return code_msg[code]


# Example
@response_json
def func():
    return 200, []


print(func())
# {'code': 200, 'message': 'SUCCESS', 'data': []}