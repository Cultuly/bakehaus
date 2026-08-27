import enum


# Order statuses
class OrderStatus(str, enum.Enum):
    PENDING="pending"
    DELIVERED="delivered"
    CANCELED="canceled"