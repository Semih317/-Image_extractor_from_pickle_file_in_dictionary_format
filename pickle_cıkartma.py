#this code works for data in dictionary format and stored as numpy array in features key

import os
from PIL import Image
import pickle

#upload file
with open('file_path', 'rb') as file:
    data = pickle.load(file)

#output directory
output_dir = r"file_path"
os.makedirs(output_dir, exist_ok=True)

features = data['features']
labels = data['labels']

for i, img_array in enumerate(features):
    img = Image.fromarray(img_array)
    #save image
    label = labels[i]
    img.save(os.path.join(output_dir, f"resim_{i}_label_{label}.jpg"))

print(f"Tüm resimler '{output_dir}' dizinine kaydedildi.")

"""
if you want to know your data type;

import pickle

with open('file_path', 'rb') as file:
    data = pickle.load(file)

print(type(data))
print(data)

"""