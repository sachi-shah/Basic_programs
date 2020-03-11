# Program to caculate marksheet based on marks per semester
import math

rollno = int(input("Enter your roll : "))
name = (input("Enter your name : "))
course = (input("Enter your class : "))

print("----------------------------------------------------------ENTER THEORY MARKS OUT OF 75-------------------------------------------------------------------------------")

dm = int(input("Enter marks obt in dm : "))
pp = int(input("Enter marks obt in pp : "))
wp = int(input("Enter marks obt in wp : "))
oop = int(input("Enter marks obt in oop : "))
it = int(input("Enter marks obt in it tools : "))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("----------------------------------------------------------ENTER PRACTICAL MARKS OUT OF 25----------------------------------------------------------------------------")
dmint = int(input("Enter marks obt in dm internals : "))
ppint = int(input("Enter marks obt in pp internals : "))
wpint = int(input("Enter marks obt in wp internals : "))
oopint = int(input("Enter marks obt in oop internals : "))
itint = int(input("Enter marks obt in it tools internals : "))
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

pptot = pp + ppint
ooptot = oop + oopint
dmtot = dm + dmint
wptot = wp + wpint
ittot = it + itint

obtmarks = dmtot + pptot + wptot + ooptot + ittot
perc = (obtmarks / 500) * 100

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


def grade(t):
    if(t > 80):
        return "O"
    elif(t > 70 and t < 80):
        return "A+"
    elif(t > 60 and t < 70):
        return "A"
    elif(t > 55 and t < 60):
        return "B+"
    elif(t > 50 and t < 55):
        return "B"
    elif(t > 45 and t < 50):
        return "C"
    elif(t > 40 and t < 45):
        return "D"
    else:
        return "F"
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def g(x):
    if(grade(x) == "O"):
        return "10"
    elif(grade(x) == "A+"):
        return "9"
    elif(grade(x) == "A"):
        return "8"
    elif(grade(x) == "B+"):
        return "7"
    elif(grade(x) == "B"):
        return "6"
    elif(grade(x) == "C"):
        return "5"
    elif(grade(x) == "D"):
        return "4"
    else:
        return "0"

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


def final_grade(a):
    if(a == 10):
        return "O"
    elif(a > 9 and a < 10):
        return "A+"
    elif(a > 8 and a < 9):
        return "A"
    elif(a > 7 and a < 8):
        return "B+"
    elif(a > 6 and a < 7):
        return "B"
    elif(a > 5 and a < 6):
        return "C"
    elif(a > 4 and a < 5):
        return "D"
    else:
        return "F"


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = (int(g(dmtot)) * 2) + (int(g(pptot)) * 4) + \
    (int(g(wptot)) * 4) + (int(g(ooptot)) * 4) + (int(g(ittot)) * 4)
b = 2 + 4 + 4 + 4 + 4

v = float(a / b)
sgpa = round(v, 2)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("*********************************************************************MARKSHEET**************************************************************************")
print("student name: ", name)
print("student rollno: ", rollno)
print("student course: ", course)
print("***************************************************************************************************************************************************************")
print("subject \t 100 \t theory \t prac \t total \t grade \t G \t C \t CG \t sum(CG) \t CE \t SGPA \t Final Grade")
print("***************************************************************************************************************************************************************")
print(" dm \t 100 \t", dm, "\t", dmint, "\t", dmtot, "\t", grade(
    dmtot), "\t", g(dmtot), "\t 2 \t", (int(g(dmtot)) * 2), "\t\t\t")
print("pp \t 100 \t", pp, "\t", ppint, "\t", pptot, "\t", grade(
    pptot), "\t", g(pptot), "\t 4 \t", (int(g(pptot)) * 4), "\t\t\t")
print("wp \t 100 \t",
      wp,
      "\t",
      wpint,
      "\t",
      wptot,
      "\t",
      grade(wptot),
      "\t",
      g(wptot),
      "\t 4 \t",
      (int(g(wptot)) * 4),
      "\t",
      a,
      "\t",
      b,
      "\t",
      sgpa,
      "\t",
      final_grade(sgpa))
print("oop \t 100 \t", oop, "\t", oopint, "\t", ooptot, "\t", grade(
    ooptot), "\t", g(ooptot), "\t 4 \t", (int(g(ooptot)) * 4), "\t\t\t")
print("it \t 100 \t", it, "\t", itint, "\t", ittot, "\t", grade(
    ittot), "\t", g(ittot), "\t 4 \t", (int(g(ittot)) * 4), "\t\t\t")
print("***************************************************************************************************************************************************************")
print("total \t 500 \t ", obtmarks)
print("percentage \t ", perc)
print("****************************************************************************************************************************************************************")
print("\t\t\t\t thank you \t\t")
