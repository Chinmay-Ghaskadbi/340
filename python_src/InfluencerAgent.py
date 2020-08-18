from mesa import Agent
from randomGenerator import uniformRandomGenerator

class InfluencerAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        self.out_degree = 0
        self.decision = False
        self.interest = uniformRandomGenerator(0, 1)

    def get_outDegree(self):
        return self.out_degree

    def set_outDegree(self, out_degree):
        self.out_degree = out_degree

    def get_interest(self):
        return self.interest

    def get_decision(self):
        return self.decision

    def update_interest(self, influence):
        self.interest = self.interest + (self.interest*influence)**2

    def make_decision(self, influence):
        return uniformRandomGenerator(0, 1) < self.interest*influence