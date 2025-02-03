# Match statment -> switch in java
#Match the op and execute
#python > 3.10

#Match variable:
#   case pattern1:
#       code block
#   Case pattern2:
#       code block

#Write a program to ask user which browser he want to run automation
browser_name = input("Enter the browser name\n")
match browser_name:
    case "firefox":
        print("Starting Firefox!")
    case "chrome":
        print("Starting chrome!")
    case "Edge":
        print("Starting Edge")
