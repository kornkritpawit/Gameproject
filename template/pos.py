
def check_brick_y(x,y):
    if 0<=x<100 and 480>y>=420:
        return 0,0
    elif 100<=x<200 and 480>y>=420:
        return 0,1
    elif 200<=x<300 and 480>y>=420:
        return 0,2
    elif 300<=x<400 and 480>y>=420:
        return 0,3
    elif 400<=x<500 and 480>y>=420:
        return 0,4
    elif 500<=x<600 and 480>y>=420:
        return 0,5
    elif 600<=x<700 and 480>y>=420:
        return 0,6
    elif 700<=x<800 and 480>y>=420:
        return 0,7
    elif 800<=x<900 and 480>y>=420:
        return 0,8
    elif 900<=x<=1000 and 480>y>=420:
        return 0,9

    if 0<=x<100 and 540>y>=480:
        return 1,0
    elif 100<=x<200 and 540>y>=480:
        return 1,1
    elif 200<=x<300 and 540>y>=480:
        return 1,2
    elif 300<=x<400 and 540>y>=480:
        return 1,3
    elif 400<=x<500 and 540>y>=480:
        return 1,4
    elif 500<=x<600 and 540>y>=480:
        return 1,5
    elif 600<=x<700 and 540>y>=480:
        return 1,6
    elif 700<=x<800 and 540>y>=480:
        return 1,7
    elif 800<=x<900 and 540>y>=480:
        return 1,8
    elif 900<=x<=1000 and 540>y>=480:
        return 1,9

    if 0<=x<100 and 600>y>=540:
        return 2,0
    elif 100<=x<200 and 600>y>=540:
        return 2,1
    elif 200<=x<300 and 600>y>=540:
        return 2,2
    elif 300<=x<400 and 600>y>=540:
        return 2,3
    elif 400<=x<500 and 600>y>=540:
        return 2,4
    elif 500<=x<600 and 600>y>=540:
        return 2,5
    elif 600<=x<700 and 600>y>=540:
        return 2,6
    elif 700<=x<800 and 600>y>=540:
        return 2,7
    elif 800<=x<900 and 600>y>=540:
        return 2,8
    elif 900<=x<=1000 and 600>y>=540:
        return 2,9

    if 0<=x<100 and 660>y>=600:
        return 3,0
    elif 100<=x<200 and 660>y>=600:
        return 3,1
    elif 200<=x<300 and 660>y>=600:
        return 3,2
    elif 300<=x<400 and 660>y>=600:
        return 3,3
    elif 400<=x<500 and 660>y>=600:
        return 3,4
    elif 500<=x<600 and 660>y>=600:
        return 3,5
    elif 600<=x<700 and 660>y>=600:
        return 3,6
    elif 700<=x<800 and 660>y>=600:
        return 3,7
    elif 800<=x<900 and 660>y>=600:
        return 3,8
    elif 900<=x<=1000 and 660>y>=600:
        return 3,9

    if 0<=x<100 and 720>y>=660:
        return 4,0
    elif 100<=x<200 and 720>y>=660:
        return 4,1
    elif 200<=x<300 and 720>y>=660:
        return 4,2
    elif 300<=x<400 and 720>y>=660:
        return 4,3
    elif 400<=x<500 and 720>y>=660:
        return 4,4
    elif 500<=x<600 and 720>y>=660:
        return 4,5
    elif 600<=x<700 and 720>y>=660:
        return 4,6
    elif 700<=x<800 and 720>y>=660:
        return 4,7
    elif 800<=x<900 and 720>y>=660:
        return 4,8
    elif 900<=x<=1000 and 720>y>=660:
        return 4,9
    return -1,-1