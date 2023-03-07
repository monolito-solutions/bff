from fastapi import FastAPI
import uvicorn
import asyncio
from infrastructure.consumers import subscribe_to_topic
from modules.orders.application.commands.commands import CommandCreateOrder
from modules.orders.application.events.events import BffEvent
from modules.orders.infrastructure.queue import init_order_queue
from api.orders.endpoints import router as api_router

app = FastAPI()
app.include_router(api_router)
init_order_queue()

tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(subscribe_to_topic(
        "order-events", "sub-bff", BffEvent))
    task2 = asyncio.ensure_future(subscribe_to_topic(
        "order-commands", "sub-com-bff", CommandCreateOrder))
    tasks.append(task1)
    tasks.append(task2)


@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9009)