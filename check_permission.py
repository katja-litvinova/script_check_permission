import sqlite3
from sqlite3 import Connection, Cursor


def connect_to_database() -> Connection:
    connection = sqlite3.connect("/Library/Application Support/com.apple.TCC/TCC.db")
    return connection


def cursor_for_the_connection() -> Cursor:
    cursor = connect_to_database().cursor()
    return cursor


def result_of_sql_query() -> tuple[int]:
    sql_statement: str = (
        "SELECT auth_value FROM access WHERE client = 'com.f-secure.fsmac.gui'"
    )
    result = cursor_for_the_connection().execute(sql_statement).fetchone()
    if not result:
        print(f"There is no result for '{sql_statement}'")
    return result


def check_permission_for_the_f_secure_product() -> None:
    try:
        for item in result_of_sql_query():
            if item == 0:
                print("The full disk access is denied")
            if item == 2:
                print("The full disk access is allowed")
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])


def close_database() -> None:
    connect_to_database().close()


def main() -> None:
    connect_to_database()
    cursor_for_the_connection()
    result_of_sql_query()
    check_permission_for_the_f_secure_product()
    close_database()


if __name__ == "__main__":
    main()
