class DocumentAlreadyExists(Exception):
    def __init__(self):
        super().__init__('DocumentAlreadyExists')
