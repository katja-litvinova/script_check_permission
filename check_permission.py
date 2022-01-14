import sqlite3


def connect_to_database() -> sqlite3.Connection:
    return sqlite3.connect("/Library/Application Support/com.apple.TCC/TCC.db")


def check_permissions(permission_codes: list[tuple[int]]) -> None:
    disk_access_permissions_map = {
        0: "denied",
        1: "unknown",
        2: "allowed",
        3: "limited"
    }
    if not len(permission_codes) or len(permission_codes) > 1:
        print("Permissions are empty or have more than one value. Please check SQL query")
        return

    permission_code = permission_codes[0][0]
    permission = disk_access_permissions_map[permission_code]
    print(f"The full disk access is {permission}")


def check_permission_for_the_f_secure_product() -> None:
    sql_query: str = (
        "SELECT auth_value FROM access WHERE client = 'com.f-secure.fsmac.gui'"
    )
    connect = connect_to_database()
    cursor = connect.cursor()
    permission_codes = cursor.execute(sql_query).fetchall()
    check_permissions(permission_codes)
    connect.close()


if __name__ == "__main__":
    check_permission_for_the_f_secure_product()
