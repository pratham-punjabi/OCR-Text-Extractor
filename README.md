# 🧾 OCR Text Extractor

Optical Character Recognition (OCR) is a technology that enables the extraction of text from images, scanned documents, or handwritten notes. The primary goal of this project is to develop a lightweight OCR tool using Python that can process image files and accurately retrieve the text content within them.

This project leverages libraries like pytesseract, OpenCV, and Pillow to pre-process the images and extract textual data efficiently. It is useful for converting scanned documents into editable formats, automating data entry tasks, or enabling search functionality in image-based archives.

---

## 📌 Features

- Extracts printed text from images
- Supports multiple image formats (JPG, PNG, etc.)
- Clean command-line interface
- Easy to install and use
- Can be integrated into larger projects

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- pytesseract
- Pillow

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/OCR_Task.git
cd OCR_Task
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On Linux/macOS
```

### 4. Make Sure Tesseract is Installed
- Download and install Tesseract from here. https://github.com/tesseract-ocr/tesseract
- Add the Tesseract path to your system environment variables.
- Or manually set the path in your Python file:

```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 📷 How to Use

Place your image(s) in the `images/` folder (or update the path).

Then run:

```bash
python main.py
```

The script will print the extracted text in the console or save it to a `.txt` file.

---

## 📝 Sample Output

```bash
Extracted Text:
----------------
This is a sample image
with text that has been
successfully extracted!
```

---

## 📁 Project Structure

```bash
OCR_Task/
├── images/
│   └── sample.jpg
├── ocr_script.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🙌 Contributions

Feel free to fork the project and suggest improvements! Open issues or submit pull requests to contribute.

---

## 📬 Contact

For queries or collaborations, feel free to reach out:

- **Name**: *Pratham Punjabi*
- **Email**: *prathampunjabi705@gmail.com*
- **LinkedIn**: https://www.linkedin.com/in/pratham-p-b288b1218/
