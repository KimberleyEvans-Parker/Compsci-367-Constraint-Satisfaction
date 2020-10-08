import random
from .utils import argmin_random_tie


# ______________________________________________________________________________
# Min-conflicts Hill Climbing search for CSPs
num_assignments = 0
num_repair_assignments = 0
a = 0


def min_conflicts(csp, max_steps=100000):
    """Solve a CSP by stochastic Hill Climbing on the number of conflicts."""
    global num_assignments
    global num_repair_assignments
    num_assignments = 0
    num_repair_assignments = 0

    global a
    a = 0

    # Generate a complete assignment for all variables (probably with conflicts)
    csp.current = current = {}
    for var in csp.variables:
        val = min_conflicts_value(csp, var, current)
        csp.assign(var, val, current)
        num_assignments += 1
        a += 1
    # Now repeatedly choose a random conflicted variable and change it
    for i in range(max_steps):
        conflicted = csp.conflicted_vars(current)
        if not conflicted:
            return current
        var = random.choice(conflicted)
        val = min_conflicts_value(csp, var, current)
        num_assignments += 1
        num_repair_assignments += 1
        csp.assign(var, val, current)
    return None


def min_conflicts_value(csp, var, current):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    return argmin_random_tie(csp.domains[var], key=lambda val: csp.nconflicts(var, val, current))
