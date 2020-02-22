class event_manager:
    def __init__(self):
        self.subscriptions = {}

    def register(self, topic, callback):
        # print(f'EVENT: {topic} registered')
        if topic not in self.subscriptions:
            self.subscriptions[topic] = []
        self.subscriptions[topic].append(callback)

    def notify(self, time, topic, payload=None):
        print(f'EVENT: time={time:.1f}, topic={topic}, payload={payload}')
        for callback in self.subscriptions[topic]:
            callback(payload)

global_event_manager = event_manager()
