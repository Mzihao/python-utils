# 统一响应装饰器decorator

在api接口服务中减少代码耦合，统一响应格式。

## 示例：
```python
# Example
@response_json
def func():
    return 200, []


print(func())
# {'code': 200, 'message': 'SUCCESS', 'data': []}
```