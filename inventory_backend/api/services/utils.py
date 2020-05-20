import logging
from PIL import Image

# Get an instance of a logger
logger = logging.getLogger(__name__)


def image_validation(image):
    """
        Validates the image field like
        1. Checks the Image Dimensions with max and min width & height.
        2. Checks the Image size with max and min size.
        3. Checks the Image Extension with default extensions.
    """
    logger.info(" Image_validation entered")
    msg = None
    max_height = max_width = 800
    default_extension = ['png', 'jpg', 'jpeg']
    img = Image.open(image)
    width, height = img.size
    if img.format.lower() not in default_extension:
        msg = 'Ensure that Image format should be `{}`'.format(
            default_extension)
        return msg
    if width > max_width or height > max_height:
        msg = 'Height x Width must not exceed `{0} x {1}`'.format(
            max_height, max_width)
        return msg
    return msg
    logger.info(" Image_validation ended")
