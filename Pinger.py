from os import popen
from re import findall, MULTILINE

class Pinger:
    def getPingResult(self):
        p = popen('ping www.baidu.com')
        return p.read().replace("\n",'')

    def getAveragePing(self, PingResult):
        result = findall(r"= [0-9]*ms", PingResult, MULTILINE)[-1]
        result = result.replace('= ','').replace('ms','')
        return int(result)

    def getLostRate(self, PingResult):
        result = findall(r"\([0-9]*%", PingResult, MULTILINE)[-1]
        result = result.replace('(','').replace('%','')
        return int(result)

    def isConnectionUnstable(self):
        try:
            PingResult = self.getPingResult()
            if self.getLostRate(PingResult) > 30:
                return True
            elif self.getAveragePing(PingResult) > 200:
                return True
            else:
                return False
        except:
            return True
