# Practice: Rotate Image CLI tool

[Pillow](https://python-pillow.org) is a Python package for working with images.
Create a full [Python application](/notes/py-app-structure.md) that has a
 [virtualenv](/notes/py-virtualenv.md) with Pillow installed in it.

Create a program `rotate.py` in your application that uses Pillow to open an
image, rotate it 45 degrees, and save the rotated version.
Have it take in the input image and output image filename from the command line
 arguments of the script.

```bash
python rotate.py input.jpg rotated.png
```

Check out the [Pillow docs](http://pillow.readthedocs.io/) and search around on
the internet for help on opening, rotating, and saving images.
Still practice good program structure, even for this little demo.

### Advanced

- Automatically rotate a whole directory of images.  
- Auto generate thumbnails for each image file in an input directory.
