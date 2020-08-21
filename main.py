from selenium import webdriver

from time import sleep

import os

import json


class InstaBot:

    def getBrowserOfChoice(self):

        try:
            # opening settings file 
            with open(self.path) as fil:
                data = json.loads(fil.read())
        except FileNotFoundError:
            print("settings file is missing")
            input("\n\npress enter to continue ...")
            exit()

        # if the browser is not set then ask for the choice
        if(data["browser_of_choice"] == ""):
            print("1. Chrome")
            print("2. Firefox")

            print("\nAlso you can set your default browser in settings file")

            try:
                choice = int(input("\nenter the index of browser of choice (1 or 2) : "))

                if((choice < 1) or (choice > 2)):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("please enter a valid choice")
                    input("\n\npress enter to continue ...")
                    self.getBrowserOfChoice()

                
                else:
                    return choice

            except Exception:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("please enter a valid choice")
                input("\n\npress enter to continue ...")
                self.getBrowserOfChoice()

        
        # for chrome
        elif(data["browser_of_choice"] == "chrome"):
            return 1

        # for firefox
        elif(data["browser_of_choice"] == "firefox"):
            return 2
        
        # else ask for input
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("wrong browser setted in settings file")
            input("\n\npress enter to continue ...")
            os.system('cls' if os.name == 'nt' else 'clear')


            print("1. Chrome")
            print("2. Firefox")

            print("\nAlso you can set your default browser in settings file")

            try:
                choice = int(input("\nenter the index of browser of choice (1 or 2) : "))

                if((choice < 1) or (choice > 2)):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("please enter a valid choice")
                    input("\n\npress enter to continue ...")
                    self.getBrowserOfChoice()

                
                else:
                    return choice

            except Exception:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("please enter a valid choice")
                input("\n\npress enter to continue ...")
                self.getBrowserOfChoice()


    
    def userNameAndPass(self):

        os.system('cls' if os.name == 'nt' else 'clear')

        # count for username's
        count = 1

        # user name and password list
        userPassList = []

        try:
            # opening settings file 
            with open(self.path) as fil:
                data = json.loads(fil.read())
        except FileNotFoundError:
            print("settings file is missing")
            input("\n\npress enter to continue ...")
            exit()

        # checking for number of username in settings file
        for i in range(1,11):
            string = "username"
            string = string + str(i)

            string2 = "password"
            string2 = string2 + str(i)

            try:
                getFromDataUserName = data[string]
                getFromDataPass = data[string2]

                # if username exit but is empty then it will be ignored and else 
                if(not(getFromDataUserName == "")):
                    print("{}. {} = {}".format(count, string , getFromDataUserName))
                    count = count + 1
                    
                    # adding user name and pass to temp list so that it can be appended to user Pass list
                    tempList = []
                    tempList.append(getFromDataUserName)
                    tempList.append(getFromDataPass)
                    userPassList.append(tempList)
                    
            except KeyError:
                pass

        # if not user name is found
        if(len(userPassList) == 0):
            print("no user found , please enter the username and pass in settings file")
            return False

        # if only one user name is found
        elif(len(userPassList) == 1):
            return userPassList[0]

        # else
        else:
            try:
                choice = int(input("\nSelect the username from Above (Enter the index number) : "))

                if((choice < 1) or (choice > (len(userPassList)+1))):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("please enter a valid choice")
                    input("\n\npress enter to continue ...")
                    self.userNameAndPass()

                
                else:
                    return userPassList[choice-1]

            except Exception:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("please enter a valid choice")
                input("\n\npress enter to continue ...")
                self.userNameAndPass()

    def __init__(self):

        # settings file path
        self.path = "mySettings.json"

        # getting user name and pass and assigning
        listElement = self.userNameAndPass()
        self.username = listElement[0]
        self.password = listElement[1]

        # setting browser driver
        returnBrowser = self.getBrowserOfChoice()
        if(returnBrowser == 1):
            self.driver = webdriver.Firefox()
        elif(returnBrowser == 2):
            self.driver = webdriver.Chrome()


    def loginInInsta(self):
        self.driver.get("https://instagram.com")
        sleep(5)

        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(self.password)

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

    
        

        

        # os.system("cls")
        # input("press enter after opening followers tab and loading all")
        # input("\nagain press enter to continue")

        # os.system("cls")
        

        # # finding followers
        # followers = []
        # print("finding followers ...")
        # tempFollowers = self.driver.find_elements_by_class_name("_0imsa ")
        
        # print("\ntotal followers found = {}".format(len(tempFollowers)))


        # print("converting Followers Found")
        # for i in tempFollowers:
        #     followers.append(str(i.text))

        # os.system("pause")
        # os.system("cls")


        # # finding following 
        # following = []
        # input("press enter after opening following tab and loading all")
        # input("\nagain press enter to continue")

        # os.system("cls")

        # print("finding following...")
        # tempFollowing = self.driver.find_elements_by_class_name("_0imsa ")

        # print("\ntotal following found = {}".format(len(tempFollowing)))

        # print("converting following Found")

        # for i in tempFollowing:
        #     following.append(str(i.text))

        # notFollowed = 0

        # os.system("cls")
        # for i in following:
        #     if(not(i in followers)):
        #         print(i)
        #         notFollowed += 1

        # print("\nPeople who have not folloed  = {}\n\n".format(notFollowed))

        # os.system("pause")

        # print("script will end in 30 sec")

        # os.system("cls")
        # sleep(30)




                






if __name__ == "__main__":
    print(getBrowserOfChoice())



