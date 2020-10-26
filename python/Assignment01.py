import maya.cmds as cmds

cmds.polySphere(name='Ball_',
                subdivisionsHeight=20,
                subdivisionsAxis=32)

print (cmds.polySphere('Ball_', q=True, subdivisionsHeight=True))

cmds.polySphere(name='Base_Ball',
                radius=4,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)


cmds.polySphere(name='Second_Ball',
                radius=3,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1
                )
cmds.move( 0, 5, 0) #move 2nd sphere up



cmds.polySphere(name='Third_Ball',
                radius=2,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1
                )
cmds.move( 0, 9, 0) #move third ball up


#TopHat

cmds.polyCylinder( name='Hat',
            radius = 2,
            subdivisionsX = 20,
            subdivisionsY = 20,
            axis = [0, 1, 0],
            createUVs = 2,
            constructionHistory = 1
                )
cmds.scale(1, 3, 1)
cmds.move( 0, 13, 0)
cmds.polyExtrudeFacet( 'Hat.f[0] ', 'Hat.f[0:19]', kft=False, ltz=2, ls=(.5, .5, 0) )

#Eye01
cmds.polySphere(name='Left_Eye',
                radius=1,
                subdivisionsX=10,
                subdivisionsY=10,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1
                )
cmds.scale(.5, .5, .5)
cmds.move( .5, 9, 2)


#Eye02
cmds.polySphere(name='Right_Eye',
                radius=1,
                subdivisionsX=10,
                subdivisionsY=10,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1
                )
cmds.scale(.5, .5, .5)
cmds.move( 2, 9, .5) #RightEyeball






#Nose
cmds.polyCone(name='Nose',
                radius=1,
                subdivisionsX=10,
                subdivisionsY=10,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1
                )
cmds.scale(.5, .5, .5)
cmds.rotate(90, 40, 0)
cmds.move( 1.8, 9, 1.8)