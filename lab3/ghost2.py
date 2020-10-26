import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((666, 865))

# Alpha surfaces
sur1 = pygame.Surface((666, 865))
sur1.set_alpha(100)
sur2 = pygame.Surface((666, 865))
sur2.set_alpha(100)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MOONLIGHT = (230, 230, 230)
GHOST = (179, 179, 179)
GHOSTEYES = (135, 205, 222)
HOUSE = (54, 46, 18)
SKY = (152, 152, 152)
BALCONY = (35, 35, 35)
BALCONYDARK = (25, 25, 25)
PIPE = (40, 40, 40)
CLOUDLIGHTALPHA12 = (102, 102, 102)
CLOUDLIGHTALPHA3 = (52, 52, 52)
CLOUDLIGHT = (77, 77, 77)
CLOUDDARKALPHA = (26, 26, 26)
CLOUDDARK = (51, 51, 51)
WINDOWDARK = (36, 14, 0)
WINDOWLIGHT = (212, 170, 0)
CRATER = (175, 167, 146)
WINDOWUP = (78, 69, 64)
EXTRAHOUSECOLOR = (0, 74, 0)


# Sky and clouds between houses
rect(screen, BLACK, (0, 0, 666, 865))
ellipse(sur2, CLOUDLIGHTALPHA12, (291, 437, 520, 63))
ellipse(sur2, CLOUDLIGHTALPHA12, (0, 499, 343, 59))

# The big ghost is drawn on 3 surfaces. Order: body, body outline,
# head, eyes, pupils, flares.
polygon(sur1, GHOST, ([555, 693], [561, 693], [599, 722], [615, 737],
                        [637, 756], [640, 781], [633, 787], [622, 789],
                        [611, 798], [608, 810], [601, 824], [581, 824],
                        [568, 822], [511, 830], [535, 845], [522, 846],
                        [505, 826], [485, 815], [452, 820], [465, 798],
                        [468, 788], [487, 761], [487, 753], [495, 739],
                        [500, 715], [555, 693]))
polygon(sur1, BLACK, ([555, 693], [561, 693], [599, 722], [615, 737],
                        [637, 756], [640, 781], [633, 787], [622, 789],
                        [611, 798], [608, 810], [601, 824], [581, 824],
                        [568, 822], [511, 830], [535, 845], [522, 846],
                        [505, 826], [485, 815], [452, 820], [465, 798],
                        [468, 788], [487, 761], [487, 753], [495, 739],
                        [500, 715], [555, 693]), 3)
circle(sur1, GHOST, (527, 700), 30)
circle(sur1, GHOSTEYES, (512, 702), 8)
circle(sur1, GHOSTEYES, (539, 697), 8)
circle(sur1, BLACK, (509, 701), 3)
circle(sur1, BLACK, (537, 696), 3)
line(sur1, WHITE, [517, 696], [511, 699], 2)
line(sur1, WHITE, [543, 691], [538, 695], 2)
polygon(sur2, GHOST, ([555, 693], [561, 693], [599, 722], [615, 737],
                        [637, 756], [640, 781], [633, 787], [622, 789],
                        [611, 798], [608, 810], [601, 824], [581, 824],
                        [568, 822], [511, 830], [535, 845], [522, 846],
                        [505, 826], [485, 815], [452, 820], [465, 798],
                        [468, 788], [487, 761], [487, 753], [495, 739],
                        [500, 715], [555, 693]))
polygon(sur2, BLACK, ([555, 693], [561, 693], [599, 722], [615, 737],
                        [637, 756], [640, 781], [633, 787], [622, 789],
                        [611, 798], [608, 810], [601, 824], [581, 824],
                        [568, 822], [511, 830], [535, 845], [522, 846],
                        [505, 826], [485, 815], [452, 820], [465, 798],
                        [468, 788], [487, 761], [487, 753], [495, 739],
                        [500, 715], [555, 693]), 3)
circle(sur2, GHOST, (527, 700), 30)
circle(sur2, GHOSTEYES, (512, 702), 8)
circle(sur2, GHOSTEYES, (539, 697), 8)
circle(sur2, BLACK, (509, 701), 3)
circle(sur2, BLACK, (537, 696), 3)
line(sur2, WHITE, [517, 696], [511, 699], 2)
line(sur2, WHITE, [543, 691], [538, 695], 2)
polygon(screen, GHOST, ([555, 693], [561, 693], [599, 722], [615, 737],
                          [637, 756], [640, 781], [633, 787], [622, 789],
                          [611, 798], [608, 810], [601, 824], [581, 824],
                          [568, 822], [511, 830], [535, 845], [522, 846],
                          [505, 826], [485, 815], [452, 820], [465, 798],
                          [468, 788], [487, 761], [487, 753], [495, 739],
                          [500, 715], [555, 693]))
