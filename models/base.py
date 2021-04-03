
class CustomModel:
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)