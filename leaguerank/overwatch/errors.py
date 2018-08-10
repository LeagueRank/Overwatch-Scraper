
class PrivateProfile(Exception):
    def __init__(self):
        super(PrivateProfile, self).__init__("This profile is private.")


class NoData(Exception):
    def __init__(self):
        super(NoData, self).__init__("Overwatch returned no data.")
