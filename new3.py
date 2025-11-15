print("Welcome to our page :)")
def run():
    print("Press 1 to continue.")
    print("Press 2 to exit.")
    choose = int(input("Enter your choice :- "))
    if choose == 2:
       print("Thank for choosing us.")
       exit()
    return True
run()
def languages_library():
    print("press 1 for Python.")
    print("press 2 for C.")
    print("press 3 for Java.")
    print("press 4 for CSS.")
    print("press 5 for HTML.")
languages_library()
import webbrowser
choose = int(input("Enter the nubrer for visit the book you want to see :- "))
if choose == 1:
    print("Python book :- ")
    webbrowser.open("https://developer.mozilla.org/en-US/docs/Glossary/Python")
elif choose == 2:
    print("C book :- ")
    webbrowser.open("https://developer.mozilla.org/en-US/docs/Glossary/Computer_Programming")
elif choose ==3:
    print("Java book :- ")
    webbrowser.open("https://developer.mozilla.org/en-US/docs/Glossary/Java")
elif choose == 4:
    print("CSS :- ")
    webbrowser.open("https://developer.mozilla.org/en-US/docs/Web/CSS")
elif choose == 5:
    print("HTML :- ")
    webbrowser.open("https://developer.mozilla.org/en-US/docs/Web/HTML")
else:
    print("Invalid choose.")

def again():
    while True:
        run()
        languages_library()
        print("Press 1 to continue.")
        print("Press 2 to exit.")
        again = int(input("Enter your choice :- "))
        if again == 2:
            print("Goodbye :)")
        break
again()

