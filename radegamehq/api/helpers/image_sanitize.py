import copy


def sanitize_image(data, props=None):
    props = props if props is not None else ['image']
    data = copy.deepcopy(data)

    for prop in props:
        if prop in data and data[prop] is not None and 'http' in data[prop]:
            data.pop(prop)
    return data
