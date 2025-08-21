# 증강 파이프라인
import os
import cv2
import numpy as np
import albumentations as A
from tqdm import tqdm
import shutil
import random

# 원본 데이터 폴더 (이미지 & 라벨)
image_dir = "/mnt/data/homecam_dataset/images"
label_dir = "/mnt/data/homecam_dataset/labels"

# 증강된 데이터 저장 폴더
output_image_dir = "/mnt/data/homecam_dataset_augmented/images"
output_label_dir = "/mnt/data/homecam_dataset_augmented/labels"

# 저장 폴더 생성
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 홈캠 겹침 문제 해결을 위한 데이터 증강 기법 정의
transform = A.Compose([
    A.Cutout(num_holes=5, max_h_size=30, max_w_size=30, p=0.4),  # Occlusion Masking (일부 가리기)
    A.Perspective(scale=(0.05, 0.15), p=0.3),  # 원근 변환
    A.ShiftScaleRotate(shift_limit=0.02, scale_limit=0.1, rotate_limit=15, p=0.5),  # 확대/축소 & 회전
    A.RandomBrightnessContrast(p=0.4),  # 밝기/대비 조정 (낮/밤 환경 대응)
    A.GaussNoise(p=0.3),  # 가우시안 노이즈 추가 (실내 조명 변화를 학습)
    A.Blur(blur_limit=3, p=0.3),  # 블러 효과 (흐려진 영상 대응)
    A.HueSaturationValue(p=0.3),  # 색상 변화 적용
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

# 증강할 횟수 설정 (2배 증강)
num_augmentations = 2  

# 모든 이미지 파일 가져오기
image_files = [f for f in os.listdir(image_dir) if f.endswith((".jpg", ".png"))]

print(" 홈캠 데이터 증강 시작...")
for image_file in tqdm(image_files):
    image_path = os.path.join(image_dir, image_file)
    label_path = os.path.join(label_dir, image_file.replace(".jpg", ".txt").replace(".png", ".txt"))

    # 원본 이미지 로드
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # 원본 이미지 & 라벨 복사 (원본도 유지)
    shutil.copy(image_path, os.path.join(output_image_dir, image_file))
    shutil.copy(label_path, os.path.join(output_label_dir, image_file.replace(".jpg", ".txt").replace(".png", ".txt")))

    # 원본 라벨 불러오기 (YOLO 형식)
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            labels = f.readlines()

        bboxes = []
        class_labels = []
        for label in labels:
            parts = label.strip().split()
            class_id = int(parts[0])
            x_center, y_center, w, h = map(float, parts[1:])
            bboxes.append([x_center, y_center, w, h])
            class_labels.append(class_id)

        # 데이터 증강 수행 (2배 증가)
        for i in range(num_augmentations):
            augmented = transform(image=image, bboxes=bboxes, class_labels=class_labels)
            aug_image = augmented["image"]
            aug_bboxes = augmented["bboxes"]
            aug_labels = augmented["class_labels"]

            # 증강된 이미지 저장
            aug_image_filename = f"{os.path.splitext(image_file)[0]}_aug_{i}.jpg"
            aug_image_path = os.path.join(output_image_dir, aug_image_filename)
            cv2.imwrite(aug_image_path, aug_image)

            # 증강된 라벨 저장 (YOLO 포맷 유지)
            aug_label_filename = f"{os.path.splitext(image_file)[0]}_aug_{i}.txt"
            aug_label_path = os.path.join(output_label_dir, aug_label_filename)
            with open(aug_label_path, "w") as f:
                for bbox, class_id in zip(aug_bboxes, aug_labels):
                    x_center, y_center, w, h = bbox
                    f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

print(" 홈캠 데이터 증강 완료! (겹침 문제 해결)")