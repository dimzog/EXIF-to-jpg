from PIL import Image
import argparse
from pathlib import Path


def convert(img_path):
    # Read
    img = Image.open(img_path)

    # Backup
    if args.backup:
        backup_path = Path.cwd() / 'backup'
        backup_path.mkdir(parents=True, exist_ok=True)
        img.save(backup_path / img_path.name, quality=100)

    if not img.mode == 'RGB':
        img = img.convert('RGB')

    # New path
    img_save = img_path.parent / (img_path.stem + '.jpg')
    print(f'Converted: {img_path} to {img_save}.')

    img.save(img_save, quality=args.quality)


if __name__ == '__main__':

    # Parse CLI
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir', required=True, type=str, help='img to be converted')
    parser.add_argument('--quality', type=int, default=95, help='jpg quality')
    parser.add_argument('--backup', action='store_true', default=True, help='backup original img')
    args = parser.parse_args()

    img_path = Path(args.img_dir)

    # Loop over (.jpg/.png)
    for f in img_path.glob('*.*g'):
        convert(f)









