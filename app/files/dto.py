import datetime

import pydantic


class FileDTO(pydantic.BaseModel):
    id: int
    filename: str
    path: str
    uploaded_at: datetime.datetime
