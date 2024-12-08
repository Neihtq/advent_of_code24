from collections import defaultdict
from functools import cmp_to_key

from utils.day5.get_input_utils import get_input
from utils.time_utils import execute


def get_rule_map(rules):
    rule_map = defaultdict(set)
    for left, right in rules:
        rule_map[left].add(right)

    return rule_map


def is_correct_order(rule_map, pages):
    comp = lambda a, b: 1 if b in rule_map[a] else 0

    def compare(a, b):
        if b in rule_map[a]:
            return -1
        elif b not in rule_map[a]:
            return 0
        else:
            return 0 

    tmp = pages.copy()
    tmp.sort(key=cmp_to_key(compare))

    order_is_correct = tmp == pages
    if order_is_correct:
        return order_is_correct, 0

    middle = len(tmp) // 2
    return order_is_correct, int(tmp[middle])


def solve(rules, page_updates):
    rule_map = get_rule_map(rules)
    sum_correct_order = 0
    sum_incorrect_order = 0
    for pages in page_updates:
        order_is_correct, middle_value = is_correct_order(rule_map, pages)
        if order_is_correct:
            middle = len(pages) // 2
            sum_correct_order += int(pages[middle])
        else:
            sum_incorrect_order += middle_value
    
    print("Sum of middle page numbers from correct updates", sum_correct_order)
    print("Sum of middle page numbers from incorrect updates", sum_incorrect_order)


def main():
    page_ordering_rules, page_updates = get_input()
    execute([solve], page_ordering_rules, page_updates)


if __name__ == "__main__":
    main()