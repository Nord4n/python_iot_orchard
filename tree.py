
class Appletree:
    """Represents a single apple tree in the orchard."""

    def __init__(self, tree_id, variety, planted_year, harvest_time="",
                 problems=None, pruned_this_year=False):
        self.tree_id            = tree_id
        self.variety            = variety
        self.planted_year       = planted_year
        self.harvest_time       = harvest_time
        self.problems           = problems if problems is not None else []
        self.pruned_this_year   = pruned_this_year

    def to_dict(self):
        """Convert this Appletree object into a plain dict (for saving as JSON)."""
        return {
            "tree_id":          self.tree_id,
            "variety":          self.variety,
            "planted_year":     self.planted_year,
            "harvest_time":     self.harvest_time,
            "problems":         self.problems,
            "pruned_this_year": self.pruned_this_year,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Tree object from a dict (loaded from JSON)."""
        return cls(
            data["tree_id"],
            data["variety"],
            data["planted_year"],
            data.get("harvest_time", ""),
            data.get("problems", []),
            data.get("pruned_this_year", False),
        )

    def __str__(self):
        problems_str = ", ".join(self.problems) if self.problems else "None"
        pruned_str = "Yes" if self.pruned_this_year else "No"
        return (
            f"[{self.tree_id}] {self.variety} "
            f"(planted {self.planted_year}) | "
            f"Harvest: {self.harvest_time or 'unknown'} | "
            f"Problems: {problems_str} | "
            f"Pruned this year: {pruned_str}"
        )
