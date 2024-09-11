from ultralytics import YOLO

model = YOLO('yolov8x')  # Load model

model.predict("image.bmp", save=True)  # Inference on image.bmp, save result image to 'inference/output'