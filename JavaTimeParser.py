import jpype

class JavaTimeParser:
    timeParser = None

    def __init__(self, libPath:str):
        jvmPath = jpype.getDefaultJVMPath();
        ext_classpath = libPath
        jvmArg = '-Djava.class.path=' + ext_classpath
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, jvmArg)
            TimeParser = jpype.JClass("com.timeparser.TimeParser")
            self.timeParser = TimeParser()

    def __del__(self):
        if jpype.isJVMStarted():
            jpype.shutdownJVM()

    def getTimeFromText(self, sentence:str):
        strs = self.timeParser.getTimeArray(sentence)
        res = []
        for item in strs:
            res.append(str(item))
        return res;
