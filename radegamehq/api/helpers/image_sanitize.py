def sanitize_image(data):
    if 'image' in data and 'http' in data['image']:
        data.pop('image')
    return data
