class Tache:

    def __init__(self, id, duree, deadline=None, priorite=1):
        self.id = id
        self.duree = duree
        self.deadline = deadline
        self.priorite = priorite  # Priorité (1 = faible, 5 = élevée)

    def __repr__(self):
        return f"T{self.id}(d={self.duree})"
