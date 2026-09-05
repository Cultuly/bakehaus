import enum


class DeliveryType(str, enum.Enum):
    DELIVERY="delivery"
    PICKUP="pickup"