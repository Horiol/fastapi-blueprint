from sqlalchemy import BigInteger, Column
from sqlalchemy.orm import as_declarative, declared_attr

class_registry: dict = {}


@as_declarative(class_registry=class_registry)
class Base(object):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    @declared_attr
    def id(self):
        return Column(BigInteger, primary_key=True, index=True)
