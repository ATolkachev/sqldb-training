AVAILABLE_SQL_COMMANDS = {'select', 'insert', 'update', 'delete'}

DATABASE = {}


def query_select(select_query: str):
    query = select_query[6:].strip(' ')[:-1]
    if query.isdigit():
        return query


def query_insert(insert_query: str):
    ...


def query_update(update_query: str):
    ...


def query_delete(delete_query: str):
    ...


def query_create_table(create_query: str):
    ...


SQL_COMMANDS_TO_FUNCTIONS = {
    'select': query_select,
    'insert': query_insert,
    'update': query_update,
    'delete': query_delete,
}


def get_query_type(query: str):
    command = query[0:query.find(' ')]
    if command not in AVAILABLE_SQL_COMMANDS:
        raise NotImplemented
    return command


def execute_query(query: str):
    lowered_query = query.lower().strip(' ')
    command = get_query_type(query=lowered_query)
    if query[-1] != ';':
        raise SyntaxError
    executor = SQL_COMMANDS_TO_FUNCTIONS[command]
    result = executor(lowered_query)
    return result


query = 'select 1;'
print(query)
print(execute_query(query))
