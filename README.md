# EXIF-to-jpg

Removes EXIF from image and converts it to .jpg forat using Pillow library.

Run `python3 to_jpg.py --img_dir --backup --quality`

* --`img_dir`: Union[pathlib.Path, str]. Directory to scan for images (.jpg/.png) Can be a nested directory of directories. 
* --`backup`: bool. Whether or not to keep original images. Default False.
* --`quality`: int. Quality of output .jpg, int in range [1-100]. Default 90.
