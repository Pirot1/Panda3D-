class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.7,0.7,0.7,0.5)
        self.startNew()
        self.startNew()
    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.setTag("at",str(position))
        self.block.reparentTo(self.land)
    def startNew(self):
        self.land = render.attachNewNode("Land")
    
    def clear(self):
        self.land.removeNode()
        self.startNew()

    def LoadLand(self,filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x,y,z0))
                    x +=1
                y += 1
        return x,y
    def findBlocks(self,pos):
        return self.land.findAllMatches("=at=" + str(pos))
    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    def findHighestEmpty(self,pos):
        x,y,z = pos
        z= 1
        while not self.isEmpty:
            z+= 1
        return (x,y,z)
    def buildBlock(self,pos):
        x,y,z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z +1:
            self.addBlock(new)
    def delBlock(self,position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()
    def delBlockFrom(self,position):
        x,y,z = self.findHighestEmpty(position)
        pos= x,y,z - 1
        for block in self.findBlocks(pos):
            block.removeNode()
