from dataclasses import dataclass
from typing import Dict

order_queue = None

@dataclass
class OrderQueue:
    queue: Dict[str, dict]

    def __init__(self):
        self.queue = {}

    def get_order(self, order_id: str):
        return self.queue[order_id]

    def insert(self, order_id: str, order: dict):
        self.queue[order_id] = order

def init_order_queue():
    global order_queue
    if order_queue is None:
        order_queue = OrderQueue()

def get_order_queue():
    return order_queue