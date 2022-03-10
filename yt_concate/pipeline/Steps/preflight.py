from .Step import Step


class PreFlight(Step):
    def process(self, data, inputs, utils):
        print("in Preflight")
        utils.create_dirs()
