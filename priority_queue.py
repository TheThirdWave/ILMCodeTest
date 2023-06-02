import json
import argparse

def load_dict(filepath):
    dict = {}
    with open(filepath) as file:
        dict = json.load(file)

    return dict


def sort_and_execute(commands_list, num_priorities):
    priority_dict = generate_priority_dict(num_priorities)
    priority_dict = fill_dict(commands_list, priority_dict)
    execute_commands(priority_dict)


def generate_priority_dict(num_priorities):
    dict = {}
    for prio in range(num_priorities):
        dict[prio] = []
    return dict

def fill_dict(commands_list, priority_dict):
    for command in commands_list:
        priority_dict[command['priority']].append(command['command'])

    # I do not believe I need to return this to update the priority_dict in the "sort_and_execute" function,
    # but I believe doing so makes it more explicit about what "fill_dict" is actually doing
    return priority_dict


def execute_commands(priority_dict):
    for prio, commands_list in priority_dict.items():
        for command in commands_list:
            print('EXECUTING PRIORITY{0} COMMAND: {1}'.format(prio, command))


def parse_args():
    parser = argparse.ArgumentParser(description="Reads a JSON file and executes the commands within according to their priority.")
    parser.add_argument('filepath', type=str, default='', help='The path to the JSON file that contains the commands.')
    parser.add_argument('--priorities', type=int, default=11, required=False, help='The number of priority levels the commands could have.')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    commands_dict = load_dict(args.filepath)
    sort_and_execute(commands_dict['commandList'], args.priorities)