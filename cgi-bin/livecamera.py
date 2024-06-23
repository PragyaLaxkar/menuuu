#!/usr/bin/python3
import cgi
import os
import time
upload_dir = "myupload/"

print("Content-Type: text/plain")
print()

try:
    form = cgi.FieldStorage()
    image_file = form['image']
    
    if image_file.filename:
        timestamp = int(time.time())
        filename = f"image_{timestamp}.png"
        
        filepath = os.path.join(upload_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(image_file.file.read())
        print("Image uploaded successfully")
    else:
        print("No image file received")
except Exception as e:
    print("An error occurred:", str(e))


#!/usr/bin/python3

# import cgi
# import os
# import time
# import cv2
# import numpy as np

# # Directory where uploaded files will be stored
# upload_dir = "myupload/"

# # Ensure the upload directory exists
# if not os.path.exists(upload_dir):
#     os.makedirs(upload_dir)

# print("Content-Type: text/plain")
# print()

# try:
#     form = cgi.FieldStorage()
#     image_file = form['image']
    
#     if image_file.filename:
#         timestamp = int(time.time())
#         original_filename = f"image_{timestamp}.png"
#         filtered_filename = f"image_{timestamp}_filtered.png"
        
#         original_filepath = os.path.join(upload_dir, original_filename)
#         filtered_filepath = os.path.join(upload_dir, filtered_filename)

#         with open(original_filepath, 'wb') as f:
#             f.write(image_file.file.read())

#         # Read the image with OpenCV
#         img = cv2.imread(original_filepath)

#         # Apply a background blur filter
#         blur = cv2.GaussianBlur(img, (21, 21, 0))

#         # Save the filtered image
#         cv2.imwrite(filtered_filepath, blur)

#         print("Image uploaded and filtered successfully")
#         print(f"Original Image: {original_filename}")
#         print(f"Filtered Image: {filtered_filename}")
#     else:
#         print("No image file received")
# except Exception as e:
#     print("An error occurred:", str(e))
