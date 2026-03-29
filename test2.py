import os
from pdf2image import convert_from_path
from PIL import Image
import argparse

# Terminal arguments
parser = argparse.ArgumentParser(description="Batch convert PDFs to images.")
parser.add_argument("input_folder", help="Folder containing PDF files")
parser.add_argument("-o", "--output", default="output_images", help="Output folder")

args = parser.parse_args()

input_folder = args.input_folder
output_root = args.output

os.makedirs(output_root, exist_ok=True)

# Loop through all PDFs in folder
for file in sorted(os.listdir(input_folder)):
    if file.lower().endswith(".pdf"):

        pdf_path = os.path.join(input_folder, file)
        pdf_name = os.path.splitext(file)[0]

        # Create subfolder with same name as PDF
        output_folder = os.path.join(output_root, pdf_name)
        os.makedirs(output_folder, exist_ok=True)

        print(f"Processing {file}...")

        pages = convert_from_path(pdf_path, dpi=300)

        for i, page in enumerate(pages, start=1):
            print(f"[{pdf_name}] Page {i}/{len(pages)}")
            img = page.convert("L")
            img = img.resize((1700, 2400), Image.LANCZOS)

            filename = f"page-{i}.jpg"
            img.save(
                os.path.join(output_folder, filename),
                "JPEG",
                quality=95,
                dpi=(300, 300)
            )

print("All PDFs converted.")