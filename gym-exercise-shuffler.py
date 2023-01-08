# -*- coding: utf-8 -*-

import random
import webbrowser


# gym is basically weekdays
gym_days = ("Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday")

# gym workout is what body part you hitting on that day
gym_workout = ("Chest", "Legs", "Shoulders", "Biceps", "Triceps", "Back")

# workout of chest
upper_chest = ('Low Cable Fly\n', 'Incline Barbell Bench Press\n',
               'Incline Dumbbell Press\n', 'Incline Machine Press\n', 'Incline Dumbbell Fly\n')
mid_chest = ('Dumbbell Chest Fly\n', 'Flat Barbell Bench Press\n', 'High Cable Fly\n',
             'Flat Bench Dumbbell Press\n', 'Pullover\n', 'Seated Machine Fly\n')
lower_chest = ('Decline Bench Press\n', 'Decline Dumbbell Fly\n',
               'High To Low Cable Fly\n', 'Decline Dumbbell Press\n')

# workout of legs
quad_legs = ('Dumbbell Split Squat\n', 'Hack Squat\n',
             'Leg Extension\n', 'Stiff Leg Deadlift\n', 'Hamstring Curl\n')
thigh_legs = ('Forward Lunge\n', 'Leg Press\n', 'Squats\n',
              'Smith Machine Squats\n', 'Goblet Squats\n')

# workout of shoulders
shoulders = ('Barbell Overhead Press\n', 'Seated Dumbbell Shoulder Press\n',
             'Side Lateral Raises\n', 'Front Raises\n', 'Face Pulls\n', 'Seated Bent-Over Rear Delt Fly\n')

# workout of biceps
biceps = ('Barbell Curl\n', 'Dumbbell Curl\n', 'Hammer Curl\n', 'Goblet Curl\n',
          'Preacher Curl\n', 'Concentration Curl\n', 'Cable Curl\n', 'Cable Rope Curl\n')

# workout of triceps
triceps = ('Cable Push Downs\n', 'Laying Triceps Extensions\n', 'Close Grip Bench Press\n',
           'Seated Triceps Extensions\n', 'Decline Skull Crusher\n', 'V Grip Cable Push Down\n', 'Rope Push Down\n')

# workout of back
traps = ('Deadlift\n', 'Pull Ups\n', 'Dumbbell Row\n',
         'Seated Cable Row\n', 'Barbell Row\n')
lats = ('Neutral Grip Pulldown\n', 'Bent Over Barbell Row\n',
        'Single Arm Row\n', 'Pullover\n')
lower_back = ('45° Back Extension\n', 'Close Grip Pulldown\n',
              'Wide dumbbell bent-over row\n', 'Reverse fly\n', 'High Seated Cable Pulldown\n')


# code starts 1
# chest workout
def chest():
    print("Chest Workout:\n")
    Chest = random.sample(upper_chest, k=2) + random.sample(mid_chest,
                                                            k=2) + random.sample(lower_chest, k=2)
    for Chest in Chest:
        if Chest == Chest:
            pass
        print(Chest)


# legs workout
def legs():
    print("Legs Workout:\n")
    Legs = random.sample(quad_legs, k=3) + random.sample(thigh_legs, k=3)
    for Legs in Legs:
        if Legs == Legs:
            pass
        print(Legs)


# biceps and triceps workout
def arms():
    print("Arms Workout:\n")
    Arms = random.sample(biceps, k=3) + random.sample(triceps, k=3)
    for Arms in Arms:
        if Arms == Arms:
            pass
        print(Arms)


# shoulder workout
def shoulders():
    print("Shoulder Workout:\n")
    Shoulders = random.sample(shoulders, k=6)
    for Shoulders in Shoulders:
        if Shoulders == Shoulders:
            pass
        print(Shoulders)


# back workout
def back():
    print("Back Workout:\n")
    Back = random.sample(lats, k=2) + random.sample(traps,
                                                    k=2) + random.sample(lower_back, k=2)
    for Back in Back:
        if Back == Back:
            pass
        print(Back)


# code starts 2
# asking which day of the week you training
weekday = input('Which Day Of The Week Is It?\n')
if weekday not in gym_days:
    print('Please Type A Weekday')
    exit()


# code starts 3
# asking which part of the body you hitting
workout = input('Which Part Of The Body You Hitting?\n')
if workout == 'Chest':
    chest()
elif workout == 'Legs':
    legs()
elif workout == 'Arms':
    arms()
elif workout == 'Shoulders':
    shoulders()
elif workout == 'Back':
    back()
elif workout not in gym_workout:
    print('Please Type A Body Part')
else:
    exit()
