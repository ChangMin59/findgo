# 🕵️‍♂️ FindGo — 실시간 객체 탐지·추적 (Showcase Only)

YOLOv8(+ByteTrack 옵션) 기반 **실시간 객체 탐지·추적** 프로젝트의 코드 구성과 작업 흐름을 보여주기 위한 **쇼케이스 레포**입니다.  
**데이터, 가중치, 로그는 포함하지 않으며**, 재현 실행보다 구조와 아이디어 전달에 초점을 맞춥니다.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1w_tqy06pbsKyC61KbOjjVGVDjizUolVz?usp=sharing)

> 위 배지는 참고용 링크입니다. 이 저장소에는 데이터가 없으므로, Colab에서 실행하려면 별도 데이터 연결이 필요합니다.

---

## ✨ Highlights
- **증강 파이프라인**: Albumentations로 Occlusion/Cutout, Shift/Scale/Rotate, Noise/Blur 등 구성
- **노트북 워크플로우**: 데이터 확인 → 전처리 → 학습 → 추론의 단계 분리(코드 흐름 관찰용)
- **모듈화**: 증강 로직을 `src/` 폴더로 분리해 재사용/재구성 용이

---

## 📂 Repository Structure (Showcase)
```
findgo/
├─ notebooks/             # 실험/개발 노트북 (데이터 미포함)
│  ├─ file_chek.ipynb
│  ├─ Preprocessing.ipynb
│  ├─ train.ipynb
│  └─ main.ipynb
├─ src/
│  └─ Augmentation.py     # Albumentations 증강 파이프라인 (YOLO bbox 유지)
├─ README.md
└─ requirements.txt       # 증강/노트북 관찰용 최소 의존성
```

> ℹ️ 이 저장소는 쇼케이스 목적이므로 **실행 재현을 위한 데이터/가중치**는 제공하지 않습니다.

---

## 🧠 Tech Stack
- **Augmentation**: Albumentations, OpenCV
- **Notebook Env**: Jupyter, Python 3.9+
- **(옵션)** Detection/Tracking: YOLOv8, ByteTrack 구성을 전제로 코드 분리

---

## 🔎 Code Pointers
- `notebooks/`: 단계별 코드 흐름을 확인(EDA/전처리/학습/추론)
- `src/Augmentation.py`: YOLO 포맷 라벨을 유지한 상태로 증강 이미지를 생성하는 파이프라인

---

## 🔗 Reference
- Google Colab 노트북: https://colab.research.google.com/drive/1w_tqy06pbsKyC61KbOjjVGVDjizUolVz?usp=sharing

---

## 📌 Note
- 데이터 경로/학습 설정은 개인 환경에 맞게 별도 구성이 필요합니다.