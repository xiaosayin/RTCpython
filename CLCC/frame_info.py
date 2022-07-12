timestamp_template = ["frame_id", "psnr", "frameSize","width", "height", "is_KeyFrame","gotT", "beforeEncT",
                      "sendT", "complete_frameT","beforeDecT", "afterDecT", "beforeRenderT",
                      "RenQueueReceived", "afterRenderT"]
NumI = timestamp_template.index("frame_id")
psnrI = timestamp_template.index("psnr")
sizeI = timestamp_template.index("frameSize")
widthI = timestamp_template.index("width")
heightI = timestamp_template.index("height")
gotTI = timestamp_template.index("gotT")
beforeEncTI = timestamp_template.index("beforeEncT")
is_KeyFrameI = timestamp_template.index("is_KeyFrame")
sendTI = timestamp_template.index("sendT")
complete_frameI = timestamp_template.index("complete_frameT")
beforeDecTI = timestamp_template.index("beforeDecT")
afterDecTI = timestamp_template.index("afterDecT")
beforeRenderTI = timestamp_template.index("beforeRenderT")
RenQueueReceivedI = timestamp_template.index("RenQueueReceived")
afterRenderTI = timestamp_template.index("afterRenderT")

timelistL = len(timestamp_template) + 1

# class FrameInfo:
#     def __init__(self):
#         self.frame_id = None  # uint16_t
#         self.timestamp_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         self.enc_width = 0
#         self.enc_height = 0
#         self.enc_psnr = 0.0
#
#     def calculate_frame_delay(self):
#         return self.timestamp_list[afterRenderTI] - self.timestamp_list[gotTI]
#
#     def set_psnr(self, psnr):
#         self.enc_psnr = psnr
