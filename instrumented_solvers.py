from textbook.backtracking_search_solver import *
from textbook.min_conflicts_solver import *

#####################
# Your imports here #
#####################

import time


def backtracking_search2(
    csp,
    select_unassigned_variable=first_unassigned_variable,
    order_domain_values=unordered_domain_values,
    inference=no_inference,
    max_steps=100000,
):
    """[Figure 6.5]"""

    csp.num_backtracks = 0

    class MaxSteps(Exception):
        """Raise to terminate backtracking."""

    def backtrack(assignment):

        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if csp.nassigns == max_steps:
                raise MaxSteps()
            if 0 == csp.nconflicts(var, value, assignment):
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                    csp.num_backtracks += 1
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    try:
        result = backtrack({})
    except MaxSteps:
        result = None
    assert result is None or csp.goal_test(result)
    return result


def backtracking_search_instrumented(
    csp,
    select_unassigned_variable=first_unassigned_variable,
    order_domain_values=unordered_domain_values,
    inference=no_inference,
    max_steps=100_000,
):
    """Return a dict where the key 'assignment' is identical to to result of backtracking_search(csp, select_unassigned_variable, ...).

    The key 'num_assignments' == the number of times csp.assign is called.
    The key 'num_backtracks' == the number of backtracks performed.
    """
    ######################
    ### Your code here ###
    ######################

    start = time.time()

    results = backtracking_search2(
        csp, select_unassigned_variable, order_domain_values, inference, max_steps)
    finish = time.time()
    return {
        "num_assignments": csp.nassigns,  # int
        "num_backtracks": csp.num_backtracks,  # int
        "assignment": results,  # dict or None
        "time": finish - start
    }


def min_conflicts_instrumented(csp, max_steps=100_000):
    """Return a dict where the key 'assignment' is identical to to result of min_conflicts(csp, max_steps).

    The key 'num_assignments' == the number of times csp.assign is called.
    The key 'num_repair_assignments' == the number of assignments made outside of generating the initial assignment of variables.
    """
    ######################
    ### Your code here ###
    ######################
    start = time.time()
    assignment = min_conflicts(csp, max_steps)
    finish = time.time()
    return {
        "assignment": assignment,  # dict or None
        "num_assignments": csp.nassigns,  # int
        "num_repair_assignments": csp.nassigns - len(csp.variables),  # int
        "time": finish - start
    }
