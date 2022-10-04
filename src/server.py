import grpc
from concurrent.futures import ThreadPoolExecutor
from protobuf.protobuild.OnlineShop_pb2_grpc import ThingsSearcherServicer, add_ThingsSearcherServicer_to_server
from protobuf.protobuild.OnlineShop_pb2 import Answer
from content import Thing
from db import db_things


class Service(ThingsSearcherServicer):
    def ThingsSearcher(self, request, context):
        """Search things with given filter request.

        Args:
            request (TypeThing): price range, sub_name

        Returns:
            Answer : number of fitting things
        """
        # print(len(db_things))
        list_of_things = [thing for thing in db_things if
                          ((request.sub_name in thing.thing_name)
                           and (request.lower_price < thing.thing_cost
                                < request.upper_price))]
        return Answer(number_things=len(list_of_things))


def start_server():
    """Starts server."""
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_ThingsSearcherServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:4000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    start_server()
