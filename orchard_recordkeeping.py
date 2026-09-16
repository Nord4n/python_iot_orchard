#File saving/loading functions for oschard.json

from fileinput import filename
import json
import pathlib
import datetime
from tree import Appletree

DATA_FILE = pathlib.Path("orchard.json")


def save_trees(trees, filename=DATA_FILE):
    """Save the list of trees to a JSON file, along with the year they
    were saved in (used by load_trees to detect a new year)."""
    data = {
        "current_year": datetime.datetime.now().year,
        "trees": [t.to_dict() for t in trees],
    }
    filename.write_text(json.dumps(data, indent=2))
 
 
def load_trees(filename=DATA_FILE):
    """Load the list of trees from a JSON file. Returns an empty list if
    the file doesn't exist yet or is invalid.
 
    If the year stored in the file doesn't match the current year,
    'pruned_this_year' is reset to False for every tree, since pruning
    status should start over each new year."""
    if not filename.exists():
        return []
 
    try:
        data = json.loads(filename.read_text())
    except json.JSONDecodeError:
        print("Warning: could not read data file, starting with an empty orchard.")
        return []
 
    stored_year = data.get("current_year")
    trees_data = data.get("trees", [])
    trees = [Appletree.from_dict(d) for d in trees_data]
 
    current_year = datetime.datetime.now().year
    if stored_year != current_year:
        print(f"New year detected ({current_year}) - resetting pruning status for all trees.")
        for tree in trees:
            tree.pruned_this_year = False
 
    return trees