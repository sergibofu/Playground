class Logger():
    __nextID = 1

    def __init__(self, fileName):
        self.fileName = fileName
        self.id = self.__nextID
        self.nextLogID()

    def writeLog(self, level, msg):
        with open(self.fileName, mode='a', encoding='utf-8') as log_file:   
            log_file.write('[{0}] {1}\n'.format(level, msg))   

    
    @classmethod
    def nextLogID(cls):
        cls.__nextID += 1


