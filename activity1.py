class Activity1:
    #1. Create method to initialize class
    def __init__(self):
        #2. Variable declaration
        self.editor_name = 'Visual Studio code'
        self.language = 'Python'
        self.version = 3.0
        self.user_name = ""
        self.country_list = []
    
    #3. MEthod that will prinnt the value of the variables
    def show_info(self):
        print(f'We are programming in {self.editor_name}, with the language {self.language} {self.version}')

    def say_hi():
        print("Hello world")


    def input_user_data(self):
        self.user_name = input("Enter your name: \n")
        while True:
            try:
                age = int(input("Age: \n"))
                break
            except:
                print("Error, isn't a numerical value")
            print(f'{self.user_name}, is {age} years old.')

    def input_frameworks_data():
        framework_list = []
        while True:
            try:
                framework_count = int(input("How many frameworks do you know?\n"))
                for item_framework in range(framework_count):
                    framework_name = input(f'   {item_framework}: ')
                    #append() adds framework to the end of the list
                    framework_list.append(framework_name)
                break
            except:
                print("Error, expected a number")


    def input_language_data():
        language_list = []
        while True:
            try:
                language_count = int(input("How many programming lanaguages do you know?\n"))
                for item_language in range(language_count):
                    language_name = input(f'    {item_language}: ')
                    #append() adds language to the end of the list
                    language_list.append(language_name)
                break
            except:
                print("Error, expected a number")


    def insert_student_data():
        print("Enter the following information:\n")
        students_list = []
        while True:
            try:
                student_counter = int(input("How many student will you add to the system: "))
                for current_student in range(1, student_counter+1):    
                    student_name = str(input("    name: "))
                    student_id = input("    ID: ")
                    students_list.append(current_student, student_name, student_id)
                break
            except:
                print("Error, expected a number")


    def countries_data(self):
        while True:
            try:
                country_counter = int(input("How many countries will you name: "))
                if country_counter == -1:
                    break
                for current_country in range(1, country_counter+1):
                    country_name = input("    Country: ")
                    while True:
                        try:
                            country_population = int(input("        Population: "))
                            break
                        except:
                            print("Error, expected a number")
                    self.country_list.append(current_country, country_name, country_population)
                print(f'            Countries:\n                {self.country_list}')
                break
            except:
                print("Error, expected a number")

