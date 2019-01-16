
"""
The event class allows the creation of simple events when needed.
to create a custom event
 'event = Event()'

to subscribe to an event
 'event += function_to_call_on_event'

to call an event
 'event()'
"""
class Event(list):
    # Event subscription
    def __call__(self, *args, **kwargs):
        for f in self:
            f(*args, **kwargs)

    def __repr__(self):
        return "Event(%s)" % list.__repr__(self)

    def __iadd__(self, handler):
        self.append(handler)
        return self

    def __isub__(self, handler):
        self.remove(handler)
        return self