polygon(screen, BLACK, ([555, 693], [561, 693], [599, 722], [615, 737],
                          [637, 756], [640, 781], [633, 787], [622, 789],
                          [611, 798], [608, 810], [601, 824], [581, 824],
                          [568, 822], [511, 830], [535, 845], [522, 846],
                          [505, 826], [485, 815], [452, 820], [465, 798],
                          [468, 788], [487, 761], [487, 753], [495, 739],
                          [500, 715], [555, 693]), 3)
circle(screen, GHOST, (527, 700), 30)
circle(screen, GHOSTEYES, (512, 702), 8)
circle(screen, GHOSTEYES, (539, 697), 8)
circle(screen, BLACK, (509, 701), 3)
circle(screen, BLACK, (537, 696), 3)
line(screen, WHITE, [517, 696], [511, 699], 2)
line(screen, WHITE, [543, 691], [538, 695], 2)

# Small ghosts looking to the right. a, b - array of displacements.
# k - coefficient of turning. m, n - variables for displacement.
a = [-25, 0, 583, 751, 732]
b = [-46, 0, -63, -173, -219]
for i in range (2):
    k = 1
    m = a[i]
    n = b[i]
    polygon(sur2, GHOST, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                            [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                            [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                            [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                            [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                            [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                            [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                            [118*k + m, 785 + n]))
    polygon(sur2, BLACK, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                            [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                            [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                            [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                            [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                            [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                            [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                            [118*k + m, 785 + n]), 2)
    circle(sur2, GHOST, (134*k + m, 789 + n), 13)
    circle(sur2, GHOSTEYES, (127*k + m, 787 + n), 3)
    circle(sur2, GHOSTEYES, (141*k + m, 790 + n), 3)
    circle(sur2, BLACK, (127*k + m, 787 + n), 1)
    circle(sur2, BLACK, (141*k + m, 790 + n), 1)
    
# Small ghosts looking to the left.
for i in range (2, 5):
    k = -1
    m = a[i]
    n = b[i]
    polygon(sur2, GHOST, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                            [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                            [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                            [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                            [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                            [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                            [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                            [118*k + m, 785 + n]))
    polygon(sur2, BLACK, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                            [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                            [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                            [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                            [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                            [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                            [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                            [118*k + m, 785 + n]), 2)
    circle(sur2, GHOST, (134*k + m, 789 + n), 13)
    circle(sur2, GHOSTEYES, (127*k + m, 787 + n), 3)
    circle(sur2, GHOSTEYES, (141*k + m, 790 + n), 3)
    circle(sur2, BLACK, (127*k + m, 787 + n), 1)
    circle(sur2, BLACK, (141*k + m, 790 + n), 1)

# Adding brightness to small ghosts. k - coefficient of turning.
# m, n - variables for displacement.
k = -1
m = 751
n = -173
polygon(sur1, GHOST, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                        [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                        [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                        [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                        [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                        [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                        [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                        [118*k + m, 785 + n]))
polygon(sur1, BLACK, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                        [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                        [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                        [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                        [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                        [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                        [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                        [118*k + m, 785 + n]), 2)
circle(sur1, GHOST, (134*k + m, 789 + n), 13)
circle(sur1, GHOSTEYES, (127*k + m, 787 + n), 3)
circle(sur1, GHOSTEYES, (141*k + m, 790 + n), 3)
circle(sur1, BLACK, (127*k + m, 787 + n), 1)
circle(sur1, BLACK, (141*k + m, 790 + n), 1)
k = 1
m = -25
n = -46
polygon(sur1, GHOST, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                        [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                        [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                        [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                        [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                        [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                        [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                        [118*k + m, 785 + n]))
polygon(sur1, BLACK, ([118*k + m, 785 + n], [112*k + m, 786 + n], [99*k + m, 797 + n],
                        [95*k + m, 799 + n], [83*k + m, 810 + n], [73*k + m, 820 + n],
                        [72*k + m, 834 + n], [82*k + m, 837 + n], [87*k + m, 841 + n],
                        [93*k + m, 855 + n], [114*k + m, 855 + n], [131*k + m, 870 + n],
                        [145*k + m, 856 + n], [154*k + m, 851 + n], [172*k + m, 853 + n],
                        [165*k + m, 841 + n], [164*k + m, 836 + n], [157*k + m, 826 + n],
                        [154*k + m, 817 + n], [149*k + m, 810 + n], [146*k + m, 796 + n],
                        [118*k + m, 785 + n]), 2)
circle(sur1, GHOST, (134*k + m, 789 + n), 13)
circle(sur1, GHOSTEYES, (127*k + m, 787 + n), 3)
circle(sur1, GHOSTEYES, (141*k + m, 790 + n), 3)
circle(sur1, BLACK, (127*k + m, 787 + n), 1)
circle(sur1, BLACK, (141*k + m, 790 + n), 1)
    
# Sky with alpha clouds
rect(screen, SKY, (0, 0, 666, 393))
rect(sur1, SKY, (0, 0, 666, 393))
ellipse(screen, BLACK, (325, 203, 418, 60))
ellipse(sur2, CLOUDDARKALPHA, (325, 203, 418, 60))
ellipse(sur2, CLOUDLIGHTALPHA3, (111, 360, 706, 56))

# Houses are drawn in this order: body, pipe, roof, other pipes, upper windows,
# vertical partitions on windows, horisontal partitions on windows,
# balcony. m, n - variables for displacement.

# Upper right house
m = 257
n = -124
rect(sur1, HOUSE, (226 + m, 347 + n, 177, 244))
rect(sur1, PIPE, (332 + m, 305 + n, 6, 27))
polygon(sur1, BLACK, ([237 + m, 328 + n], [211 + m, 347 + n], [420 + m, 347 + n],
                        [390 + m, 328 + n]))
rect(sur1, PIPE, (376 + m, 304 + n, 6, 36))
rect(sur1, PIPE, (262 + m, 285 + n, 12, 55))
rect(sur1, PIPE, (252 + m, 303 + n, 6, 36))
rect(sur1, WINDOWUP, (240 + m, 348 + n, 19, 92))
rect(sur1, WINDOWUP, (274 + m, 348 + n, 19, 92))
rect(sur1, WINDOWUP, (319 + m, 348 + n, 19, 92))
rect(sur1, WINDOWUP, (364 + m, 348 + n, 19, 92))
line(sur1, BLACK, (249 + m, 348 + n), (249 + m, 440 + n))
line(sur1, BLACK, (283 + m, 348 + n), (283 + m, 440 + n))
line(sur1, BLACK, (328 + m, 348 + n), (328 + m, 440 + n))
line(sur1, BLACK, (373 + m, 348 + n), (373 + m, 440 + n))
line(sur1, BLACK, (240 + m, 394 + n), (259 + m, 394 + n))
line(sur1, BLACK, (274 + m, 394 + n), (293 + m, 394 + n))
line(sur1, BLACK, (319 + m, 394 + n), (338 + m, 394 + n))
line(sur1, BLACK, (364 + m, 394 + n), (383 + m, 394 + n))
rect(sur1, WINDOWDARK, (246 + m, 520 + n, 33, 42))
rect(sur1, WINDOWDARK, (301 + m, 520 + n, 33, 42))
rect(sur1, WINDOWLIGHT, (350 + m, 520 + n, 33, 42))
rect(sur1, BALCONY, (215 + m, 421 + n, 4, 23))
rect(sur1, BALCONY, (219 + m, 410 + n, 194, 11))
rect(sur1, BALCONY, (237 + m, 419 + n, 10, 27))
rect(sur1, BALCONY, (269 + m, 419 + n, 10, 27))
rect(sur1, BALCONY, (304 + m, 419 + n, 10, 27))
rect(sur1, BALCONY, (341 + m, 419 + n, 10, 27))
rect(sur1, BALCONY, (378 + m, 419 + n, 10, 27))
rect(sur1, BALCONY, (413 + m, 421 + n, 4, 27))
rect(sur1, BALCONY, (208 + m, 442 + n, 216, 25))

screen.blit(sur1, (0, 0))

# Central house
m = 0
n = 0
rect(screen, HOUSE, (226 + m, 347 + n, 177, 244))
rect(screen, PIPE, (332 + m, 305 + n, 6, 27))
polygon(screen, BLACK, ([237 + m, 328 + n], [211 + m, 347 + n], [420 + m, 347 + n],
                          [390 + m, 328 + n]))
rect(screen, PIPE, (376 + m, 304 + n, 6, 36))
rect(screen, PIPE, (262 + m, 285 + n, 12, 55))
rect(screen, PIPE, (252 + m, 303 + n, 6, 36))
rect(screen, WINDOWUP, (240 + m, 348 + n, 19, 92))
rect(screen, WINDOWUP, (274 + m, 348 + n, 19, 92))
rect(screen, WINDOWUP, (319 + m, 348 + n, 19, 92))
rect(screen, WINDOWUP, (364 + m, 348 + n, 19, 92))
line(screen, BLACK, (249 + m, 348 + n), (249 + m, 440 + n))
line(screen, BLACK, (283 + m, 348 + n), (283 + m, 440 + n))
line(screen, BLACK, (328 + m, 348 + n), (328 + m, 440 + n))
line(screen, BLACK, (373 + m, 348 + n), (373 + m, 440 + n))
line(screen, BLACK, (240 + m, 394 + n), (259 + m, 394 + n))
line(screen, BLACK, (274 + m, 394 + n), (293 + m, 394 + n))
line(screen, BLACK, (319 + m, 394 + n), (338 + m, 394 + n))
line(screen, BLACK, (364 + m, 394 + n), (383 + m, 394 + n))
rect(screen, WINDOWDARK, (246 + m, 520 + n, 33, 42))
rect(screen, WINDOWDARK, (301 + m, 520 + n, 33, 42))
rect(screen, WINDOWLIGHT, (350 + m, 520 + n, 33, 42))
rect(screen, BALCONY, (215 + m, 421 + n, 4, 23))
rect(screen, BALCONY, (219 + m, 410 + n, 194, 11))
rect(screen, BALCONY, (237 + m, 419 + n, 10, 27))
rect(screen, BALCONY, (269 + m, 419 + n, 10, 27))
rect(screen, BALCONY, (304 + m, 419 + n, 10, 27))
rect(screen, BALCONY, (341 + m, 419 + n, 10, 27))
rect(screen, BALCONY, (378 + m, 419 + n, 10, 27))
rect(screen, BALCONY, (413 + m, 421 + n, 4, 27))
rect(screen, BALCONY, (208 + m, 442 + n, 216, 25))

screen.blit(sur2, (0, 0))

# Objects in the sky: moon, craters, clouds.
circle(screen, MOONLIGHT, (597, 81), 57)
circle(screen, CRATER, (615, 66), 15)
circle(screen, CRATER, (628, 45), 3)
circle(screen, CRATER, (598, 56), 11)
circle(screen, CRATER, (571, 66), 18)
circle(screen, CRATER, (562, 92), 13)
circle(screen, CRATER, (574, 115), 8)
circle(screen, CRATER, (589, 116), 11)
ellipse(screen, CLOUDDARK, (32, 88, 521, 63))
ellipse(screen, CLOUDLIGHT, (292, 56, 376, 67))
ellipse(screen, CLOUDLIGHT, (394, 132, 412, 59))

# Lower left house
m = -210
n = 88
rect(screen, EXTRAHOUSECOLOR, (226 + m, 347 + n, 177, 244))
rect(screen, PIPE, (332 + m, 305 + n, 6, 27))
polygon(screen, BLACK, ([237 + m, 328 + n], [211 + m, 347 + n], [420 + m, 347 + n],
                          [390 + m, 328 + n]))
rect(screen, PIPE, (376 + m, 304 + n, 6, 36))
rect(screen, PIPE, (262 + m, 285 + n, 12, 55))
rect(screen, PIPE, (252 + m, 303 + n, 6, 36))
rect(screen, WINDOWUP, (240 + m, 348 + n, 19, 92))
rect(screen, WINDOWUP, (274 + m, 348 + n, 19, 92))
rect(screen, WINDOWUP, (319 + m, 348 + n, 19, 92))
rect(screen, WINDOWUP, (364 + m, 348 + n, 19, 92))
line(screen, BLACK, (249 + m, 348 + n), (249 + m, 440 + n))
line(screen, BLACK, (283 + m, 348 + n), (283 + m, 440 + n))
line(screen, BLACK, (328 + m, 348 + n), (328 + m, 440 + n))
line(screen, BLACK, (373 + m, 348 + n), (373 + m, 440 + n))
line(screen, BLACK, (240 + m, 394 + n), (259 + m, 394 + n))
line(screen, BLACK, (274 + m, 394 + n), (293 + m, 394 + n))
line(screen, BLACK, (319 + m, 394 + n), (338 + m, 394 + n))
line(screen, BLACK, (364 + m, 394 + n), (383 + m, 394 + n))
rect(screen, WINDOWDARK, (246 + m, 520 + n, 33, 42))
rect(screen, WINDOWDARK, (301 + m, 520 + n, 33, 42))
rect(screen, WINDOWLIGHT, (350 + m, 520 + n, 33, 42))
rect(screen, BALCONYDARK, (215 + m, 421 + n, 4, 23))
rect(screen, BALCONYDARK, (219 + m, 410 + n, 194, 11))
rect(screen, BALCONYDARK, (237 + m, 419 + n, 10, 27))
rect(screen, BALCONYDARK, (269 + m, 419 + n, 10, 27))
rect(screen, BALCONYDARK, (304 + m, 419 + n, 10, 27))
rect(screen, BALCONYDARK, (341 + m, 419 + n, 10, 27))
rect(screen, BALCONYDARK, (378 + m, 419 + n, 10, 27))
rect(screen, BALCONYDARK, (413 + m, 421 + n, 4, 27))
rect(screen, BALCONYDARK, (208 + m, 442 + n, 216, 25))

pygame.display.update()
clock = pygame.time.Clock()


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
