try:
    a = 25
    b = 4
    c = "W"
    d = c / a  
except ValueError as e:
    print("There is a value error")
except Exception as e:  
    print("Something went wrong")
finally:
    print("Done")
