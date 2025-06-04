vazn = float(input('vazningnikiriting :'))
boy = float(input('boyingani kiriting :'))

if vazn < 1 or vazn >500:
    print(" 1- 500kg oraligida") 
elif boy < 0.5 or boy > 3.0:
    print('Boy 0.5-3.0 m oraligida bolishi kerak')
else:
    BMI = vazn / (boy ** 2)

    if BMI < 18.5:
         print('kam vazn')
    elif BMI < 25:
         print("Normal vazn")
    elif BMI < 30:
        print("Ortiqcha vazn")
    else:
        print("Semizlik")    