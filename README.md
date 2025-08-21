# 🕵️‍♂️ FindGo — 실시간 객체 탐지·추적 (Code Showcase)

이 레포는 **데이터·가중치·로그 없이**, 프로젝트의 **코드 구조와 설계 의도**를 보여주기 위한 **쇼케이스**입니다.  
실행 재현보다는 **구성·아키텍처·핵심 로직**을 빠르게 파악할 수 있게 하는 데 목적이 있습니다.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1w_tqy06pbsKyC61KbOjjVGVDjizUolVz?usp=sharing)
<!-- 문서/보고서는 별도 레포나 링크로 관리하세요. 필요 시 아래 링크를 채워 넣으세요. -->
[📄 Full Report](#-문서-링크-추가예정)

---

## ✨ Highlights
- **증강 파이프라인**: Occlusion/Cutout, Shift/Scale/Rotate, Noise/Blur 등 (YOLO bbox 유지)
- **워크플로우 분리**: `EDA → 전처리 → 학습 → 추론` 단계별 노트북
- **모듈화**: `src/`에 증강 로직 모듈화(재사용·이식 용이)

---

## 📂 Repository Structure

```
findgo/
├─ notebooks/             # 실험/개발 노트북 (데이터 미포함)
│  ├─ 01_check.ipynb      # 데이터 확인/EDA
│  ├─ 02_preprocess.ipynb # 전처리
│  ├─ 03_train.ipynb      # 학습
│  └─ 04_infer.ipynb      # 추론/시연
├─ src/
│  └─ Augmentation.py     # Albumentations 증강 파이프라인 (YOLO bbox 유지)
├─ README.md
└─ requirements.txt       # 관찰/리뷰용 최소 의존성
```

> 이 저장소는 **코드 쇼케이스** 목적입니다. 실제 실행에는 별도의 데이터/가중치/환경 구성이 필요합니다.

---

## 🔎 Code Tour

- **`src/Augmentation.py`**
  - Albumentations Compose로 Cutout/Perspective/ShiftScaleRotate/Noise/Blur/HSV 구성
  - YOLO 포맷 라벨을 **동일 변환**으로 유지 → `_aug_N` 파일로 저장
- **`notebooks/`**
  - `01_check`: EDA/라벨 검증 아이디어(빈 라벨/좌표범위/샘플 시각화 등)
  - `02_preprocess`: 클래스 재매핑/균형화/샘플링 전략
  - `03_train`: 탐지 모델 학습 실험 로드맵(하이퍼·증강 조합 표기)
  - `04_infer`: 데모 시나리오 및 시각화(코드 스니펫 중심)

---

## 🧠 Tech Stack
- **Augmentation**: Albumentations, OpenCV
- **Notebook Env**: Jupyter, Python 3.9+
- **(옵션)** Detection/Tracking: YOLOv8, ByteTrack 구성을 전제로 분리 가능

---

## 🔗 Links
- **Colab**: https://colab.research.google.com/drive/1w_tqy06pbsKyC61KbOjjVGVDjizUolVz?usp=sharing
- **Full Report**: (별도 링크/레포/Release 자산에 PDF 업로드 후 여기에 주소를 넣으세요)

---

## 📌 Notes
- 노트북은 **출력(Out[]) 비운 상태**로 커밋 권장 (필요 시 `nbstripout` 사용)
- `requirements.txt`는 최소 의존성만 기재(실행 재현 목적이 아니므로 torch/ultralytics는 생략 가능)
- 데이터/가중치/로그는 포함하지 않습니다

---
