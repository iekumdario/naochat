import behavior.naochat.aiml as aiml
k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("LOAD AIML B")
k.saveBrain("behavior/naochat/standard.brn")