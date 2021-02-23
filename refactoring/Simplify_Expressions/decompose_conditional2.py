# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

low_cholostrol = total_cholostrol < 200
low_ldl = ldl < 100
low_triglyceride = triglyceride < 150

middle_cholostrol = total_cholostrol < 200
middle_ldl = ldl > 160
middle_triglyceride = triglyceride >= 200

high_cholostrol = 200 <total_cholostrol < 240
high_ldl = 130 < ldl < 160
high_triglyceride = 150 <= triglyceride < 200

if low_cholostrol and low_ldl and low_triglyceride:
    # good level
    print('*** Good level of cholestrol ***')
elif high_cholostrol or high_ldl or high_triglyceride:
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif middle_cholostrol or middle_ldl or middle_triglyceride:
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')
