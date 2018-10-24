from api.helpers.image_sanitize import sanitize_image


class ImageHandler:
    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = self.to_internal_value(data)
        return value
