import input
import psycopg2

tokens = []

train_string_input = []

train_binary_result = []

test_string_input = []

test_binary_result = []

conn = ''


def get_input_instance():
    init()
    input_instance = input.Input(tokens,
                                 train_string_input,
                                 train_binary_result,
                                 test_string_input,
                                 test_binary_result)

    return input_instance


def init():
    print("...Initializing db...")
    try:
        conn = psycopg2.connect("dbname='mrmp_oznal' "
                                "user='postgres' "
                                "host='team05-16.studenti.fiit.stuba.sk' "
                                "password='mfc-2016_postgres' "
                                "port='5432'")
    except:
        print("I am unable to connect to the database")

    fill_tokens()
    fill_test_data()
    fill_train_data()


def fill_train_data():
    print("")


def fill_test_data():
    print("")


def fill_tokens():
    print("")
    # cur = conn.cursor()
    # cur.execute("""SELECT tokens from items limit 1""")
    # rows = cur.fetchall()
    # print(rows)

