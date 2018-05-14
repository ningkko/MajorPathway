from PIL import Image
from graphics import *
import tkinter
import tkinter.messagebox

import random
def main():
    # Create the scene
    global scene
    scene = "outside"
    createWindow()
    oneClickObjects()
    drawScene()
    welcome()

    # Animation loop
    while True:

        global k
        k = win.checkKey()

        # End the game
        if k == 'period':
            print( 'Quit the game.' )
            break
        # move, check logic
        elif k == "i":
            computer.inform()
        else:
            mainCharacter.move()
            interact()

    #---------------------------------------------------------------
    # Wait for click
    print ('click to close')
    win.getMouse( )
    win.close( )

#=========== Classes ====================
class Character:
    '''Player class
    '''
    def __init__(self, px, py):
        '''Constructor'''

        self.image = Image( Point(px,py), "front.gif" )
        self.imageID = 'front'
        self.positionX = px
        self.positionY = py
        self.year = 'first year'
        self.classes = []
        self.major = False
        self.advisor = ""
        self.courseNum = 0
        self.GPA=4.0
        
    def graduate(self):
        if semester == "spring" and year == 2022:
            tkinter.messagebox.showinfo("Congratulation","Congratulation! You graduate!")
            
    def rising(self):
        global year
        year +=1
        
    def springToFall(self):
        self.courseNum = 0
        global semester
        if semester == "spring":
            #global semester
            semester = "fall"
        else:
            #global semester
            semester = "spring"
            
    def declare(self, professor):
        '''Declare CS major with certain professor'''
        self.major = True
        self.advisor = professor

    def switchIMG( self, img ):
        '''Switch the image of the character to the one related with the action
        '''

        # First undraw current image
        self.image.undraw()

        # Import images for all actions of the character
        front = Image( Point(self.positionX,self.positionY), 'front.gif')
        back = Image( Point(self.positionX,self.positionY),'back.gif' )
        standleft1 = Image( Point(self.positionX,self.positionY), 'standleft.gif')
        standleft2 = Image( Point(self.positionX,self.positionY), 'standleft.gif')
        standright1 = Image( Point(self.positionX,self.positionY), 'standright.gif')
        standright2 = Image( Point(self.positionX,self.positionY), 'standright.gif')
        walkleft1 = Image( Point(self.positionX,self.positionY), 'walkleft1.gif')
        walkleft2 = Image( Point(self.positionX,self.positionY), 'walkleft2.gif')
        walkright1 = Image( Point(self.positionX,self.positionY), 'walkright1.gif')
        walkright2 = Image( Point(self.positionX,self.positionY), 'walkright2.gif')

        # If want to walk to the left
        if img == 'left':

            # Switch image based on current image
            # To create the motions of walking
            if ( self.imageID == 'walkleft1'):
                self.imageID = 'standleft1'
                self.image = standleft1
            elif (self.imageID == 'standleft1'):
                self.imageID = 'walkleft2'
                self.image = walkleft2
            elif (self.imageID == 'walkleft2'):
                self.imageID = 'standleft2'
                self.image = standleft2
            else:
                self.imageID = 'walkleft1'
                self.image = walkleft1

        # If want to walk to the right
        if img == 'right':
            if ( self.imageID == 'walkright1'):
                self.imageID = 'standright1'
                self.image = standright1
            elif (self.imageID == 'standright1'):
                self.imageID = 'walkright2'
                self.image = walkright2
            elif (self.imageID == 'walkright2'):
                self.imageID = 'standright2'
                self.image = standright2
            else:
                self.imageID = 'walkright1'
                self.image = walkright1

        # If want to show the front of the character
        # (press the downKey)
        if img == 'front':
            self.imageID = 'front'
            self.image = front

        # If want to show the back of the character
        # (press the upKey)
        if img == 'back':
            self.imageID = 'back'
            self.image = back

    def getX(self):
        '''Getter for positionX'''
        return self.positionX

    def getY(self):
        '''Getter for positionY'''
        return self.positionY

    def move( self ):
        '''Make the character move'''

        # Step can control the walking speed of the character
        step = 30

        #If certain key is pressed, make the character move towards certain direction
        #First change its position, then undraw the image to switch the image, and draw the new one
        if (k == leftKey ) and (self.positionX > -580):
            self.positionX -= step
            self.switchIMG( 'left' )
            self.image.draw(win)

        if (k == rightKey ) and (self.positionX < 580):
            self.positionX += step
            self.switchIMG( 'right' )
            self.image.draw(win)

        if (k == upKey) and (self.positionY < 32):
            self.positionY += step
            self.switchIMG( 'back' )
            self.image.draw(win)

        if (k == downKey) and (self.positionY > -32):
            self.positionY -= step
            self.switchIMG( 'front' )
            self.image.draw(win)

    def updateYearTo( self, yr ):
        '''Update the character's class to certain year'''
        if yr == 2:
            self.year = 'sophomore'
        if yr == 3:
            self.year = 'junior'
        if yr == 4:
            self.year = 'senior'

    def updateClasses(self, Lclasses):
        '''Update the classes chosen for the character'''
        self.classes = Lclasses

    def checkInfo():
        '''Check the character's class year and classes that have been taken'''
        return self.year
        return self.classes

    def checkGrade(self):
        '''Check the overall grade of the character'''
        return grade
    def checkMajor(self):
        '''Check if the character have declared CS major'''
        return self.major

