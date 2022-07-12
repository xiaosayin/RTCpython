logSwitch = True

frameTemplate = ["frameNum", "frameSize", "PSNR", "width", "rtpTimeStamp", "gotT", "beforeEncT", "is_KeyFrame", \
            "afterEncT", "sendT", "recvT1", "recvT2", \
            "beforeDecT", "afterDecT", "beforeRenderT",\
            "RenQueueRecved", "afterRenderT", "ifDropped"]
tmp = ["frameNum", "frameSize", "PSNR", "width", "rtpTimeStamp", ["gotT", "beforeEncT", "is_KeyFrame", \
            "afterEncT", "sendT", "recvT1", "recvT2", \
            "beforeDecT", "afterDecT", "beforeRenderT",\
            "RenQueueRecved", "afterRenderT"], "ifDropped"]
NumI = frameTemplate.index("frameNum")
SizeI = frameTemplate.index("frameSize")
PSNRI = frameTemplate.index("PSNR")
RtpI = frameTemplate.index("rtpTimeStamp")
widthI = frameTemplate.index("width")
gotI = frameTemplate.index("gotT")
beforeI = frameTemplate.index("beforeEncT")
isKeyI = frameTemplate.index("is_KeyFrame")
afterEncI = frameTemplate.index("afterEncT")
sendI = frameTemplate.index("sendT")
recv1I = frameTemplate.index("recvT1")
recv2I = frameTemplate.index("recvT2")
beforeDecI = frameTemplate.index("beforeDecT")
afterDecI = frameTemplate.index("afterDecT")
beforeRenderI = frameTemplate.index("beforeRenderT")
RenQueueRecvedI = frameTemplate.index("RenQueueRecved")
afterRenderI = frameTemplate.index("afterRenderT")
DroppedI = frameTemplate.index("ifDropped")

tmpDroppedI = tmp.index("ifDropped")

decTemplate = ["frameSize", "rtpTimeStamp", ["gotT", "beforeEncT", "is_KeyFrame", \
            "afterEncT", "sendT", "recvT1", "recvT2", \
            "beforeDecT", "afterDecT", "beforeRenderT",\
            "RenQueueRecved", "afterRenderT"], "ifDropped"]
dSizeI = decTemplate.index("frameSize")
dRtpI = decTemplate.index("rtpTimeStamp")
dDroppedI = decTemplate.index("ifDropped")

cTemplate = ["frameSize", "rtpTimeStamp", "in1", "in2"]
cSizeI = cTemplate.index("frameSize")
cRtpI = cTemplate.index("rtpTimeStamp")
cIn1I = cTemplate.index("in1")
cIn2I = cTemplate.index("in2")
frameL = len(frameTemplate) + 1