from roboarm import Arm
import urllib.request as urllib2
import json
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": False,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":False,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":False

       }
}

req = urllib2.Request('https://prototype.iotnxt.io/api/v3/data/post')
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', 'Basic YXBpOmtleS13cjRjaXVhMW11Z2FvbnZsbWwza2Vlc3ZiOHdoM3RmeA==')

response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": True,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":False,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":False

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
arm = Arm()
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": True,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":False,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":True

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))arm.elbow.up(timeout=2)
arm.grips.close(timeout=1.5)
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": True,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":True,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":False

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
arm.shoulder.up(timeout=2)
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": True,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":False,
       "SholderDown":True,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":False

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
arm.shoulder.down(timeout=1.7)
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": True,
       "ElbowUp":False,
       "ElbowDown":True,
       "SholderUp":False,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":False

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
arm.elbow.down(timeout=1.7)
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": True,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":False,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":True,
       "GripClose":False

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
arm.grips.open(timeout=1.5)
data = {"id": "OWIRobotArm","data": {
       "MovementDetected": False,
       "ElbowUp":False,
       "ElbowDown":False,
       "SholderUp":False,
       "SholderDown":False,
       "WristUp":False,
       "WristDown":False,
       "GripOpen":False,
       "GripClose":False

       }
}
response = urllib2.urlopen(req,json.dumps(data).encode("utf-8"))
