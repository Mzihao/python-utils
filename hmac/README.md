Example inputs:

| Variable | Value |
| --- | --- |
| key | `the shared secret key here` |
| message | `the message to hash here ` |

Reference outputs for example inputs above:

| Type | Hash |
| --- | --- |
| as hexit | `4643978965ffcec6e6d73b36a39ae43ceb15f7ef8131b8307862ebc560e7f988` |
| as base64 | `RkOXiWX/zsbm1zs2o5rkPOsV9++BMbgweGLrxWDn+Yg=` |

```python
import hashlib
import hmac
import base64

message = bytes('the message to hash here', 'utf-8')
secret = bytes('the shared secret key here', 'utf-8')

hash = hmac.new(secret, message, hashlib.sha256)

# to lowercase hexits
hash.hexdigest()

# to base64
base64.b64encode(hash.digest())
```
