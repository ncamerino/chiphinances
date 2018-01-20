""" Methods to initialize brother allowances and
    track food expenditures per brother."""

import json
import os
import sys

brother_file = os.path.dirname(os.path.realpath('test_roster.txt')) + '/test_roster.txt'
prop_file = os.path.dirname(os.path.realpath('test_props.json')) + '/test_props.json'


def init_allowances():
    total_budget = 0
    brothers = []
    num_brothers = 0
    cost_per_brother = 0
    allowances = {}
    # Load total budget
    try:
        with open(prop_file) as f:
            props = json.load(f)
            total_budget = float(props['budget']['totalBudget'])
    except:
        print('File %s does not exist' % prop_file)
        sys.exit(1)
    if total_budget == 0:
        print('Invalid totalBudget property.')
        sys.exit(1)
    # Load brother roster and fill JSON object with values
    try:
        roster = open(brother_file)
        for name in roster:
            if name[-1] == os.linesep:
                name = name[:len(name) - 1]
            num_brothers += 1
            brothers.append(name)
        roster.close()
    except:
        print('File %s does not exist.' % brother_file)
        sys.exit(1)
    if num_brothers == 0:
        print('No brothers were found. Please check brother roster file.')
    cost_per_brother = round(total_budget / num_brothers, 2)
    for brother in brothers:
        allowances[brother] = cost_per_brother
    return json.dumps(allowances)


if __name__ == '__main__':
    print(init_allowances())