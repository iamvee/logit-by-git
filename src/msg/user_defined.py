class AType(BaseMessageType):
    repr_str = "{amount}"
    pattern = r"\s*[aA](\d+)\s*"

    def __init__(self, val):
        self.val = int(val)
