import csv

def save_to_file(jobs):
    # open(파일 열기, 파일이 없다면 생성)
    file = open("jobs.csv", mode="w", encoding="UTF-8") # 모드 : w(write)
    # 첫 줄에 카테고리 작성
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        # dictionary 객체에 접근(values()로 값만 가져옴 -> list로 바꾸기)
        writer.writerow(list(job.values()))
    return