from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel

class MySettings(BaseModel):
    api_key: str = ""


@plugin
def settings_model():
    return MySettings
