from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    根路由的异步处理函数，返回一个简单的欢迎消息。

    Returns:
        dict: 包含欢迎消息的字典，键为'message'，值为'Hello World'。
    """
    return {"message": "Hello World"}


@app.get("/hello/")
async def hello():
    """
    异步端点，用于返回欢迎消息。

    该函数不接受任何参数，并返回一个包含欢迎消息的JSON对象。
    函数定义为异步函数，以异步方式处理请求，提高服务器性能。

    返回:
        dict: 包含键 'message' 和其对应的欢迎字符串的字典。
    """
    return {"message": "Hello, you are welcome."}


@app.get("/say_hello_to_name/{name}")
async def say_hello_to_name(name: str):
    """
    根据提供的名称返回个性化的问候消息。

    此函数是一个异步FastAPI端点，它通过URL路径参数{name}接收用户的名称，
    然后返回一个包含该名称的问候消息。这种方式允许创建动态的、个性化的
    问候，同时通过异步处理提高服务器的响应效率。

    参数:
    - name (str): 通过URL路径提供的用户名称。

    返回:
    - dict: 包含问候消息的字典，消息中包含提供的名称。
    """
    return {"message": f"Hello, {name}"}


class Gender(str, Enum):
    """
    定义性别枚举类，继承自str和Enum类。

    为什么需要这个类：
    通过创建Gender枚举类，我们可以确保性别值的正确性和一致性，避免拼写错误或不一致的表示。

    属性说明：
    - male: 代表男性，值为"male"
    - female: 代表女性，值为"female"

    这种设计使得在代码中使用性别信息时更加直观和统一。
    """
    male = "male"
    female = "female"


@app.get("/say_hello_to_gender/{gender}")
async def say_hello_to_gender(gender: Gender):
    """
    根据性别问候用户。

    该端点接受一个性别参数，并根据用户的性别返回个性化的问候消息。

    参数:
    - gender: 指定用户的性别，可以是Gender枚举类型的male或female。

    返回:
    - 如果性别为male，返回一个包含问候男性消息的字典。
    - 如果性别为female，返回一个包含问候女性消息的字典。
    """
    # 检查性别是否为男性
    if gender is Gender.male:
        # 返回问候男性的消息
        return {"message": "Hello, you are a man."}
    # 检查性别是否为女性
    elif gender is Gender.female:
        # 返回问候女性的消息
        return {"message": "Hello, you are a woman."}