class Professor:
    '''Professor
        '''
    # Initialization
    def __init__(self, name, px, py, image):
        self.image = Image(Point(px, py), image)
        self.name = name
        self.positionX = px
        self.positionY = py
    # Getter
    def getX(self):
        return self.positionX
  
    # chat with professor
    def chatWith(self, mainCharacter):
        box1 = tkinter.Tk()
        b1 = tkinter.Button(box1, text = "Chat", command = self.chat)
        b2 = tkinter.Button(box1, text = "Declare", command= lambda: self.declare(mainCharacter))
        b3 = tkinter.Button(box1, text = "Advise", command = self.advise)
        b4 = tkinter.Button(box1, text = "Close", command=box1.destroy)
        b1.pack()        
        b2.pack()
        b3.pack()
        b4.pack()

    def advise(self):
        if mainCharacter.checkMajor() == True and mainCharacter.advisor == professor.name:
            tkinter.messagebox.showinfo("Advising", "Hi, come on in and sit down.")
            box2 = tkinter.Tk()
            b1 = tkinter.Button(box2, text = "Study Away", command = self.studyAway)
            b2 = tkinter.Button(box2, text = "courseTaking", command = self.courseTaking)
            b3 = tkinter.Button(box2, text = "Recommondate", command = self.recommondate)
            b4 = tkinter.Button(box2, text = "Research", command = self.research)
            b5 = tkinter.Button(box2, text = "Close", command = box2.destroy)
            b1.pack()        
            b2.pack()
            b3.pack()
            b4.pack()
            b5.pack()

        elif mainCharacter.checkMajor() == False:
            tkinter.messagebox.showinfo("Advising", "Hi, are you interested in becoming a CS major or minor?")
            tkinter.messagebox.showinfo("Advising", "To become a CS major, you have to fulfill 11 courses inside the major, including three 200 level core courses and one 300 level seminar.")
            tkinter.messagebox.showinfo("Advising", "If you want to minor in CS, there are differnet concentrations which you can find on the minor page. They generally include 111, 212 and one 300 level course.")
        
        elif mainCharacter.checkMajor() == True and mainCharacter.advisor != professor.name:
            tkinter.messagebox.showinfo("Advising", "Hi, Come on in.")
            tkinter.messagebox.showinfo("Advising", "You can ask me about courses and policies, but since I don't know you so I might not be able to give you the best suggestion.")
            box3 = tkinter.Tk()
            b1 = tkinter.Button(box3, text = "Study Away", command = self.studyAway)
            b2 = tkinter.Button(box3, text = "courseTaking", command = self.courseTaking)
            b3 = tkinter.Button(box3, text = "Research", command = self.research)
            b4 = tkinter.Button(box3, text = "Close", command = box3.destroy)
            b1.pack()        
            b2.pack()
            b3.pack()
            b4.pack()
    def studyAway(self):
        tkinter.messagebox.showinfo("Study elsewhere", "There are some programs for CS students. Check them out.")
    def courseTaking(self):
        tkinter.messagebox.showinfo("Requirements", "To graduate, you have to fulfill 11 courses inside the major, including CSC111, MTH111 and 153, three 200 level core courses in theory, programming and system areas and one 300 level seminar.")
        tkinter.messagebox.showinfo("Requirements", "Some courses cannot be counted towards the major after you take some other courses, make sure you check them out before taking them.")
    def research(self):
        tkinter.messagebox.showinfo("Research", "We have a program called SURF, which is a summer research.")
        tkinter.messagebox.showinfo("Research", "Professors also support special studies which take place during semesters. They worth 1 to 4 credits based on different situations.")
    def recommondate(self):
        tkinter.messagebox.showinfo("Recommondation Letter", "Ok, tell me more about you.")


    def chat(self):
        chance = random.randint(0, 8)
        if chance == 0 or chance == 7 or chance == 8:
                if self.name == "joe":
                        tkinter.messagebox.showinfo( "Chat.", "Nice weather today...:-j")       
                else:
                        tkinter.messagebox.showinfo( "Chat.", "Nice weather today...")

        if chance == 1:
                tkinter.messagebox.showinfo( "Chat.", "You should take 212 before looking for intern. 212 is very import.")
        if chance == 2:
                tkinter.messagebox.showinfo( "Chat.", "Do you know that you should ask the department chair if you can transfer credit or not.")
        if chance == 3:
                tkinter.messagebox.showinfo( "Chat.", "Do you know that you can take game courses at Hampshire and Umass.")
                tkinter.messagebox.showinfo( "Chat.", "But you'll probalbly not be able to get in.")        
        if chance == 4:
                tkinter.messagebox.showinfo( "Chat.", "We are trying to hire new professors...")


        if self.name == "joe" and chance == 5:
                tkinter.messagebox.showinfo( "Chat.", "I've got so many advisees this year...")         

        if self.name == "joe" and chance == 6:
                tkinter.messagebox.showinfo( "Chat.", "I'll not be here for the next semester, but we can still talk by email.:-j")

        if self.name == "jordan" and chance == 5:
                tkinter.messagebox.showinfo( "Chat.", "Logan, how do you think of computer science?")
                tkinter.messagebox.showinfo( "Chat.", "Logan: Ahhh...")
                tkinter.messagebox.showinfo( "Chat.", "Ha! That's very thoughtful!") 

        if self.name == "jordan" and chance == 6:
                tkinter.messagebox.showinfo( "Chat.", "Go for Hackathons and Datafests! You can get extra credits for my classes.")

        if self.name == "nick" and chance == 5:
                tkinter.messagebox.showinfo( "Chat.", "...")
                tkinter.messagebox.showinfo( "Chat.", ".........")
                tkinter.messagebox.showinfo( "Chat.", "Emmmmmmm...")
        if self.name == "nick" and chance == 6:
                tkinter.messagebox.showinfo( "Chat.", "(Nick is smiling at you).")


        if self.name == "dominique" and chance == 4:
                tkinter.messagebox.showinfo( "Chat.", "You should ask Dave to help you if you can't find out which banana is the largest.")
        if self.name == "dominique" and chance == 5:
                tkinter.messagebox.showinfo( "Chat.", "You should take some ESS courses.")
        if self.name == "dominique" and chance == 6:
            tkinter.messagebox.showinfo( "Chat.", "We're not sure if we can add more courses for the next semester or not. ")
            tkinter.messagebox.showinfo( "Chat.", "It's like quantum computing, we're kind of between yes and no.")


    # declare your major
    def declare(self, mainCharacter):
        if mainCharacter.checkMajor() == False:
            chance = random.randint(0, 6)
            # You get a 1/6 chance to declare with Joe
            if (chance == 0 and self.name == "joe") or (chance == 1 and self.name == "joe") or (chance == 2 and self.name == "joe") or (chance == 3 and self.name == "joe") or (chance == 4 and self.name == "joe") or (chance == 5 and self.name == "joe"):
                tkinter.messagebox.showinfo("Declare", "Someone has taken the last advisee position! Now Joe has 100 advisees. You have to wait.")
                tkinter.messagebox.showinfo("Declare", "Hopefully you'll be able to declare with Joe before you graduate.")

            else:
                result = tkinter.messagebox.askquestion("Declare", "Are You Sure you want to declare major with this professor?", icon='warning')
                if result =='yes':
                    tkinter.messagebox.showinfo("Declare", "Declared! Welcome to CS major!")
                    mainCharacter.declare(self.name)
                else:
                    tkinter.messagebox.showinfo("Declare", "Take your time.")

        elif mainCharacter.checkMajor() == True and mainCharacter.advisor != professor.name:
            tkinter.messagebox.showinfo("Declare", "You have already declared your major with "+mainCharacter.advisor)
            tkinter.messagebox.showinfo("Declare", "Don't worry, you are always welcomed to talk to me.")

