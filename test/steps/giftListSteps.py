import sys
sys.path.append("..")
from actor import Actor
from abilities.defaultAbilities import runRPATask
from tasks.defaultTasks import run
from tasks.defaultTasks import executeThe
from tasks.defaultTasks import finishTheExecution
from questions.giftListRobotQuestions import amazonInformation
from questions.giftListRobotQuestions import ebayInformation
from utils.fileUtils import deleteFiles

Robot=None

@given(u'Robot runs {task} for {File} in {RPATool}')
def step_impl(context,task,RPATool,File):
    global Robot
    Robot=Actor(named='BotMarley')
    Robot.can(runRPATask)
    Robot.wasAbleTo(
        run(The=task,withArgs={'csvFileToRead':File})
    )

@when(u'Robot do the {current} process')
def step_impl(context,current):

    Robot.attemptsTo(
        executeThe,Process=current
    )

@then(u'All the process should be in {one} state')
def step_impl(context,one):
    
    Robot.should(
        finishTheExecution,inState=one
        )

@then(u'Robot should put the Amazon information in the CSV Files')
def step_impl(context):
    Robot.shouldSee(
        amazonInformation
    )

@then(u'Robot should put the Ebay information in the CSV Files')
def step_impl(context):
    Robot.shouldSee(
        ebayInformation
    )
    pass


