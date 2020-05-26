all_corporations = []

class corporation:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        all_corporations.append(self)

    def add(self, member):
        if not isinstance(member, list):
            member = [member,]
        for m in member:
            self.members.append(m)
            m.corporation = self

    def remove(self, member):
        self.members.remove(member)

    def __getitem__(self, k):
        return self.members[k]

    def __setitem__(self, k, v):
        self.members[k] = v

    def __delitem__(self, k):
        self.members.remove(k)

