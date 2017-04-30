import input
import psycopg2

tokens = []

train_string_input = []

train_binary_result = []

test_string_input = []

test_binary_result = []


global items_kfold

global conn


def get_input_instance(items_kfold_str):
    global items_kfold
    items_kfold = items_kfold_str
    init()
    input_instance = input.Input(tokens,
                                 train_string_input,
                                 train_binary_result,
                                 test_string_input,
                                 test_binary_result)

    return input_instance


def init():
    print("...Initializing db...")
    global conn
    try:
        conn = psycopg2.connect("dbname='mrmp_oznal' "
                                "user='postgres' "
                                "host='team05-16.studenti.fiit.stuba.sk' "
                                "password='mfc-2016_postgres' "
                                "port='5432'")
    except:
        print("I am unable to connect to the database")

    fill_tokens()
    fill_binary_result('true')
    fill_binary_result('false')
    fill_string_input('true')
    fill_string_input('false')


def fill_binary_result(is_train):
    print("... filling binary result, train is " + is_train)
    global train_binary_result
    global test_binary_result

    query = "select array(" \
            "select " \
            "CASE WHEN i.contains_meet='t' THEN 1 " \
                 "WHEN i.contains_meet='f' THEN 0 " \
            "END " \
            "FROM items AS i " \
            "JOIN " + items_kfold + " As k ON i.id = k.id " \
            "WHERE k.train = " + is_train + " " \
            "ORDER BY k.id)"

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    if is_train == 'true':
        train_binary_result = rows[0][0]
    elif is_train == 'false':
        test_binary_result = rows[0][0]


def fill_string_input(is_train):
    print("... filling string inputs, train is %s" % is_train)
    global train_string_input
    global test_string_input

    query = "SELECT i.tokens " \
            "FROM items AS i " \
            "JOIN " + items_kfold + " AS k ON i.id = k.id " \
            "WHERE k.train = " + is_train + " " \
            "ORDER BY k.id"

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    tmp_array_string = []
    for row in rows:
        tmp_array_string.append(row[0])

    if is_train == 'true':
        train_string_input = tmp_array_string
    elif is_train == 'false':
        test_string_input = tmp_array_string


def fill_tokens():
    print("... filling tokens")
    global tokens

    query = "SELECT array(SELECT token FROM tokens WHERE recipe = false)"

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    tokens = rows[0][0]

