import sys

operation = sys.argv[1]

if operation == "--help" or "-h":
    print("heres help")

elif operation == "--version" or "-v":
    print("Storm Code V0.1.0")

elif operation == "--help version":
    print("Displays the Code Editors version ")
    
elif operation == "--Update":
    print("we are working on that")