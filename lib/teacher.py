#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        if not self.knowledge:
            return "I have no knowledge to share"
        else:
            return random.choice(self.knowledge)