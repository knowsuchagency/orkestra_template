import random
from typing import *
from uuid import uuid4

from aws_lambda_powertools import Logger, Tracer
from pydantic import BaseModel

from orkestra import compose
from orkestra.interfaces import Duration


class Item(BaseModel):
    id: str
    name: str
    price: Optional[float] = None

    @classmethod
    def random(cls):
        return cls(
            id=str(uuid4()),
            name=random.choice(
                [
                    "potato",
                    "moon rock",
                    "hat",
                ]
            ),
        )


logger = Logger()

tracer = Tracer()


default_args = dict(
    enable_powertools=True,
    timeout=Duration.seconds(6),
)


@compose(**default_args)
def generate_item(event, context):
    logger.info("generating random item")
    item = Item.random().dict()
    logger.info(item)
    tracer.put_metadata("GenerateItem", "SUCCESS")
    return item


@compose(model=Item, **default_args)
def add_price(item: Item, context):
    price = 3.14
    logger.info(
        "adding price to item",
        extra={
            "item": item.dict(),
            "price": price,
        },
    )
    item.price = price
    return item.dict()


@compose(model=Item, **default_args)
def copy_item(item: Item, context) -> list:
    logger.info(item.dict())
    return [item.dict()] * 10


@compose(model=Item, is_map_job=True, **default_args)
def double_price(item: Item, context):
    item.price = item.price * 2
    return item.dict()


@compose(**default_args)
def assert_false(event, context):
    assert False


@compose(**default_args)
def do_nothing(event, context):
    logger.info({"doing": "nothing"})


@compose(**default_args)
def say_hello(event, context):
    return "hello, world"


@compose(**default_args)
def say_goodbye(event, context):
    return "goodbye"


@compose(**default_args)
def random_int(event, context):
    return random.randrange(100)


@compose(**default_args)
def random_float(event, context):
    return float(random_int(event, context))


(
    generate_item
    >> add_price
    >> copy_item
    >> double_price
    >> (do_nothing, assert_false)
    >> say_hello
    >> [random_int, random_float]
    >> say_goodbye
)
