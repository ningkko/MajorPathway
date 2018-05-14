# MajorPathway
Educational game; CSC 220 Final Project - Spring 2018 @Smith

## Introduction
Students, especially first years, often feel overwhelmed by the rich and rigorous course offerings and major requirements when they transition to college - They are expected to find all related information at the department website on their own.\
Although the website is a good resource, some further explanations are necessary to provide students with a big picture of their education. \
With the goal of informing students in an interactive way, we want to build a browser “role playing game” to help students better understand the paths towards Computer Science majors and minors at Smith. \
Ideally, it informs the players about the course offerings of CS department and the tracks they may go through. After playing this game, students would have a basic idea about what a CS major student’s education looks like.

## How to run:
#### Notice: Python 3.6.5 required.
Download the zip file and unzip it to a directory.\
Run MajorPathway.py
#### Note: 
We have a Question.text where questions of different courses are assigned, and its example question reference text Q1.text. \
To add more questions, add question texts in the same format as Q1.text. \
Then return to Question.txt and add the name of the question text (e.g."Q1.txt") in the same format as Q1.txt is added.

## Current problems:
Graduation logic not complished.\
Character drifts when changing scenes.

## Change Log:
From latest to earliest
### Version 4.0
Fix the bugs that will keep going up to the top when use the staircaseUp\
Expand the interactions with non-player characters, for example, professors.\
Implement the semester and GPA system (though not perfect)\
Implement the Graduation logic (the ending)\
Have practice problem
### Version 3.0
Main character can enter professor's offices!\
Fix bugs so that main character can interact with professors in their offices
### Version 2.2
Fix some bugs that occur when the main character moves between scences\
Implement the Computer class: can display interactions with the computer\
Can register for classes, check class info, and see practice questions (not included) using the computer
### Version 2.1
Create more images for professors\
Make changes to the interactions with stairs: two stairs, no messageboxes\
Implement the Door class and the Staircase class as a sub-class of Objects\
Add some welcome words for players
### Version 2.0
Implement setKeyboard function: Can choose between WSAD control and arrow key control systems!\
Create messageboxes for interactions with stairs: can select between going upstairs or downstairs\
Create scene images for second floor
### Version 1.2
Create the first scene of the game\
Implement the Objects class for scene changes and interactive objects\
Implement some scene changes, but not completely successful (cannot go upstairs and downstairs)\
Minor changes in courseinfo.txt and the check course session
### Version 1.1
Create more images for scenes (e.g. chairs, tables, plants, etc.)\
More interactions with professors: Declaring your major!\
Implement the Computer Class (and delete the Course class)\
Can display course info in messageboxes
### Version 1.0
Implement the Professor class\
Create chatting windows using the tkinter package\
Include some interactions with the professor
### Version 0.2
Create more images for non-player characters\
Create two txt files storing information collected from Smith website\
Implement the Course class: can print course info and prerequisites
### Version 0.1
Include SwitchIMG method: the main character is walking rather than "gliding"\
### Version 0.0
Create images for the main character\
Implement the Character Class\
Can control the movement of main character using arrow keys

## Contributors:
Fanghui He, Yining Hua, Qiaqia Ji, Yanwan Zhu
