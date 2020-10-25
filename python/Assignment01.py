import maya.cmds as cmds

cmds.polySphere(name='Ball_Geo',
                subdivisionsHeight=20,
                subdivisionsAxis=32)

print (cmds.polySphere('Ball_Geo', q=True, subdivisionsHeight=True))