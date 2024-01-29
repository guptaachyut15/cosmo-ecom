from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.order import Order
from utils.mongo_db import collection_orders
from utils.config import LOG

router = APIRouter(tags=["orders"])


# @router.get("/")
# async def get_all_orders():
#     """
#     Logic to get all placed orders
#     """


@router.post("/")
async def upload_order(order: Order):
    LOG.info("upload_order called")
    status_code = 201
    content = {"status": "success"}
    try:
        result = collection_orders.insert_one(order.model_dump())
        content["id"] = str(result.inserted_id)
    except Exception as err:
        status_code = 500
        content = {"status": "failed", "message": err}
    finally:
        return JSONResponse(status_code=status_code, content=content)
