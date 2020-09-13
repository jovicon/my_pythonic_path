"""
01 - SRP
My notes:
    We have to separete Classes
    We have to avoid God Objects
    Persistance manager is a good way to take Persistance to another level
    Patterns are Good, Anti Patterns are bad
    We have to avoid change code twice
"""

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP
    # ALERT!!!
    # We HAVE TO AVOID THIS
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


# WE KEEP SRP By creating another class to handle Persistence
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = 'journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
