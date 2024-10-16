import dataclasses
import datetime


@dataclasses.dataclass
class File:
    filename: str
    url: str
    uploaded_at: datetime.datetime = dataclasses.field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
