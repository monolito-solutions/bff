from dataclasses import asdict
from pulsar.schema import *
from utils import time_millis
import uuid

class QueryMessage(Record):
    order_id = String()
    type = String(default="message")
    payload = String()

class BffEventPayload(Record):
    id = String(default=str(uuid.uuid4()))
    order_id = String()
    customer_id = String()
    order_date = String()
    order_status = String()
    order_items = String()
    order_total = Float()
    order_version = Long()

    def to_dict(self):
        return {
            "order_id": str(self.order_id),
            "customer_id": str(self.customer_id),
            "order_date": str(self.order_date),
            "order_status": str(self.order_status),
            "order_items": str(self.order_items),
            "order_total": float(self.order_total),
            "order_version": int(self.order_version)
        }


class BffEvent(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v2")
    type = String(default="BffEvent")
    datacontenttype = String()
    service_name = String(default="bff.entregasalpes")
    data_payload = BffEventPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
