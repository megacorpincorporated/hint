import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class HomeConsumer(WebsocketConsumer):
    """Allows frontend users to subscribe to events related to a Home"""


    def __init__(self, *args, **kwargs):
        """"""
        self.home_ids = []
        super().__init__(*args, **kwargs)

    def connect(self):
        """
        TODO On connection, accept the connection. Authentication checks should
        already have been made?
        """
        print("Connected to HomeConsumer")

        self.accept()

    def disconnect(self, close_code):
        """
        Not strictly necessary, but spares performance to discard the home_id
        group add on disconnect. If this is not done, or fails, a timeout will
        take care of the cleanup at some point.
        """
        print("Disconnected from HomeConsumer")

        for home_id in self.home_ids:
            async_to_sync(self.channel_layer.group_discard)(
                home_id, self.channel_name
            )

    def receive(self, text_data=None):
        """
        Called on receiving an event from the socket connection. Currently, the
        only expected event is a subscription for a home ID.

        :param text_data: JSON formatted string
        """
        print(f"New home consumer message: {json.loads(text_data)}")
        decoded_data = json.loads(text_data)

        # TODO remove
        if decoded_data.get("testing"):
            self.send(json.dumps(
                {
                    "home_id": decoded_data["home_id"],
                    "hume_uuid": decoded_data["hume_uuid"],
                }
            ))
            return

        home_id = str(decoded_data["home_id"])
        self.home_ids.append(home_id)
        print(f"Currently monitored home_ids: {self.home_ids}")
        async_to_sync(self.channel_layer.group_add)(
            home_id, self.channel_name
        )

    def home_event(self, event):
        """
        Called when an event occurs for a particular home through:

        async_to_sync(channel_layer.group_send)(
            "1337",  # This is the home id (group name)
            {
                "type": "home.event",  # Ensures the home_event def is called
                ...
            }
        )

        :param event: contains event information to be propagated to websocket
                      listener. Format of the event can be found in the
                      consumer_views module in the broker app
        :type event: dict
        """
        def format_event(event):
            """
            Formats an incoming event for dispatch to a websocket client.

            :param event: dict with event information
            :returns: formatted JSON string
            """
            event.pop("type")
            return json.dumps(event)
        self.send(format_event(event))
