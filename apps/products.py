from fastapi import APIRouter, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional
from utils.mongo_db import collection_products, serialize_data
from utils.config import LOG


router = APIRouter(tags=["products"])


@router.get("/", description="Get all products")
async def get_all_products(
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, description="Maximum price filter"),
    limit: Optional[int] = Query(
        10, description="Number of items to return per page", ge=1
    ),
    offset: int = Query(0, description="Number of items to skip for pagination"),
):
    LOG.info("get_all_products called")
    status_code = 200
    data = []
    page = {}
    try:
        pipeline = []
        match_stage = {}
        price_range = {}
        if min_price:
            price_range["$gte"] = min_price
        if max_price:
            price_range["$lte"] = max_price
        if price_range:
            match_stage["$match"] = {"price": price_range}
            pipeline.append(match_stage)

        facet_stage = {
            "$facet": {
                "data": [{"$skip": offset}, {"$limit": limit}],
                "page": [
                    {
                        "$count": "total",
                    }
                ],
            }
        }
        pipeline.append(facet_stage)

        result = collection_products.aggregate(pipeline)

        for item in result:
            result = item
        data = serialize_data(result.get("data"))

        if result.get("page"):
            page = result.get("page")[0]
        else:
            page = {"total": 0}
        prevOffset = offset - limit if offset - limit >= 0 else None
        nextOffset = offset + limit if offset + limit < page.get("total") else None

        page.update(
            {"limit": limit, "prevOffset": prevOffset, "nextOffset": nextOffset}
        )
    except Exception as err:
        LOG.error(f"get_all_products failed with error : {err}")
        status_code = 500
    finally:
        return JSONResponse(
            status_code=status_code, content={"data": data, "page": page}
        )


# @router.post("/{product_id}", description="Get a particular product")
# async def get_product(product_id: str = Path(...)):
#     """
#     Code for fetching product with specified product_id
#     """
