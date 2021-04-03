from django.db import models
from django.contrib.auth get_user_model

AuthUserModel = get_user_model()

# create the models here
class User(models.Model):
    __tablename__ = 'users'
    first_name = Column(VARCHAR(255), Field.null = False)
    last_name = Column(VARCHAR(255), Field.null = False)
    email = Column(VARCHAR(255), Field.null = False, unique=True)
    addresses = relationship('Address')
    shipping_address_id = (INTEGER, ForeignKey(Address.id))


class UserOrder(AuthUserModel):
    __tablename__ = 'user_order '
    __table_args__ = (UniqueConstraint('user_id', 'order_id'),)

    user_id = Column(INTEGER, ForeignKey(User.id))
    order_id = Column(INTEGER, ForeignKey(Order.id))
    user = relationship(User, backref=backref('user_roles', cascade='all, delete-orphan'))
    order = relationship(Order, backref=backref('user_order', cascade='all, delete-orphan'))


class Address(AuthUserModel):
    __tablename__ = 'addresses'
    __table_args__ = (UniqueConstraint('user_id', 'type'),)

    user_id = Column(INTEGER, ForeignKey(User.id))
    user = relationship(User, backref='addresses')

    # The following Enum is used in setting the `addresses.type` field.
    # This can have only the value of SHIPPING or BILLING.

    class Types(enum.Enum):
        SHIPPING = SHIPPING_ADDRESS
        BILLING = BILLING_ADDRESS
    type = Column(Enum(Types))

    street = Column(VARCHAR(255), Field.null = False)
    city = Column(VARCHAR(255), Field.null = False)
    country = Column(VARCHAR(255), Field.null = False)