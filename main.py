from pathlib import Path
from PIL import Image

BASE_PATH = Path(__file__).resolve().parent
IMAGE_SUFFIX = (".jpg", ".png")


def main():
    SIZE = (600, 600)

    IMAGES_PATH  = BASE_PATH / "fotos"
    IMAGES_OUT_PATH = BASE_PATH / "salida"
    images_list = [_file for _file in IMAGES_PATH.glob('**/*') if _file.is_file() and _file.suffix.lower() in IMAGE_SUFFIX]

    if not IMAGES_OUT_PATH.exists():
        IMAGES_OUT_PATH.mkdir()
    
    for image_path in images_list:
        image = Image.open(image_path)
        
        image_out = image.resize(SIZE)
        image_out = image_out.convert('RGB')

        image_out_path = IMAGES_OUT_PATH / image_path.relative_to(IMAGES_PATH).with_suffix(".jpg")
        if not image_out_path.parent.exists():
            image_out_path.parent.mkdir(parents=True)

        image_out.save(image_out_path)


if __name__ == '__main__':
    main()