class Computer:
    '''Computer class that contains logic for course selection'''

    all_courses = {
                    111: "Introduction to Computer Science Through Programming",
                    212: "Programming with Data Structures",
                    105: "Interactive Web Documents",
                    220: "Advanced Programming Techniques",
                    240: "Computer Graphics",
                    249: "Computer Networks",
                    250: "Theory of Computation",
                    274: "Discrete & Computational Geometry",
                    370: "Computer Vision and Image Processing",
                    102: "How the Internet Works",
                    103: "How Computers Work",
                    231: "Microprocessors and Assembly",
                    262: "Operating Systems",
                    293: "Machine Learning",
                    105: "Interactive Web Documents",
                    106: "Introduction to Computing and the Arts",
                    252: "Algorithms",
                    270: "Digital Circuits and Systems",
                    274: "Discrete & Computational Geometry",
                    290: "Artificial Intelligence",
                    330: "Database Systems",
                    334: "Topics in Computational Biology",
                    352: "Parallel Programming",
                    360: "Mobile & Locative Computing",
                    370: "Computer Vision and Image Processing",
                    390: "Unsupervised Machine Learning"
                    }
    fixed_courses = {
                    111: "Introduction to Computer Science Through Programming",
                    212: "Programming with Data Structures"
                    }
    spring_courses = {
                      105: "Interactive Web Documents",
                      220: "Advanced Programming Techniques",
                      240: "Computer Graphics",
                      249: "Computer Networks",
                      250: "Theory of Computation",
                      274: "Discrete & Computational Geometry",
                      370: "Computer Vision and Image Processing"
                     }
    fall_courses = {
                    102: "How the Internet Works",
                    103: "How Computers Work",
                    231: "Microprocessors and Assembly",
                    262: "Operating Systems",
                    293: "Machine Learning",
                    }
    expected_courses = {
                        105: "Interactive Web Documents",
                        106: "Introduction to Computing and the Arts",
                        252: "Algorithms",
                        270: "Digital Circuits and Systems",
                        274: "Discrete & Computational Geometry",
                        290: "Artificial Intelligence",
                        330: "Database Systems",
                        334: "Topics in Computational Biology",
                        352: "Parallel Programming",
                        360: "Mobile & Locative Computing",
                        370: "Computer Vision and Image Processing",
                        390: "Unsupervised Machine Learning",
                        }
    course_taken = {}
    coursePracticed={}

    def __init__(self, name, px, py):
        self.image = Image(Point(px,py), "computer1.gif")
        self.imageID = 'black'
        self.positionX = px
        self.positionY = py

    # Activate the computer when walk close to
    def activate(self):
        black = Image( Point(self.positionX,self.positionY), 'computer1.gif')
        white = Image( Point(self.positionX,self.positionY), 'computer2.gif')

        if (self.imageID =='black'):
            self.imageID = 'white'
            self.image = white
            self.image.draw(win)

    # Deactivate computer when leaving
    def deactivate(self):
        black = Image( Point(self.positionX,self.positionY), 'computer1.gif')
        white = Image( Point(self.positionX,self.positionY), 'computer2.gif')

        if(self.imageID == 'white'):
            self.imageID = 'black'
            self.image = black
            self.image.draw(win)

    def chatWith(self, mainCharacter):
        root = tkinter.Tk()
        b1 = tkinter.Button(root, text = "Login", command = self.chat)
        b1.pack()
        b2 = tkinter.Button(root, text="Logout", command=root.destroy)
        b2.pack()

    # Chat with computer in two ways: Check courses info & Register/Check schedule & Practice
    def chat(self):
        root = tkinter.Tk()
        courses = self.course_list('spring')
        def courseInfo():
            self.courseDisplay(semester)
        tkinter.Label(root, text="Hi, I'm a computer. How can I help you?").pack(padx=30, pady=30)
        course = tkinter.Button(root, text="Check courses info & Register", command = courseInfo)
        course.pack()
        schedule = tkinter.Button(root, text="Check schedule & Practice", command = self.displaySchedule)
        schedule.pack()
        information = tkinter.Button(root, text="Personal Information", command = self.inform)
        information.pack() 
    def inform(self):
        #root = tkinter.Tk()
        tkinter.messagebox.showinfo("Information","Semester: "+str(semester)+" ; "+"Year: "+str(year)+" ; "+"GPA: "+str(mainCharacter.GPA))

    # Display course info when selectec
    def courseDisplay(self,semester):
        root = tkinter.Tk()
        course_list = self.course_list(semester)
        for key,value in course_list.items():
            b=tkinter.Button(root, text = str(key)+": "+value, command = lambda key=key: self.infoDisplay(key))
            b.pack()

    # Generated course list for each semester
    def course_list(self, semester):
        course_list = {}
        course_list.update(self.fixed_courses)
        if semester == 'spring':
            course_list.update(random.sample(self.spring_courses.items(), 3))
            course_list.update(random.sample(self.expected_courses.items(), 3))
        else:
            course_list.update(random.sample(self.fall_courses.items(), 3))
            course_list.update(random.sample(self.expected_courses.items(), 3))
        return course_list

    # Get course info from txt file
    def checkCourse(self, key):
        course_info = eval(open("course_info.txt",encoding='utf-8').read())
        return course_info.get(key)

    # Display info given key
    def infoDisplay(self,key):
        root = tkinter.Tk()
        tkinter.Label(root, wraplength=500, text=self.checkCourse(key)).pack(padx=30, pady=30)
        b = tkinter.Button(root, text="Register", command = lambda:self.register(key))
        b.pack()

    # Register/waitlist a class given key
    def register(self,key):
        #chance = random.randint(0,1)
        chance = 0
        if chance == 0 and mainCharacter.courseNum <=4:
            tkinter.messagebox.showinfo("Registered", "Course "+str(key)+" has been added to your schedule. Please go to your schedule and do the practice to pass this semester.")
            self.course_taken.update({key: self.all_courses[key]})
            self.coursePracticed.update({key: self.all_courses[key]})
            mainCharacter.courseNum+=1
        elif mainCharacter.courseNum >4:
            tkinter.messagebox.showinfo("Wait","Think for a while. You have already taken 4 courses for this semester.")
        elif chance!= 0:
            tkinter.messagebox.showinfo("Failed", "The class is full. You are waitlisted.")

        return self.course_taken

    #def doubleCheck(self,key)
        
    # Practice problems
    def practiceDisplay(self, key):
        #update = True
        if key in self.coursePracticed:
            self.coursePracticed.pop(key)
        root = tkinter.Tk()
        questions = eval(open("Questions.txt",encoding='utf-8').read())
        questionText = eval(open(questions.get(key),encoding ='utf-8').read())
        question = questionText.get("q")
        A = questionText.get("A")
        B = questionText.get("B")
        C = questionText.get("C")
        ans = questionText.get("ans")
        tkinter.Label(root, wraplength=500, text=question).pack(padx=30, pady=30)
        R1 = tkinter.Button(root, text=A, command=lambda: self.check(R1,ans,root))
        R1.pack()
        R2 = tkinter.Button(root, text=B,command=lambda: self.check(R2,ans,root))
        R2.pack()
        R3 = tkinter.Button(root, text=C,command=lambda: self.check(R3,ans,root))
        R3.pack()
        if root.winfo_exists !=1 and not self.coursePracticed:
            self.update()
            print("Year: ", year)
            print("Semester:", semester)
    def check(self,button,ans,root):
        if button.cget('text') == ans:
            mainCharacter.GPA = 4.0
            tkinter.messagebox.showinfo("Check", "Correct!")
            root.destroy()
        else:
            mainCharacter.GPA = 2.7
            tkinter.messagebox.showinfo("Check", "Oops!") 
            root.destroy()
    def update(self):
        if semester == "fall":
            mainCharacter.springToFall()
        else:
            mainCharacter.rising()	
            mainCharacter.springToFall()			
    # Display registered classes
    def displaySchedule(self):
        root = tkinter.Tk()
        if bool(self.course_taken) == False:
            tkinter.messagebox.showinfo("Empty", "Your schedule is empty. Register for courses!")
        else:
            for key,value in self.course_taken.items():
                b=tkinter.Button(root, text = str(key)+": "+value, command = lambda key=key: self.practiceDisplay(key))
                b.pack()
            tkinter.messagebox.showinfo("Practice", "Here are courses you have registered. Click on a course to practice.")
