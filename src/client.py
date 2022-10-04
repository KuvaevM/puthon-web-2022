import grpc
from protobuf.protobuild.OnlineShop_pb2_grpc import ThingsSearcherStub
from protobuf.protobuild.OnlineShop_pb2 import TypeThing


def search_things(sub_name_: str, lower_price_: int, upper_price_: int) -> int:
    """Connects to server, search things"""
    with grpc.insecure_channel('localhost:4000') as channel:
        client = ThingsSearcherStub(channel)
        answer = client.ThingsSearcher(request=TypeThing(sub_name=sub_name_,
                                                         lower_price=lower_price_,
                                                         upper_price=upper_price_))
        return answer.number_things
