stat = {0: {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True},
        1: {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True},
        2: {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True},
        3: {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True},
        4: {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}}

pos_x = [[50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],
         [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]]

pos_y = [[450, 450, 450, 450, 450, 450, 450, 450, 450, 450],
         [510, 510, 510, 510, 510, 510, 510, 510, 510, 510],
         [570, 570, 570, 570, 570, 570, 570, 570, 570, 570],
         [630, 630, 630, 630, 630, 630, 630, 630, 630, 630],
         [690, 690, 690, 690, 690, 690, 690, 690, 690, 690]]

pos = [(50, 450), (150, 450), (250, 450), (350, 450), (450, 450),
 (550, 450), (650, 450), (750, 450), (850, 450), (950, 450),
 (50, 510), (150, 510), (250, 510), (350, 510), (450, 510),
 (550, 510), (650, 510), (750, 510), (850, 510), (950, 510),
 (50, 570), (150, 570), (250, 570), (350, 570), (450, 570),
 (550, 570), (650, 570), (750, 570), (850, 570), (950, 570),
 (50, 630), (150, 630), (250, 630), (350, 630), (450, 630),
 (550, 630), (650, 630), (750, 630), (850, 630), (950, 630),
 (50, 690), (150, 690), (250, 690), (350, 690), (450, 690),
 (550, 690), (650, 690), (750, 690), (850, 690), (950, 690)]

# for i in range(5):
#     for j in range(10):
#         print(pos_x[i][j],pos_y[i][j])
#     print('--')

def check_brick(x,y):
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


""" x
0<=x<100,100<=x<200,200<=x<300,300<=x<400,400<=x<500,
500<=x<600,600<=x<700,700<=x<800,800<=x<900,900<=x<=1000
    y 
y>=420,y>=480,y>=540,y>=600,y>=660
"""
x,y = check_brick(1000,-10)
print(x,y)