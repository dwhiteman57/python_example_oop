class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def setNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."


class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickup_policy(self):
    return self.pickupPolicy

  def __repr__(self):
    return super().__repr__() + f" The pickup policy is {self.pickupPolicy}."


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sports_teams(self):
    return self.sportsTeams

  def __repr__(self):
    return super().__repr__() + f" Sports teams include {self.sportsTeams}."




s1 = School("Clark Middle School", "Middle", 450)
# print(s1.get_level())
s1.setNumberOfStudents(900)
# print(s1.get_numberOfStudents())
# print(s1.__repr__())


p1 = PrimarySchool("Bibich", 300, "Pickup not allowed")
# print(p1.get_pickup_policy())
# print(p1.__repr__())

h1 = HighSchool("Lake Central", 2000, ["Soccer, Football"])
print(h1.get_sports_teams())
print(h1.__repr__())

