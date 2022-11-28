class Computer():
    
    def __init__(self, cpu, gpu, ram):
        print("computer builded")
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        
    def updateRam(self, num):
        self.ram += num
    
    def updateGpu(self, num):
        self.gpu += num
        
    def __str__(self):
        return """
                PC Specs
                CPU : {}
                GPU : {}
                Ram : {}
    """.format(self.cpu, self.gpu, self.ram)
    
c1 = Computer(12, 8, 32)
c1.updateRam(32)
print(c1)