FROM python:3.8
WORKDIR /home/diyzen/Desktop/docker1
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    python3-rospy\
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "face_detection.py"]
