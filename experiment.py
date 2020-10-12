# from textbook.problems import (
#     australia_csp,
#     france_csp,
#     usa_csp,
#     NQueensCSP,
#     Zebra,
# )

# from textbook.csp import *

# import timeit
import json
import numpy
# import time
# import pandas as pd
# import openpyxl
# from instrumented_solvers import *
# from test import get_solvers
from test import get_assignment_results


# def time_function1(csp):
#     start = time.time()
#     results = backtracking_search_instrumented(csp,
#                                                max_steps=100_000,
#                                                )
#     finish = time.time()
#     result["time"] = finish - start
#     return results


# def time_function2(csp):
#     start = time.time()
#     results = backtracking_search_instrumented(csp,
#                                                inference=forward_checking,
#                                                max_steps=100_000,
#                                                )
#     finish = time.time()
#     result["time"] = finish - start
#     return results


# def time_function3(csp):
#     start = time.time()
#     results = backtracking_search_instrumented(csp,
#                                                inference=AC3,
#                                                max_steps=100_000,
#                                                )
#     finish = time.time()
#     result["time"] = finish - start
#     return results


# def time_function4(csp):
#     start = time.time()
#     results = backtracking_search_instrumented(csp,
#                                                select_unassigned_variable=mrv,
#                                                order_domain_values=lcv,
#                                                inference=no_inference,
#                                                max_steps=100_000,
#                                                )
#     finish = time.time()
#     result["time"] = finish - start
#     return results


# def time_function5(csp):
#     start = time.time()
#     results = backtracking_search_instrumented(csp,
#                                                select_unassigned_variable=mrv,
#                                                order_domain_values=lcv,
#                                                inference=AC3,
#                                                max_steps=100_000,
#                                                )
#     finish = time.time()
#     result["time"] = finish - start
#     return results

# def time_function6(csp):
#     start = time.time()
#     results = backtracking_search_instrumented(csp,
#         select_unassigned_variable=mrv,
#         order_domain_values=lcv,
#         inference=AC3,
#         max_steps=100_000,
#     )
#     finish = time.time()
#     result["time"] = finish - start
#     return results


# def get_pd(name, rows, index, columns):
#     columns = ['Average # of assignments"', '+/- std dev', 'Average time to solve',
#                '+/- std dev', 'Probability of solving', 'number of backtracks']
#     matrix = pd.DataFrame(rows, index=index, columns=columns)
#     return matrix


# NUM_ITERATIONS = 10

# def run


# print(get_solvers())

# solvers = get_solvers()

# csps = [NQueensCSP, australia_csp, usa_csp, Zebra]

# csp = CSP(NQueensCSP)
# results = backtracking_search_instrumented(australia_csp,
#                                            max_steps=100_000,
#                                            )
def get_average_std(numbers):
    return str(numpy.average(numbers)) + " +- " + str(numpy.std(numbers))


# results = get_assignment_results()
# with open('data.txt', 'w') as outfile:
#     json.dump(results, outfile)

with open('data.txt') as json_file:
    results = json.load(json_file)

# print(results)


data = {}

for method in results:
    data[method] = {}
    for cps in results[method]:
        data[method][cps] = {}
        # print(method, cps)
        data[method][cps]["num_assignments"] = get_average_std(
            results[method][cps]["num_assignments"])
        data[method][cps]["time"] = get_average_std(
            results[method][cps]["time"])
        prob = 0
        for assignment in results[method][cps]["assignment"]:
            if assignment != None:
                prob += 0.1
        data[method][cps]["prob"] = prob
        if "num_backtracks" in results[method][cps]:
            data[method][cps]["num_backtracks"] = get_average_std(
                results[method][cps]["num_backtracks"])
        if "num_repair_assignments" in results[method][cps]:
            data[method][cps]["num_repair_assignments"] = get_average_std(
                results[method][cps]["num_repair_assignments"])

# print(data)
json.dumps(data, indent=4)
with open('results.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# for csp in csps:
#     for key in solvers:
#         print(key)
#         results = solvers[key](csp)
#         print(results)
#         print()


# with pd.ExcelWriter('data.xlsx') as writer:
#     expanded_df.to_excel(writer, sheet_name='expanded')
