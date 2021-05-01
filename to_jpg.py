from PIL import Image
import argparse
from pathlib import Path


def convert(img_path, args):
    # Read
    img = Image.open(img_path)

    # Backup
    if args.backup:
        backup_path = img_path.parent / 'backup'
        backup_path.mkdir(parents=True, exist_ok=True)
        img.save(backup_path / img_path.name, quality=100)

    if not img.mode == 'RGB':
        img = img.convert('RGB')

    # New path
    img_save = img_path.with_suffix('.jpg')
    print(f'Converted: {img_path} to {img_save}.')

    img.save(img_save, quality=args.quality)

    # JPGs overwrite themselves, manually delete PNGs
    if img_path.suffix == '.png':
        img_path.unlink()


if __name__ == '__main__':

    # Parse CLI
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir', required=True, type=str, help='img to be converted')
    parser.add_argument('--quality', type=int, default=90, help='jpg quality')
    parser.add_argument('--backup', action='store_true', default=False, help='backup original img')
    args = parser.parse_args()

    img_dir = list(Path(args.img_dir).glob('**/*.*g'))

    # Loop over (.jpg/.png)
    for img_path in img_dir:
        convert(img_path, args)
