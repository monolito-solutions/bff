from pulsar.schema import *
from utils import time_millis
import uuid


class OrderPayload(Record):
    order_id = String()
    customer_id = String()
    order_date = String()
    order_status = String()
    order_items = String()
    order_total = Float()
    order_version = Long()


class CommandCreateOrder(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v2")
    type = String(default="CommandCreateOrder")
    datacontenttype = String()
    service_name = String(default="bff.entregasalpes")
    data_payload = OrderPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandGetOrder(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v2")
    type = String(default="CommandGetOrder")
    datacontenttype = String()
    service_name = String(default="bff.entregasalpes")
    data_payload = OrderPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)