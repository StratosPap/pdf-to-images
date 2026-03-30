# 📄 PDF to Grayscale Image Converter

## 📌 Overview

This script converts PDF files into grayscale JPEG images. It is designed to handle **large PDFs and batch processing** efficiently without running into memory issues.

Each PDF is converted into a separate folder, and each page is saved as an individual image.

---

## ⚙️ Features

* Converts PDF pages to **8-bit grayscale images**
* Resizes images to **1700 × 2400**
* Saves images as **JPEG (quality 95, 300 DPI)**
* Processes **multiple PDFs in a folder**
* Creates **one output folder per PDF**
* Memory-safe: processes **one page at a time**
* Progress output in terminal

---

## 📂 Input Structure

Place your PDFs inside a folder:

```
input_folder/
  00000001.pdf
  00000002.pdf
  ...
  00000250.pdf
```

---

## 📁 Output Structure

The script will generate:

```
output_images/
  00000001/
    page-1.jpg
    page-2.jpg
  00000002/
    page-1.jpg
    page-2.jpg
```

---

## 🚀 How to Run

### Basic usage:

```
python script.py input_folder
```

### With custom output folder:

```
python pdf_to_jpg_converter.py input_folder -o output_images
```

> ⚠️ If your folder name contains spaces, wrap it in quotes.

---

## 🧠 How It Works

Instead of loading the entire PDF into memory, the script:

1. Reads total number of pages
2. Loads **one page at a time**
3. Converts and saves it
4. Moves to the next page

This prevents **MemoryError** when processing large PDFs.

---

## 🛠 Requirements

Install dependencies:

```
pip install pdf2image pillow
```

### Additional Requirement (Windows)

You must install **Poppler** and set the correct path in the script:

```
poppler_path = r"C:\path\to\poppler\bin"
```

---

## 📊 Output Details

Each image will be:

* Format: JPEG
* Color: Grayscale (8-bit)
* Resolution: 1700 × 2400
* DPI: 300
* Naming: `page-1.jpg`, `page-2.jpg`, ...

---

## 🧩 Troubleshooting

### ❌ Error: `MemoryError`

✔ Fixed by processing pages one-by-one (already implemented)

---

### ❌ Error: `poppler not found`

✔ Ensure Poppler is installed and path is correct

---

### ❌ Error with spaces in folder name

✔ Use quotes:

```
python pdf_to_jpg_converter.py "my folder"
```

---

## ⏹ Stopping the Script

Press:

```
Ctrl + C
```

Then confirm with:

```
Y
```

---

## 📈 Possible Improvements

* Add progress bar (`tqdm`)
* Parallel processing for speed
* Resume from last processed file
* Option to change DPI or resolution

---

## 👨‍💻 Author

Stratos

---
