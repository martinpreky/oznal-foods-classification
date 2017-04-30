import input
import psycopg2

global items_kfold

global is_with_recipe

global conn


def get_input_instance(items_kfold_str, with_recipe):
    global items_kfold
    global is_with_recipe

    items_kfold = items_kfold_str
    is_with_recipe = with_recipe

    init()

    # tokens,
    # trainStrInput,
    # trainBinaryResult,
    # testStrInput,
    # testBinaryResult
    input_instance = input.Input(fill_tokens(),
                                 fill_string_input('true'),
                                 fill_binary_result('true'),
                                 fill_string_input('false'),
                                 fill_binary_result('false'))

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


def fill_binary_result(is_train):
    print("... filling binary result, train is " + is_train)

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

    return rows[0][0]


def fill_string_input(is_train):
    print("... filling string inputs, train is %s" % is_train)

    select = ""
    if is_with_recipe:
        select = "SELECT array_cat(i.tokens, i.recipe_tokens)"
    else:
        select = "SELECT i.tokens"

    query = select + " " \
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

    return tmp_array_string


def fill_tokens():
    print("... filling tokens")

    query = ""
    if is_with_recipe:
        query = "SELECT array(SELECT token FROM tokens)"
    else:
        query = "SELECT array(SELECT token FROM tokens) WHERE recipe_only = false"

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    return rows[0][0]

