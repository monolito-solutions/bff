from fastapi import APIRouter
from upscaler.orders.versioning import detect_order_version
from modules.orders.application.commands.commands import CommandCreateOrder, OrderPayload, CommandGetOrder
from modules.orders.infrastructure.queue import get_order_queue, init_order_queue
from infrastructure.dispatchers import Dispatcher
import utils
import json
import uuid

router = APIRouter(prefix="/orders", tags=["orders"])
init_order_queue()

order_queue = get_order_queue()

@router.post("/", status_code=202)
def create_order(order:dict):
    order = detect_order_version(order)

    command_payload = OrderPayload(
        order_id = str(order.order_id),
        customer_id = str(order.customer_id),
        order_date = str(order.order_date),
        order_status = str(order.order_status),
        order_items = json.dumps(order.order_items),
        order_total = float(order.order_total),
        order_version = int(order.order_version)
    )

    command = CommandCreateOrder(
        time = utils.time_millis(),
        ingestion = utils.time_millis(),
        datacontenttype = OrderPayload.__name__,
        data_payload = command_payload
    )

    dispatcher = Dispatcher()
    dispatcher.publish_message(command, "order-commands")

    return {"message": "Order create accepted"}

@router.get("/")
def get_order(order_id: uuid.UUID):
    try:
        order = order_queue.get_order(order_id)
    except KeyError:
        command_payload = OrderPayload(
            order_id = str(order_id),
            customer_id = "",
            order_date = "",
            order_status = "",
            order_items = "",
            order_total = 0.0,
            order_version = 2
        )

        command = CommandGetOrder(
            time = utils.time_millis(),
            ingestion = utils.time_millis(),
            datacontenttype = OrderPayload.__name__,
            data_payload = command_payload,
        )

        order_queue.insert(order_id, dict())

        dispatcher = Dispatcher()
        dispatcher.publish_message(command, "order-commands")
        return {"message": "Order get accepted, please refresh and wait for the response"}

    if order != dict():
        return {"message": order}
    else:
        return {"message": "Order not yet retreived, please refresh and wait for the response"}