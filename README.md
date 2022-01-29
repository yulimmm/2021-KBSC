# 2021 kbsc KB 국민은행 소프트웨어 경진대회  참가
주제: 국민과 함깨 환경을 바꾸는 소프트웨어

### Smart Locker 소개
- 보안성이 높고 바이러스 살균기능이 있는 신발장 겸 락커
- 살기 좋은 편한 환경을 만들어 줌

### 핵심 아이디어
 <img src="https://user-images.githubusercontent.com/89307538/151662361-add39347-20ad-447c-ad47-672c48085579.png" width="600" height="300"/> 
 
 + 현재 날씨를 알 수 있는 터치 디스플레이
 + 비가 오면 FAN을 더 세게 돌려 젖은 신발을 건조
 + UV LED와 FAN을 통한 보관물품/신발 소독
 + 손잡이를 잡지 않고 얼굴인식을 통해 자동으로 문이 열리는 접촉을 최소화한 언택트 신발장 겸 보안 락커
 + 날씨 api를 받아와 현재 날씨에 따라 바뀌는 FAN세기

### 내가 구현한 부분 구현 기술 (Face Recognition, uart 통신)
 - 웹캠으로 실시간 얼굴인식
 - 라즈베리파이와 cortex m 통신

### 구현 환경
 - Raspberry Pi 4, logic webcam 
 - Cortex M4

### 팀원
 - [Yoo-jung](https://github.com/Yoo-jung)
 - [micromi](https://github.com/micromielec)
 - [HwangGoeun](https://github.com/HwangGoeun)
 

## 구현영상
- [구현영상]https://www.youtube.com/watch?v=eEnxIa0pKeo

## 참고
- https://github.com/ageitgey/face_recognition/blob/master/README_Korean.md#deployment
