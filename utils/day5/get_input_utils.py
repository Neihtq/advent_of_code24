from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(5)
    with open(input_path) as file:
        lines = file.readlines()
        page_ordering_rules = []
        updates = []

        to_populate = page_ordering_rules
        for line in lines:
            if line == '\n':
                to_populate = updates
                continue
            to_populate.append(line)

        page_ordering_rules = [rule.rstrip() for rule in page_ordering_rules ]
        page_ordering_rules = [rule.split('|') for rule in page_ordering_rules]

        updates = [update.rstrip().split(',') for update in updates]

        return page_ordering_rules, updates