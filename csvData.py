import input

tokens = []

train_string_input = []

train_binary_result = []

test_string_input = []

test_binary_result = []


def get_input_instance():
    init()
    input_instance = input.Input(tokens,
                                 train_string_input,
                                 train_binary_result,
                                 test_string_input,
                                 test_binary_result)

    return input_instance


def init():
    print("...Initializing csvs...")
    fill_tokens()
    fill_test_data()
    fill_train_data()


def fill_train_data():
    print("...Reading train.csv")

    with open('csv/train.csv') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for x in content:
        tmp = x.split(',')
        result = 1 if tmp.pop() == 'true' else 0
        train_binary_result.append(result)
        train_string_input.append(tmp)


def fill_test_data():
    print("...Reading test.csv")

    with open('csv/test.csv') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for x in content:
        tmp = x.split(',')
        result = 1 if tmp.pop() == 'true' else 0
        test_binary_result.append(result)
        test_string_input.append(tmp)


def fill_tokens():
    print("...Reading tokens.csv")

    with open('csv/tokens.csv') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for x in content:
        tmp = x.split(',')
        tokens.append(tmp[0])