#============ Scene Logic  ===================
# Parent class for staicase, door, elevator and etc.
class Objects:
    '''This is a class for all objects that interact with the main character.
    '''
    def __init__(self, px, py, image, name):
        self.image = Image( Point(px, py), image)
        self.positionX = px
        self.positionY = py
        self.name = name

class Npc:
    ''' subclass of objects, has chat function
    '''
    def __init__(self, px, py, image):
        self.image = Image( Point(px, py), image)
        self.positionX = px
        self.positionY = py

    def chat(self):
        if checkDistance(self, mainCharacter.getX(), mainCharacter.getY()):

            chance = random.randint(0, 8)
            if chance == 0:
                tkinter.messagebox.showinfo( "Chat.", "Hey, how are you?")
            if chance == 1:
                tkinter.messagebox.showinfo( "Chat.", "How's your project going?")
            if chance == 2:
                tkinter.messagebox.showinfo( "Chat.", "Do you know that you can check your info pressing i key.")
            if chance == 3:
                tkinter.messagebox.showinfo( "Chat.", "Hey what courses are you going to take next semester?")
            if chance == 4:
                tkinter.messagebox.showinfo( "Chat.", "I'm so worried about finding an intern...")            
            if chance == 5:
                tkinter.messagebox.showinfo( "Chat.", "Where is that bug!!")            
            if chance == 6:
                tkinter.messagebox.showinfo( "Chat.", "...")
                tkinter.messagebox.showinfo( "Chat.", "......")
                tkinter.messagebox.showinfo( "Chat.", "Sorry I'm too busy to talk.")
            if chance == 7:
                tkinter.messagebox.showinfo( "Chat.", "Hey are you in the mentor mentee program?")
                tkinter.messagebox.showinfo( "Chat.", "It's held by Smithies in CS.")
            if chance == 8:
                tkinter.messagebox.showinfo( "Chat.", "You can literally live in Ford, it has two kitchens, a bathroom on the basement, a vending machine...")
                tkinter.messagebox.showinfo( "Chat.", "And a fantastic deckchair in the bathroom")

class Door():
    ''' Subclass of Objects, has openDoor function
    '''
    def __init__(self, px, py, image, name):
        self.image = Image( Point(px, py), image)
        self.positionX = px
        self.positionY = py
        self.name = name

    # When open the door, connect to someone's office or wc.
    def openDoor(self):
        '''Shift into a office and from a office to the floor
        '''
        global scene

        resetScene()
        if self.name == "joeDoor":
            scene = "joeOffice"
            global joe
            joeDoor.image.undraw()
            joe = drawOffice("joe.gif", "joe", self)
            
        elif self.name == "jordanDoor":
            scene = "jordanOffice"
            global jordan
            jordanDoor.image.undraw()
            jordan = drawOffice("jordan.gif", "jordan", self)
            global logan
            logan = Objects(-220, 150, "babysitter.gif", "logan")
            logan.image.draw(win)

        elif self.name == "nickDoor":
            scene = "nickOffice"
            global nick
            nickDoor.image.undraw()
            nick = drawOffice("nick.gif", "nick", self)

        elif self.name == "dominiqueDoor":
            scene = "dominiqueOffice"
            global dominique
            dominiqueDoor.image.undraw()
            dominique = drawOffice("dominique.gif", "dominique", self)

        elif self.name == "ileanaDoor":
            scene = "ileanaOffice"
            global ileana
            ileanaDoor.image.undraw()
            ileana = drawOffice("ileana.gif", "ileana", self)
        
        elif self.name == "judithDoor":
            scene = "judithOffice"
            global judith
            judithDoor.image.undraw()
            judith = drawOffice( "judith.gif", "judith", self )

