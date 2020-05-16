import re


class BaseMessageType:
    subs = []
    repr_str: str = "BASE TYPE "
    pattern: str = ""


    def __init_subclass__(cls, *args, **kwargs):
        cls.subs.append(cls)
        super().__init_subclass__(*args, **kwargs)


    def __repr__(self):
        cls_name = self.__class__.__name__
        text = "{cls_name} {self.repr_str}"
        return text.format(cls_name=cls_name, **self.__dict__)


    @classmethod
    def check(cls, msg):
        _res = re.findall(cls.pattern, msg)
        if not _res:
            return None
        else:
            return cls(_res[0])
