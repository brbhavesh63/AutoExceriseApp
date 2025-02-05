import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Bhavesh\\PycharmProjects\\AutoExceriseApp\\Configurations\\config.ini")

class readConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

#################### SIGNUP INFO START ########################
    @staticmethod
    def getName():
        name = config.get('signup info','name')
        return name

    @staticmethod
    def getSignupEmail():
        email = config.get('signup info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('signup info','password')
        return password

    @staticmethod
    def getDay():
        day = config.get('signup info', 'day')
        return day

    @staticmethod
    def getMonth():
        month = config.get('signup info' , 'month')
        return month

    @staticmethod
    def getYear():
        year = config.get('signup info', 'year')
        return year

    @staticmethod
    def getFirstName():
        fname = config.get('signup info', 'firstname')
        return fname

    @staticmethod
    def getLastName():
        lname = config.get('signup info', 'lastname')
        return lname

    @staticmethod
    def getAddress():
        address = config.get('signup info', 'address')
        return address

    @staticmethod
    def getCity():
        city = config.get('signup info', 'city')
        return  city

    @staticmethod
    def getCompany():
        cname = config.get('signup info', 'company')
        return  cname

    @staticmethod
    def getState():
        state = config.get('signup info', 'state')
        return state

    @staticmethod
    def getZipcode():
        zipcode = config.get('signup info', 'zipcode')
        return zipcode

    @staticmethod
    def getMobile():
        mobile = config.get('signup info', 'mobile')
        return mobile
#####################  SIGNUP INFO END HERE #######################

##################### Valid Login Info ##########################

    @staticmethod
    def getLoginvalidEmail():
        email = config.get('validlogin info', 'email')
        return email

    @staticmethod
    def getLoginvalidPassword():
        password = config.get('validlogin info','password')
        return password
################### Valid Login Info End ###########################

################### Contact Us Info ###########################


    @staticmethod
    def getContactName():
        name = config.get('contactus info', 'name')
        return name

    @staticmethod
    def getContactEmail():
        email = config.get('contactus info', 'email')
        return  email

    @staticmethod
    def getSubject():
        subject = config.get('contactus info', 'subject')
        return subject

    @staticmethod
    def getMessage():
        message = config.get('contactus info', 'message')
        return  message


##################### SEND CARD DETAILS ######################

    @staticmethod
    def getCardName():
        name = config.get('card info','name')
        return name

    @staticmethod
    def getCardNumber():
        cardnumber = config.get('card info','cardnumber')
        return cardnumber

    @staticmethod
    def getCVV():
        cvv = config.get('card info','cvv')
        return cvv

    @staticmethod
    def getExpireMonth():
        expiremonth = config.get('card info','expiremonth')
        return expiremonth

    @staticmethod
    def getExpireYear():
        expireyear = config.get('card info','expireyear')
        return expireyear
