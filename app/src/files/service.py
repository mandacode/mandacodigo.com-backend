from . import model


class UploadFileService:

    def __init__(self, db):
        self.db = db

    def execute(self, filename: str, url: str) -> model.File:
        file = model.File(filename=filename, url=url)
        self.db.add(file)
        self.db.commit()
        return file
