class Slider:
    """
    Takes the integer values between between 1 and 5 
    
    
    """

    def __init__(self,value):
        self.value= min(abs(value),5)
        

class Range:
    """
    for a numerical range, for indicating the start and end time of somthing for example
    
    """

    def __init__(self,r):
        self.range=r

    def rangeOverlap(self):
        pass

class Id:
    """
    The aim of the id class is to allow scllearer acces to a given student's identificatory predicates 
    Attributes:
    preferredName: A person's preffered name
    idNumber: the student id number
    gender: the students gender (for the purposes of roomsharing)
    allergies: the student's allergies
    """
    def __init__(self,preferredName,idNumber,gender,courseCode,allergies):
        pass

class Habits:
    """
    Denotes general habits 
    Attributes:
    roomSharing: whether or not the student wants to share a room 
    regularSleet: times at which the student usually sleeps
    exceptionalSleep: sleep times during weekends or nights out
    tidyness: how tidy someone is
    sociability: how tidy somone is
    """
    def __init__(self, roomSharing,
                 regularSleep, exceptionalSleep, tidyness,sociability ):
        pass
class Sharing:
    """
    Indicates attitude to sharing a space 
    Attributes:
    othersDaytimeVisitors: how they feel about a roomate briging others round during the day
    othersNighttimeVisitors: how they feel about a roomate briging others round at nigh/evening, potetially to sleep
    daytimeVisitors: how likely soneone is to invite people round dur ing the day
    nighttimeVisitors: how likely somone is to invite people round in the evening/ at night


    """


    def __init__(self, othersDaytimeVisitors,othersNighttimeVisitors,daytimeVisitors, nightimeVisitors ):
        pass

class Interests:
    """
    Provides a persons's interests
    Arrributes: 
    sports 
    
    
    """ 

    def __init__(self, sports, politics, films,filmGenres, music,musicGenres ):
        pass

class Student:
    def __init__(self,id,habits, sharing,interests):
        self.id=id
        self.habits=habits
        self.sharing=sharing
        self.interests=interests
                 
                 
                 
                 
                
        return True