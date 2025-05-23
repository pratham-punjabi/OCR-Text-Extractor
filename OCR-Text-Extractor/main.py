import easyocr
import os
import cv2

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )

    temp_path = "temp_cleaned.jpg"
    cv2.imwrite(temp_path, thresh)
    return temp_path

def extract_text_with_easyocr(folder_path, use_preprocessing=False, min_confidence=0.3):
    reader = easyocr.Reader(['en'])  # English lang model

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            original_path = os.path.join(folder_path, filename)
            image_path = preprocess_image(original_path) if use_preprocessing else original_path

            result = reader.readtext(image_path)

            print(f"\nImage: {filename}")
            if not result:
                print("No text detected.")
            else:
                for bbox, text, confidence in result:
                    if confidence >= min_confidence:
                        print(f" {text} (Confidence: {confidence:.2f})")
                    else:
                        print(f"Low-confidence text skipped: {text} ({confidence:.2f})")

            print("=" * 50)

if __name__ == "__main__":
    extract_text_with_easyocr("images", use_preprocessing=False)
