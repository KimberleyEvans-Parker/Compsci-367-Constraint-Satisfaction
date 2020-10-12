
import json
import numpy
from test import get_assignment_results


# results = backtracking_search_instrumented(australia_csp,
#                                            max_steps=100_000,
#                                            )

# results = get_assignment_results()
# with open('data.txt', 'w') as outfile:
#     json.dump(results, outfile)

def get_average_std(numbers):
    return str(numpy.average(numbers)) + " +- " + str(numpy.std(numbers))


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
