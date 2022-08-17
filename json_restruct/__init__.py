import re


def flatten(d):
    """
    Flatten dict
    :param d: object to flatten
    :return: flatten dict
    """
    stack = list(d.items())
    res = {}
    while stack:
        key, val = stack.pop()
        if isinstance(val, dict):
            for sub_key, sub_val in val.items():
                stack.append((f"{key}.{sub_key}", sub_val))
        elif isinstance(val, list) and isinstance(val[0], dict):
            for i, sub_val in enumerate(val):
                stack.append((f"{key}.{i}", sub_val))
        else:
            res[key] = val
    return res


def _convert_dict_to_list(object_, parent_object, parent_object_key):
    """
    Modified _convert_dict_to_list https://github.com/amirziai/flatten
    """
    keys = []
    for key, val in object_.items():
        if isinstance(val, dict):
            _convert_dict_to_list(object_[key], object_, key)

        if key.isnumeric():
            keys.append(key)

    keys_len = len(keys)

    if keys_len > 0:
        parent_object[parent_object_key] = []
        for key in keys:
            parent_object[parent_object_key].append(object_[key])
            _convert_dict_to_list(parent_object[parent_object_key][-1],
                                  parent_object[parent_object_key], None)


def unflatten(flatten_d):
    """
    Unflatten dict
    :param flatten_d: flatten dict
    :return: dict
    """
    res = {}
    for k, v in flatten_d.items():
        k = k.split('.')
        root = res
        for p in k[:-1]:
            root.setdefault(p, {})
            root = root[p]
        root[k[-1]] = v

    _convert_dict_to_list(res, None, None)
    return res


rgx = re.compile(r'.(\d+)')

def _restruct(flatten_d, restructure_map):
    d = {}
    for k, v in flatten_d.items():
        k, n = rgx.subn('.{}', k)
        k = restructure_map.get(k)
        if k and v:
            k = k.format(*range(n))
            d[k] = v
    return d


def restruct(d, restructure_map):
    """
    Restruct dict according to restructure map
    :param d: dict object
    :param restructure_map: Prepared dict describing the way to restruct
    :return: new dict
    """
    flatten_d = flatten(d)
    x = _restruct(flatten_d, restructure_map)
    return unflatten(x)
