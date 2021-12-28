print("Hello World")
print("Hello to Coursera")


def computepay(hours, rate):
    if hours <= 40:
        pay = rate*hours
        return pay
    else:
        pay = ((hours-40)*1.5*rate) + (40*rate)
        return pay


try:
    hrs = input("Enter Hours:")
    h = float(hrs)
except:
    print("invalid input")
    h = 0
try:
    rph = float(input("Enter rate:"))
except:
    print("invalid input")
    rph = 0

p = computepay(h, rph)
print("Pay", p)
