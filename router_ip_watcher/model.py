from typing import Optional

from pydantic import BaseModel


class UserConfigModel(BaseModel):
    class _RouterSection(BaseModel):
        whoami: str
        interval: int
        device: str
        ip: str
        username: str
        password: str

    class _WebhookSection(BaseModel):
        dingtalk: Optional[str]
        wechat: Optional[str]

    class _ResultSection(BaseModel):
        wan_ip: Optional[str]
        change_time: Optional[str]

    router: _RouterSection
    webhook: _WebhookSection
    result: _ResultSection
