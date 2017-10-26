import math
import random

todayMinutes = 24 * 60

workingMinutes = float(input("How many hours will you work today?\n")) * 60 

sleepingMinutes = float(input("How many hours will you sleep of today?\n")) * 60

eatingMinutes = float(input("How many hours will you spend eating today?\n")) * 60 

drivingMinutes = float(input("How many hours will you spend driving today?\n")) * 60  

cleaningMinutes = float(input("How many hours will you spend cleaning today?\n")) * 60 

whatIsLeft = todayMinutes - (workingMinutes + sleepingMinutes + eatingMinutes +
                            drivingMinutes + cleaningMinutes)
artisticWindows = 45

articisticBreaks = 15

aWaB = 60


sessions = whatIsLeft // 60

thoughtFul = whatIsLeft % 60 


print(str(thoughtFul) + " Minutes available today to do something thoughtful for someone.")

print(str(sessions) + " Sessions available today for creating something!")




# 5/3 is the conversion for minutes to percentage
# I would like to get a breakdown of how many different movies there are and
#how many different things there are each day, to show a very solid proff how
# there is a tremendous gap in shared experience and I want to show
# how there is only so much time in a persons life and I want to show what
# a day in the life of someone in the projects may be compared to someone else
# I want to show how that may be affected
# really I want to prove the cause and effect or simply the presence of a tremendous gap
# in wealth and how it isn't because things are unfair either.

#59 hours each week of free time
#I want to break down someones day to day to show them logically and realistically how
#they can manage their time effectively
# part of addiction is not wanting to deal with reality or being
#incapabale of dealing with reality.
