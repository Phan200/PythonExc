# de ma tran tro thanh dac biet thi can tong so
# luon bang nhau; de xay ra dieu do thi tong phai
# luon bang 15
# so chinh giua ma tran =5
# cac so bao quanh luon la theo cap 1-9,2-8,3-7,4-6
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    if s.__getitem__(1).__getitem__(1)==5:


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
