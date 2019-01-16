
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