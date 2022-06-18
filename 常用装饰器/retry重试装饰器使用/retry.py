from retrying import retry

'''
retry参数说明：
retry(wait_fixed=1000)  # 设置重试间隔时长（ms  1000ms = 1s）
retry(wait_random_min=1000, wait_random_max=2000, )  # 随机重试间隔，将在1～2s内
retry(stop_max_attempt_number=3)  # 最大重试次数，超过后正常抛出异常
retry(stop_max_delay=2000)  # 最大延迟时长，2s内未满足条件则抛出异常
retry(retry_on_exception=自定义函数)  # 当发生指定异常时会执行函数
retry(retry_on_result=自定义函数)  # 每次都会执行函数，当返回返回True就重试，否则异常退出
'''

@retry(stop_max_attempt_number=3)  # 最大重试次数，超过后正常抛出异常
def func():
    pass