#============================ Interact ================================
def interact():
    '''Checks if the main character touches the any interactable objects.
    '''
    global scene

    #===================================== Outside ======================================

    if scene == "outside":
        if checkDistance(gateR, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor1l"
            mainCharacter.positionX = -500
            drawScene()

    #===================================== First Floor  ======================================

    elif scene == "floor1l":
        # Check gate
        if checkDistance(gateL, mainCharacter.getX(), mainCharacter.getY()):
            scene = "outside"
            mainCharacter.positionX = 500
            drawScene()
        if checkDistance(gateR, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor1r"
            mainCharacter.positionX = -500
            drawScene()
        # Check doors
        if checkBiggerDistance(unknownDoor4, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo( "Whole College Life Unknown Area", "Offices of CS department are on the 2nd and the 3rd floor.")
        if checkBiggerDistance(unknownDoor3, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo( "Whole College Life Unknown Area", "Offices of CS department are on the 2nd and the 3rd floor.")
        # Check NPC
        for l1 in npc1l:
            if k == "Return":
                l1.chat()

        checkComputer()
        checkElevator()


    elif scene == "floor1r":
        #Check gate
        if checkDistance(gateL, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor1l"
            mainCharacter.positionX = 500
            drawScene()

        # Check doors
        if checkBiggerDistance(unknownDoor5, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo( "Whole College Life Unknown Area", "Offices of CS department are on the 2nd and the 3rd floor.")
        if checkBiggerDistance(unknownDoor4, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo( "Whole College Life Unknown Area", "Offices of CS department are on the 2nd and the 3rd floor.")
        # Check NPC
        for r1 in npc1r:
            if k == "Return":
                r1.chat()
        checkComputer()

        if checkBiggerDistance(staircaseUp,mainCharacter.getX(),mainCharacter.getY()) and k == "Return":
            scene = "floor2r"
            drawScene()
            tkinter.messagebox.showinfo("Floor2", "You're on floor 2 now.")

        elif checkBiggerDistance(staircaseDown,mainCharacter.getX(),mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo("???", "Sadly, the ground floor belongs to the engineering department.")

    #===================================== Second Floor ======================================

    elif scene == "floor2l":
        # Check gate
        if checkDistance(gateR, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor2r"
            mainCharacter.positionX = -500
            drawScene()
        # Check NPC
        for l2 in npc2l:
            if k == "Return":
                l2.chat()

        checkComputer()
        checkElevator()

    elif scene == "floor2r" :

        # Check scene
        if checkDistance(gateL, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor2l"
            mainCharacter.positionX = 500
            drawScene()

        # Check door
        if checkBiggerDistance(joeDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            print("joe")
            joeDoor.openDoor()

        # Check NPC
        for r2 in npc2r:
            if k == "Return":
                r2.chat()

        if checkBiggerDistance(staircaseUp,mainCharacter.getX(),mainCharacter.getY()) and k == "Return":
            scene = "floor3r"
            drawScene()
            tkinter.messagebox.showinfo("Floor3", "You're on floor 3 now.")

        elif checkBiggerDistance(staircaseDown,mainCharacter.getX(),mainCharacter.getY()) and k == "Return":
            scene = "floor1r"
            drawScene()
            tkinter.messagebox.showinfo("Floor1", "You're floor 1 now.")        
        checkComputer()

    #===================================== Third Floor ======================================

    elif scene == "floor3l":
        # Check gate
        if checkDistance(gateR, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor3r"
            mainCharacter.positionX = -500
            drawScene()
        # Check door
        if checkBiggerDistance(ileanaDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            ileanaDoor.openDoor()
        if checkBiggerDistance(judithDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            judithDoor.openDoor()
        # Check NPC
        for l3 in npc3l:
            if k == "Return":
                l3.chat()
        checkComputer()
        checkElevator()

    elif scene == "floor3r" :

        # Check gate
        if checkDistance(gateL, mainCharacter.getX(), mainCharacter.getY()):
            scene = "floor3l"
            mainCharacter.positionX = 500
            drawScene()
        # Check door
        if checkBiggerDistance(jordanDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            jordanDoor.openDoor()
        if checkBiggerDistance(dominiqueDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            dominiqueDoor.openDoor()
        if checkBiggerDistance(nickDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            nickDoor.openDoor()

        if checkBiggerDistance(staircaseUp,mainCharacter.getX(),mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo("???", "Oh dude, you know what, you can't go to the sky.")
        elif checkBiggerDistance(staircaseDown,mainCharacter.getX(),mainCharacter.getY())and k == "Return":
            scene = "floor2r"
            drawScene()
            tkinter.messagebox.showinfo("Floor2", "Dude you're floor 2 now.")
    #===================================== Offices ======================================
    
    elif scene == "joeOffice":
        # Chat
        if checkBiggerDistance(professor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            professor.chatWith(mainCharacter)
        # Get out of the office
        if checkBiggerDistance(joeDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            scene = "floor2r"
            drawScene()

    elif scene == "jordanOffice":
        if checkBiggerDistance(jordanDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            scene = "floor3r"
            drawScene()
        if checkBiggerDistance(professor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            professor.chatWith(mainCharacter)

        if checkDistance(logan, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            tkinter.messagebox.showinfo("Logan" , "Ahhh!")
            
    elif scene == "dominiqueOffice":
        if checkBiggerDistance(professor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            professor.chatWith(mainCharacter)

        if checkBiggerDistance(dominiqueDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            scene = "floor3r"
            drawScene()     

    elif scene == "nickOffice":   
        if checkBiggerDistance(professor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            professor.chatWith(mainCharacter) 
        if checkBiggerDistance(nickDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return": 
            scene = "floor3r"
            drawScene() 

    elif scene == "ileanaOffice":
        if checkBiggerDistance(professor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            professor.chatWith(mainCharacter)
        if checkBiggerDistance(ileanaDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return": 
            scene = "floor3l"
            drawScene()  

    elif scene == "judithOffice":      
        if checkBiggerDistance(professor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
            professor.chatWith(mainCharacter)
        if checkBiggerDistance(judithDoor, mainCharacter.getX(), mainCharacter.getY()) and k == "Return": 
            scene = "floor3l"
            drawScene()
def checkComputer():
    '''Quick checker for computers, child_window variables are for not letting windows pop up infinite windows.
    '''
    # For windows users
    child_window_prof = True
    child_window_computer = True
    child_window_staircase = True
    
    if checkBiggerDistance(computer, mainCharacter.getX(), mainCharacter.getY()) and child_window_computer and (k == "Return"):
        computer.chatWith(mainCharacter)
        computer.activate()
        child_window_computer = False

    elif not checkBiggerDistance(computer, mainCharacter.getX(), mainCharacter.getY()):
        computer.deactivate()
        child_window_computer = True  
            
def checkElevator():
    '''A quick checker for elevator, asks which floor the player wanna go and shifts the scene.
    '''

    global scene

    def first():
        global scene
        scene = "floor1l"
        drawScene()
    def second():
        global scene
        scene = "floor2l"
        drawScene()
    def third():
        global scene
        scene = "floor3l"
        drawScene()
    if checkBiggerDistance(elevator, mainCharacter.getX(), mainCharacter.getY()) and k == "Return":
        tkinter.messagebox.showinfo("Elevator", "Which floor do you wanna go?")
        box = tkinter.Tk()
        b1 = tkinter.Button(box, text = "First floor", command = first)
        b2 = tkinter.Button(box, text = "Second floor", command = second)
        b3 = tkinter.Button(box, text = "Third floor", command = third)
        b4 = tkinter.Button(box, text = "Close", command = box.destroy)
        b3.pack()        
        b2.pack()
        b1.pack()
        b4.pack()

#============================= Draw functions ====================================

# Draw floors
def drawScene():

    resetScene()
    print("reset")
    print("position in drawScene", mainCharacter.positionX)

    print("draw in drawScene")
    print(mainCharacter.positionX)

    staircaseUp.image.undraw()
    staircaseDown.image.undraw()
    elevator.image.undraw()
    gateL.image.undraw()
    gateR.image.undraw()

    if scene == "outside":

        road1 = Line(Point(-600, -100), Point(600, -100))
        road1.setWidth(5)
        road1.draw(win)
        road2 = Line(Point(-600, 100), Point(600, 100))
        road2.setWidth(5)
        road2.draw(win)
        road3 = Line(Point(-600, -92), Point(600, -90))
        road3.setWidth(2)
        road3.draw(win)
        road4 = Line(Point(-600, 92), Point(600, 90))
        road4.setWidth(2)
        road4.draw(win)
        for i in range(-570, 620, 50):
            drawObject(i, -150, "plant1.gif")
            drawObject(i, 170, "plant1.gif")

    if scene == "floor1r":
        staircaseUp.image.draw(win)
        staircaseDown.image.draw(win)
        gateL.image.draw(win)
        unknownDoor4.image.draw(win)
        unknownDoor5.image.draw(win)
        computer.image.draw(win)
        drawObject(-380, 140, "plant1.gif")
        drawObject(-310, 140, "plant1.gif")
        drawObject(-310, -90, "tablechair2.gif")
        drawObject(-250, 140, "Npc4.gif")
        drawObject(-200, -200, "plant2.gif")
        drawObject(-200, -120, "plant2.gif")
        drawObject(-150, 180, "table.gif")
        drawObject(-120, -200, "Npc1.gif")
        drawObject(-50, -200, "Npc1.gif")
        drawObject(50, 160, "bookcase.gif")
        drawObject(30, -200, "plant2.gif")
        drawObject(30, -120, "plant2.gif")
        drawObject(80, -200, "plant2.gif")
        drawObject(80, -120, "plant2.gif")
        drawObject(130, -200, "plant2.gif")
        drawObject(130, -120, "plant2.gif")
        drawObject(200, 140, "plant2.gif")

    elif scene == "floor2r":
        staircaseUp.image.draw(win)
        staircaseDown.image.draw(win)
        gateL.image.draw(win)
        joeDoor.image.draw(win)
        computer.image.draw(win)
        drawObject(-350, 140, "plant1.gif" )
        drawObject(-300, 140, "plant1.gif" )
        drawObject(-350, 220, "plant2.gif" )
        drawObject(-300, 220, "plant2.gif" )
        drawObject(-150, 180, "tablechair2.gif" )
        drawObject(80, 160, "bookcase.gif")
        drawObject(340, 160, "bookcase.gif")
        drawObject(450, 190, "wc.gif")
        drawObject(350, -150, "trashbin.gif")
        drawObject(-340, -190, "table.gif")
        drawObject(-340, -90, "table.gif")
        drawObject(-240, -140, "Npc2.gif")
        drawObject(-240, -250, "Npc3.gif")        
        drawObject(-180, -140, "Npc3.gif")
        drawObject(-180, -250, "Npc2.gif")
        drawObject(-120, -140, "Npc2.gif")
        drawObject(-120, -250, "Npc3.gif")
        drawObject(-60, -140, "Npc3.gif")
        drawObject(-60, -250, "Npc2.gif")
        drawObject(30, -200, "plant2.gif")
        drawObject(30, -120, "plant2.gif")
        drawObject(80, -200, "plant2.gif")
        drawObject(80, -120, "plant2.gif")
        drawObject(130, -200, "plant2.gif")
        drawObject(130, -120, "plant2.gif")
        drawObject(250, -160, "board.gif")

    elif scene == "floor3r":
        staircaseUp.image.draw(win)
        staircaseDown.image.draw(win)
        gateL.image.draw(win)
        jordanDoor.positionX, jordanDoor.positionY= 400, 190
        jordanDoor.image.draw(win)
        dominiqueDoor.positionX, dominiqueDoor.positionY= -200, 190
        dominiqueDoor.image.draw(win)
        nickDoor.positionX, nickDoor.positionY= 0, 190
        nickDoor.image.draw(win)

    elif scene == "floor1l":
        elevator.image.draw(win)
        gateL.image.draw(win)
        gateR.image.draw(win)
        drawObject(-450, 140, "Npc2.gif")
        drawObject(-380, 140, "Npc3.gif")
        drawObject(-310, 140, "Npc2.gif")
        drawObject(-220, 140, "plant2.gif")
        drawObject(-220, 220, "plant2.gif")
        drawObject(-150, 180, "table.gif")
        unknownDoor3.image.draw(win)
        drawObject(200, 140, "plant2.gif")
        unknownDoor4.image.draw(win)
        drawObject(-440, -180, "tablechair2.gif")
        drawObject(-310, -180, "tablechair2.gif")
        drawObject(-440, -90, "tablechair2.gif")
        drawObject(-310, -90, "tablechair2.gif")
        drawObject(-200, -200, "plant2.gif")
        drawObject(-200, -120, "plant2.gif")
        drawObject(-120, -150, "Npc1.gif")
        drawObject(-50, -150, "Npc1.gif")
        drawObject(30, -210, "plant2.gif")
        drawObject(30, -130, "plant2.gif")
        drawObject(80, -210, "plant2.gif")
        drawObject(80, -130, "plant2.gif")
        drawObject(130, -210, "plant2.gif")
        drawObject(130, -130, "plant2.gif")
        computer.image.draw(win)


    elif scene == "floor2l":
        elevator.image.draw(win)
        gateR.image.draw(win)
        drawObject(-450, 140, "plant1.gif")
        drawObject(-380, 140, "plant1.gif")
        drawObject(-310, 140, "plant1.gif")
        drawObject(-230, 140, "Npc4.gif")
        drawObject(-150, 180, "plant1.gif")
        drawObject(200, 140, "plant2.gif")
        drawObject(-440, -90, "tablechair2.gif")
        drawObject(-310, -90, "tablechair2.gif")
        drawObject(-200, -200, "plant2.gif")
        drawObject(-200, -120, "plant2.gif")
        drawObject(-120, -210, "Npc1.gif")
        drawObject(-50, -210, "Npc1.gif")
        drawObject(30, -200, "plant2.gif")
        drawObject(30, -120, "plant2.gif")
        drawObject(80, -200, "plant2.gif")
        drawObject(80, -120, "plant2.gif")
        drawObject(130, -200, "plant2.gif")
        drawObject(130, -120, "plant2.gif")
        computer.image.draw(win)


    elif scene == "floor3l":
        elevator.image.draw(win)
        gateR.image.draw(win)
        computer.image.draw(win)
        drawObject(-450, 140, "Npc2.gif")
        drawObject(-380, 140, "Npc2.gif") 
        drawObject(-310, 140, "Npc2.gif")
        drawObject(-240, 140, "Npc4.gif")
        drawObject(-150, 180, "plant2.gif")
        drawObject(200, 140, "plant2.gif")
        drawObject(-440, -150, "bookcase.gif")
        drawObject(-310, -150, "bookcase.gif")
        drawObject(-200, -200, "Npc1.gif")      
        drawObject(-120, -210, "plant2.gif")
        drawObject(-50, -210, "plant2.gif")
        drawObject(-120, -130, "plant2.gif")
        drawObject(-50, -130, "plant2.gif")  
        drawObject(30, -200, "chair.gif")
        drawObject(80, -200, "chair.gif")
        drawObject(130, -200, "chair.gif")
        ileanaDoor.image.draw(win)
        judithDoor.image.draw(win)

    mainCharacter.image.draw(win)

# Draw Offices
def drawOffice(image, name, door):
    '''Draw the office of a given character
    '''
    resetScene()
    door.positionX = 200
    drawObject(200, 190, "door.gif")
    mainCharacter.positionX= 150
    mainCharacter.image.draw(win)
    print("draw in drawOffice")
    global professor
    professor = Professor(name, -150, 160, image)
    professor.image.draw(win)
    drawObject(0, 190, "tablechair.gif")
    return professor

# Quick draw objects
def drawObject(px, py, imageID):
    positionX = px
    positionY = py
    image = Image( Point(px, py), imageID )
    image.draw(win)

# Cover the current scene and undraw objects
def resetScene():
    mainCharacter.image.undraw()
    computer.image.undraw() 
    unknownDoor1.image.undraw()
    unknownDoor2.image.undraw()
    unknownDoor3.image.undraw()
    unknownDoor4.image.undraw()
    unknownDoor5.image.undraw()
    joeDoor.image.undraw()
    jordanDoor.image.undraw()
    dominiqueDoor.image.undraw()
    nickDoor.image.undraw()
    ileanaDoor.image.undraw()
    judithDoor.image.undraw()
    reset = Rectangle(Point(-610, -310), Point(610, 310))
    reset.setFill("white")
    reset.draw(win)
#============================= Check distance =========================================

# Checks the distance of an object and the main character
def checkDistance (self, mainCharacterX, mainCharacterY):
    if (-30 < (mainCharacterX - self.positionX ) < 30) and (-100 < (mainCharacterY - self.positionY ) < 100):
        return True
    else: return False


def checkBiggerDistance (self, mainCharacterX, mainCharacterY):
    ClosetoChat = False
    if (-40 < (mainCharacterX - self.positionX ) < 40) and (-150 < (mainCharacterY - self.positionY ) < 200):
       return True
    return False

#============================= Other functions=========================================

# Constructs objects needed.
def oneClickObjects():
    global semester
    semester = 'spring'
    global year
    year = 2018

    global mainCharacter

    global permission
    permission = True

    global computer
    computer = Computer('computer', -40, 180)

    global mainCharacter
    mainCharacter = Character( 300, 0 )
    mainCharacter.image.draw(win)

    #================================= Gates, elevator, staircases ======================
    global gateL
    global gateR 
    gateL = Objects(-550, 0, "gate.gif", "gateL")
    gateR = Objects(550, 0, "gate.gif", "gateR")
    gateR.image.draw(win)
    #elevator
    global elevator
    elevator = Objects(280, -190, "elevator1.gif", "elevator")
    #staircase
    global staircaseUp
    global staircaseDown
    staircaseUp = Objects(-440, 150, "staircase.gif", "staircase")
    staircaseDown = Objects(-440, -140, "staircase.gif", "staircase")
    
    #================================== Doors ===============================
    global joeDoor
    global jordanDoor
    global dominiqueDoor
    global nickDoor
    global judithDoor
    global ileanaDoor
    global unknownDoor1
    global unknownDoor2
    global unknownDoor3
    global unknownDoor4
    global unknownDoor5
    joeDoor = Door(200, 190, "door.gif", "joeDoor")
    jordanDoor = Door(400, 190, "door.gif", "jordanDoor")
    dominiqueDoor = Door(-200, 190, "door.gif", "dominiqueDoor")
    nickDoor = Door(0, 190, "door.gif", "nickDoor")
    ileanaDoor = Door(100, 190, "door.gif", "ileanaDoor")
    judithDoor = Door(400, 190, "door.gif", "judithDoor")
    unknownDoor1 = Door(-300, 190, "door.gif", "unknownDoor")
    unknownDoor2 = Door(-100, 190, "door.gif", "unknwonDoor")
    unknownDoor3 = Door(100, 190, "door.gif", "unknownDoor")
    unknownDoor4 = Door(300, 190, "door.gif", "unknownDoor")
    unknownDoor5 = Door(500, 190, "door.gif", "unknownDoor")

    #============================== NPCs =================================
    global Npc4_1r
    global Npc1a_1r
    global Npc1b_1r
    global Npc2_2r
    global Npc3_2r
    global Npc2b_2r
    global Npc3b_2r
    global Npc2_3l
    global Npc2b_3l
    global Npc2c_3l
    global Npc4_3l
    global Npc1_2l
    global Npc2_1l
    global Npc3_1l
    global Npc2b_1l
    global Npc1_1l
    global Npc2b_1l
    Npc2_1l = Npc(-450, 140, "Npc2.gif")
    Npc3_1l = Npc(-380, 140, "Npc3.gif")
    Npc2b_1l = Npc(-310, 140, "Npc2.gif")
    Npc1_1l = Npc(-120, -150, "Npc1.gif")
    Npc2b_1l = Npc(-50, -150, "Npc1.gif")    
    Npc4_2l = Npc(-230, 140, "Npc4.gif")
    Npc2_3l = Npc(-450, 140, "Npc2.gif")
    Npc2b_3l = Npc(-380, 140, "Npc2.gif")
    Npc2c_3l = Npc(-310, 140, "Npc2.gif")
    Npc4_3l = Npc(-240, 140, "Npc4.gif")
    Npc4_1r = Npc(-250, 140, "Npc4.gif")
    Npc1a_1r = Npc(-120, -200, "Npc1.gif")
    Npc1b_1r = Npc(-50, -200, "Npc1.gif")
    Npc2_2r = Npc(-240, -140, "Npc2.gif")
    Npc3_2r = Npc(-180, -140, "Npc3.gif")
    Npc2b_2r = Npc(-120, -140, "Npc2.gif")
    Npc3b_2r = Npc(-60, -140, "Npc3.gif")
    global npc1r
    global npc2r
    global npc3l
    global npc1l
    global npc2l
    npc1r = [Npc4_1r, Npc1a_1r, Npc1b_1r]
    npc2r = [Npc2_2r, Npc3_2r, Npc2b_2r, Npc3b_2r]
    npc3l = [Npc2_3l, Npc2b_3l, Npc2c_3l, Npc4_3l]
    npc2l = [Npc4_2l]
    npc1l = [Npc2_1l, Npc3_1l, Npc2b_1l, Npc1_1l, Npc2b_1l]

# For people who have broken keyboards 
def setDirectionKeys():

    global upKey
    global leftKey
    global rightKey
    global downKey

    upKey = ''
    leftKey = ''
    rightKey = ''
    downKey = ''

    #Set the keys to the wsad system
    def wsad():
        global upKey
        global leftKey
        global rightKey
        global downKey

        upKey = "w"
        downKey = "s"
        leftKey = "a"
        rightKey = "d"

        tkinter.messagebox.showinfo( "Control System Selection.", 'Successfully set to WSAD control system')
        tkinter.messagebox.showinfo( "Control System Selection.", 'Enjoy your CS journey!')

    #Set the keys to the UpDownLeftRight system
    def udlr():
        global upKey
        global leftKey
        global rightKey
        global downKey

        upKey = "Up"
        downKey = "Down"
        leftKey = "Left"
        rightKey = "Right"

        tkinter.messagebox.showinfo( "Control System Selection.", 'Successfully set to arrow key control system')
        tkinter.messagebox.showinfo( "Control System Selection.", 'Good luck on your CS journey!')

    tkinter.messagebox.showinfo( "Control System Selection.", "Now select your control keys.")
    top = tkinter.Tk()
    b1 = tkinter.Button(top, text = "WSAD", command = wsad)
    b1.pack()
    b2 = tkinter.Button(top, text = "UpDownLeftRight", command= udlr)
    b2.pack()
    b3 = tkinter.Button(top, text="Done", command = top.destroy)
    b3.pack()

# Some messages for the players
def welcome():
    tkinter.messagebox.showinfo( "Welcome!", 'Welcome! Dude!')
    tkinter.messagebox.showinfo( "Welcome!", 'If you want to interact with professor, use the return key.')
    tkinter.messagebox.showinfo( "Welcome!", 'When selection appear, click on "Done" to make up your mind:)')
    tkinter.messagebox.showinfo( "Welcome!", 'You can check your information on computers, or at any time pressing i.')
    tkinter.messagebox.showinfo( "Welcome!", 'If you are feeling terrible, feel free to use the period key!')
    setDirectionKeys()

# Create the window.
def createWindow():
    '''sets up the window.
    '''
    global win
    win = GraphWin( 'Major Pathway', 1400, 400, autoflush = False)
    win.setBackground( 'white' )
    win.setCoords( -600, -300, 600, 300 )


main()
