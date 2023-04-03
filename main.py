result = count = countF = totalOpen = totalSubmit = 0
srt = True
while srt:
    choice1 = int(input("작업을 선택하세요.\n1. 입력\n2. 계산\n"))


    def inp():
        global count, countF, result, totalOpen, totalSubmit
        mul = int(input("학점을 입력하세요:\n"))
        grade = str(input("평점을 입력하세요:\n"))
        match grade:
            case 'A+':
                grade = 45
            case 'A':
                grade = 40
            case 'B+':
                grade = 35
            case 'B':
                grade = 30
            case 'C+':
                grade = 25
            case 'C':
                grade = 20
            case 'D+':
                grade = 15
            case 'D':
                grade = 10
            case 'F':
                grade = 0
                countF += 1
        result = result + mul * grade
        totalOpen += mul
        if grade == 0:
            pass
        else:
            totalSubmit += mul
        count += 1


    def cal():
        global srt
        float(result)
        print("제출용: %d학점 (GPA: %.2f)\n" % (totalSubmit, (result / 10) / (count - countF)))
        print("열람용: %d학점 (GPA: %.2f)\n" % (totalOpen, (result / 10) / count))
        print("\n프로그램을 종료합니다.\n")
        srt = False


    if choice1 == 1:
        inp()
    elif choice1 == 2:
        cal()
    else:
        print("잘못된 입력")
        srt = False
