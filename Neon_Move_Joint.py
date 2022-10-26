import maya.cmds as mc
if mc.window("dumWin0",exists = True):
    mc.deleteUI("dumWin0")
    
def buttonMethod(args):
    for skin in cmds.ls(type='skinCluster'):
     cmds.skinCluster(skin, edit=True, moveJointsMode=True)
    
def buttonMethod01(args):
    for skin in cmds.ls(type='skinCluster'):
     cmds.skinCluster(skin, edit=True, moveJointsMode=False)

myWindow = mc.window("dumWin0",t="Neon Maya Script Ver0.1",w =200, h=200)
mc.columnLayout(adj = True)
mc.text(label="click the enter button to enter move joint mode or click the exit button to exit move joint mode")
mc.button(label="Enter Move Joint",command = buttonMethod)
mc.button(label="Exit Move Joint",command = buttonMethod01)
mc.showWindow(myWindow)