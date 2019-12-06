class Monster():

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def sleep(self):
        return 'zzzz'

    def eat(self):
        return 'nom nom'

    def scare_attack(self):
        return 'RAAAHHH'

    def add_skills(self, skills):
        the_monster_in_question = self
        the_monster_in_question.skills.append(skills)
