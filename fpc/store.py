from parapy.core import Base, Input


class Store(Base):
    page: int = Input(0)



STORE = Store()