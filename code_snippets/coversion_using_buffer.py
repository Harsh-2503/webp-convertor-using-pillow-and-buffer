from PIL import Image
from io import BytesIO

def convert_img_to_webp(img):
    image_io = BytesIO()
    image = Image.open(img)
    image.save(image_io, format='webp')
    image_io.seek(0)
    return image_io

file_to_upload = convert_img_to_webp('jepg')
file_to_upload.filename = 'hello'
print(file_to_upload.filename)
# return send_file(file_to_upload, mimetype="image/webp")