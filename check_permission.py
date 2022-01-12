import sqlite3


def main() -> None:
    query: str = "SELECT auth_value FROM access WHERE client = 'com.f-secure.fsmac.gui'"
    con = sqlite3.connect("/Library/Application Support/com.apple.TCC/TCC.db")
    cur = con.cursor()
    try:
        cur.execute(query)
        result_of_query: tuple = cur.fetchone()
        if not result_of_query:
            print(f"There is no result for '{query}'")
        for item in result_of_query:
            if item == 0:
                print("The full disk access is denied")
            if item == 2:
                print("The full disk access is allowed")
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
    finally:
        con.close()


if __name__ == "__main__":
    main()
