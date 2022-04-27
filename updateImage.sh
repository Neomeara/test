#!/bin/bash
python3 generate.py
# ./build/depixelize-svg ./generated_image.bmp generated_image.svg
# cairosvg generated_image.svg -o generated_image.png
python3 makepngtransparent.py
# rm generated_image.bmp
# rm generated_image.svg
rm generated_image.png
git add 768-200x300.png 
git commit -m "Update image"
git push