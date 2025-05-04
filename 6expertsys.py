class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = {}

    def add_fact(self, fact, value):
        self.facts[fact] = value

    def add_rule(self, conclusion, conditions):
        self.rules[conclusion] = conditions

    def infer(self):
        for conclusion, conditions in self.rules.items():
            if all(self.facts.get(fact) == value for fact, value in conditions.items()):
                return conclusion
        return "Performance could not be evaluated with the given data."


# Create system instance
expert = ExpertSystem()

# Ask user to enter facts
print("Please answer the following questions with 'yes' or 'no':")

facts_list = [
    "punctual",
    "targets_met",
    "team_player",
    "takes_initiative"
]

# Collect user input
for fact in facts_list:
    answer = input(f"Is the employee {fact.replace('_', ' ')}? (yes/no): ").strip().lower()
    expert.add_fact(fact, answer == 'yes')

# Define rules
expert.add_rule("Excellent Performance", {
    "punctual": True,
    "targets_met": True,
    "team_player": True,
    "takes_initiative": True
})

expert.add_rule("Good Performance", {
    "punctual": True,
    "targets_met": True,
    "team_player": True
})

expert.add_rule("Needs Improvement", {
    "punctual": False,
    "targets_met": False
})

# Inference
result = expert.infer()
print("\n🔍 Performance Evaluation Result:", result)
