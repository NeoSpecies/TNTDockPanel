from flask import request


def teardown_request(exception=None):
    # 如果有异常可以在这里处理
    if exception:
        print(f"Exception occurred: {exception}")
    # 在这里执行清理工作
    print("Teardown request...")
