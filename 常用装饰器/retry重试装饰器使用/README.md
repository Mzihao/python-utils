# retry重试装饰器

可用于程序因网络或其他原因发生异常时重试。

## 示例：
```python
# Example
@retry(stop_max_attempt_number=3)  # 最大重试次数，超过后正常抛出异常
def func():
    pass
```