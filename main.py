import os
import sys

from PIL import Image

with Image.open(sys.argv[1]) as obj:
    if not os.path.exists("{}/result/".format(os.getcwd())):
        os.mkdir("result")

    print(dir(obj))

    name = "{}/result/{}".format(os.getcwd(), obj.filename)
    result = obj.resize((512, 512), Image.Resampling.LANCZOS)

    try:
        result.save(name, quality=50)
    except Exception as e:
        print(e)
