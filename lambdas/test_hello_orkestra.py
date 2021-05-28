from dataclasses import dataclass

import pytest

from hello_orkestra import (
    generate_item,
    add_price,
    copy_item,
    double_price,
    Item,
    assert_false,
    do_nothing,
    say_hello,
    say_goodbye,
    random_int,
    random_float,
)


@pytest.fixture
def event():
    return Item.random().dict()


@pytest.fixture
def context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"
        aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

    return LambdaContext()


class TestMethods:
    @staticmethod
    def test_generate_item(event, context):
        generated = generate_item(event, context)
        assert Item(**generated)

    @staticmethod
    def test_add_price(event, context):
        result = add_price(event, context)
        assert result["price"]

    @staticmethod
    def test_copy_item(event, context):
        result = copy_item(event, context)
        assert all(i == event for i in result)

    @staticmethod
    def test_double_price(event, context):
        event["price"] = 1
        result = double_price(event, context)
        assert result["price"] == event["price"] * 2

    @staticmethod
    def test_assert_false(event, context):
        with pytest.raises(AssertionError):
            assert_false(event, context)

    @staticmethod
    def test_do_nothing(event, context):
        assert do_nothing(event, context) is None

    @staticmethod
    def test_say_hello(event, context):
        assert say_hello(event, context)

    @staticmethod
    def test_goodbye(event, context):
        assert say_goodbye(event, context)

    @staticmethod
    def test_random_int(event, context):
        result = random_int(event, context)
        assert isinstance(result, int)

    @staticmethod
    def test_random_float(event, context):
        result = random_float(event, context)
        assert isinstance(result, float)
