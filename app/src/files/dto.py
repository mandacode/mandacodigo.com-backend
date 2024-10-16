import datetime

import pydantic


class FileDTO(pydantic.BaseModel):
    id: int
    filename: str
    url: str
    uploaded_at: datetime.datetime
