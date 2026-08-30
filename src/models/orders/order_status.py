import enum


# Order statuses
class OrderStatus(str, enum.Enum):
    PENDING="pending"
    PROCESSING="processing"
    IN_PROGRESS="in-progress"
    DELIVERED="delivered"
    CANCELED="canceled"