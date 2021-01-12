from snownlp import SnowNLP
import JavaTimeParser

javaTimeParser = JavaTimeParser.JavaTimeParser("./lib/TimeParser.jar")


class ScheduleNode(object):
    dateTime = ""
    content = ""


def parseText(sentence: str):
    sentencesList = SnowNLP(sentence).sentences
    scheduleList = []

    for sentence in sentencesList:
        scheduleNode = ScheduleNode()
        scheduleNode.dateTime = javaTimeParser.getTimeFromText(sentence)
        scheduleNode.content = sentence
        scheduleList.append(scheduleNode.__dict__)

    return scheduleList
