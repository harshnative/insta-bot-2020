from selenium import webdriver

from time import sleep

import os

import json

from threading import Thread


# time left loading animation thread
timeForAn = 0

class LoadingAnimation(Thread):

    def run(self):
        global timeForAn
        time = timeForAn

        print("\n")
        
        while(time):
            sleep(1)
            print("\rtime left = {} secs".format(time) , end = "")

            if(time <= 1):
                print("\ngetting things done please wait ..\n")
            time -= 1



# main class
class InstaBot:

    def getBrowserOfChoice(self):

        os.system('cls' if os.name == 'nt' else 'clear')

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

        self.NonFollowers = 0

        # output file path 
        self.outputFilePath = "NonFollowers.txt"


        # settings file path
        self.path = "settings.json"

        # getting user name and pass and assigning
        listElement = self.userNameAndPass()
        self.username = listElement[0]
        self.password = listElement[1]

        # setting browser driver
        returnBrowser = self.getBrowserOfChoice()
        if(returnBrowser == 2):
            self.driver = webdriver.Firefox()
        elif(returnBrowser == 1):
            self.driver = webdriver.Chrome()


    def loginInInsta(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("logging into instagram , this process will take 30 seconds or more")

        # getting to site 
        self.driver.get("https://instagram.com")
        sleep(5)

        # filling details
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(self.password)

        # clicking submit
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)

        # clicking not now for save login info
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(5)
        except Exception:
            pass
        
        # clicking not now on insta
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(5)
        except Exception:
            pass

        # going to my username
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(5)

    
    def getFollowers(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("finding followers\n")

        stringToPass = self.username + "/" + "followers"

        # getting number of followers
        numberOfFollowers = self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(stringToPass))
        numberOfFollowers = numberOfFollowers.text
        tempList = numberOfFollowers.split()
        string = ""
        for i in tempList:
            try:
                for j in i:
                    if(not(j == ",")):
                        string = string + j
                numberOfFollowers = int(string)
            except Exception:
                pass
        

        print("this process will take {} secs or more".format(numberOfFollowers/6))

        # starting time left animation
        timeLeftAn = LoadingAnimation()

        global timeForAn 
        timeForAn = (int(numberOfFollowers/6))
        timeLeftAn.start()

        # click on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(stringToPass)).click()
        sleep(5)

        
        # scrolling
        fBody  = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        scroll = 0

        while scroll < int(numberOfFollowers/3): 
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(0.5)
            scroll += 1

        followers = []
        
        tempFollowers = self.driver.find_elements_by_class_name("_0imsa")
        
        print("\ntotal followers found = {}".format(len(tempFollowers)))


        print("\nconverting Followers Found")
        for i in tempFollowers:
            followers.append(str(i.text))

        # closing popup
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        
        timeLeftAn.join()
        return followers


    def getFollowing(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("finding following\n")

        stringToPass = self.username + "/" + "following"
        sleep(5)

        # getting number of following
        numberOfFollowing = self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(stringToPass))
        numberOfFollowing = numberOfFollowing.text

        tempList = numberOfFollowing.split()

        string = ""
        for i in tempList:
            try:
                for j in i:
                    if(not(j == ",")):
                        string = string + j
                numberOfFollowing = int(string)
            except Exception:
                pass


        print("this process will take {} secs or more".format(numberOfFollowing/6))

        # starting time left animation
        timeLeftAn = LoadingAnimation()

        global timeForAn 
        timeForAn = (int(numberOfFollowing/6))

        timeLeftAn.start()

        # click on following
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(stringToPass)).click()
        sleep(5)

        
        # scrolling
        fBody  = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        scroll = 0


        
        while scroll < int(numberOfFollowing/3): 
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(0.5)
            scroll += 1

        following = []
        
        tempFollowing = self.driver.find_elements_by_class_name("_0imsa")
        
        print("\ntotal following found = {}".format(len(tempFollowing)))


        print("\nconverting following Found")
        for i in tempFollowing:
            following.append(str(i.text))


        timeLeftAn.join()
        return following
        
    
    def getUnFollowers(self):
        self.loginInInsta()
        followers = self.getFollowers()
        following = self.getFollowing()

        nonFollowersCount = 0

        os.system('cls' if os.name == 'nt' else 'clear')
        print("calculating non followers")

        with open(self.outputFilePath , "w") as fili:
            for i in following:
                if(i not in followers):
                    nonFollowersCount += 1
                    fili.write(i)
                    fili.write("\n")

            self.NonFollowers = nonFollowersCount
            fili.write("\n\nNumber of people who are not following you = {}".format(nonFollowersCount))


        print("\nNon Followers as been ouputted to NonFollowers.txt present in same folder")

        input("\n\npress enter to continue")
        





if __name__ == "__main__":
    
    try:
        print("please do not close the pop up browser")
        input("\n\npress enter to continue ...")
        i = InstaBot()
        i.getUnFollowers()
    except Exception as e:
        print("make sure you are connected to the internet or using any of the following browser")
        print("\nChrome 84 or firefox version 79")
        
        print("\n\nfor dev = {}".format(e))

        input("\n\npress enter to continue ...")