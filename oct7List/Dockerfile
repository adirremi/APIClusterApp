# שלב 1: בניית התלויות בשכבה נפרדת
FROM python:3.11-slim AS builder

# התקנת תלותים בסיסיים
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# הגדרת סביבת עבודה
WORKDIR /app

# העתקת קובץ requirements.txt והתקנת תלויות
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# שלב 2: יצירת התמונה הסופית
FROM python:3.11-slim

WORKDIR /app

# העתקת התלויות שהותקנו
COPY --from=builder /root/.local /root/.local

# הגדרת משתני סביבה כך ש-Python ימצא את החבילות שהותקנו
ENV PATH=/root/.local/bin:$PATH

# העתקת הקוד לתוך הקונטיינר
COPY . .

# הרצת הסקריפט
CMD ["python", "main.py"]
