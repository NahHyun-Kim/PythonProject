import cv2

# 설치한 라이브러리 (opencv-python, matplot - 히스토그램 관련)
# 불러올 이미지 경로
image_file = "image/my_face.jpg"

# cv2.IMREAD_COLOR : 수정 없이 원본 이미지 읽기
# 이미지 읽을 때 기본값(RGB 칼라로 읽음)이며, 숫자 값으로 1 표현 가능
original = cv2.imread(image_file, cv2.IMREAD_COLOR)

# cv2.IMREAD_GRAYSCALE : 흑백사진으로 수정해서 이미지 읽기
# GrayScale(흑백), 이미지 처리 수행의 중간 단계로 활용, 숫자 값으로 1 표현 가능
gray = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

# cv2.IMREAD_UNCHANGED : 이미지 파일의 알파 채널(Alpha Channel)까지 포함해서 읽기
# 컴퓨터에서 렌더링할 때 쓰이는 보조적인 값, 이미지 투명도..
unchange = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)

# 이미지 보여주기
# 얼굴 인식 : 흑백사진 변환 -> 히스토그램 평활화(RGB값이 아닌 흑백 사진을 기반, 히스토그램을 이용하여 명암 대비 개선) -> 이미지 인식
cv2.imshow("IMREAD_COLOR", original) # 원본
cv2.imshow("IMREAD_GRAYSCALE", gray) # 흑백
cv2.imshow("IMREAD_UNCHANGED", unchange) # 알파 채널 추가

# 입력받는 것 대기하기, 작성하지 않으면 결과창이 바로 닫힘
cv2.waitKey(0)