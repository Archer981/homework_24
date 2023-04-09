def filter_query(data, query):
    return [line for line in data if query.lower() in line.lower()]


def map_query(data, query):
    return list(map(lambda x: x.split(' ')[int(query)], data))


def unique_query(data, query=''):
    return list(set(data))


def sort_query(data, query='asc'):
    query = False if query == 'asc' else True
    return sorted([line for line in data], reverse=query)


def limit_query(data, query):
    return [line for line in data][:query]
