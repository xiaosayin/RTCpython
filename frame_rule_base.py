from CLCC.frame_info import *


class Frame_delay_Estimator(object):
    def __init__(self):
        self.frame_delay_window = []
        self.threshold = 100  # 100ms
        self.window_size = 6
        self.acc_frame_delay = 0
        self.active_loss = 3
        self.frame_delay_gradient = 0
        self.avg_x = 3.5 # (avg of 1-6)
        self.fenmu = 17.5 #(sum (x - 3.5)^2)
        self.kr = 1

    def calculate_frame_delay_gradient(self):
        if len(self.frame_delay_window) != self.window_size:
            return self.frame_delay_gradient
        avg_frame_delay = sum(self.frame_delay_window)/self.window_size
        fenzi = 0
        for i in range(self.window_size):
            fenzi += (self.frame_delay_window[i] - avg_frame_delay) * (i+1 -3.5)
        self.frame_delay_gradient = fenzi / self.fenmu

    def update_threshold(self):
        self.threshold = self.threshold + self.kr * (self.acc_frame_delay - self.threshold)


    def calculate_acc_frame_delay(self, stat_ele):
        singel_frame_delay = stat_ele[beforeDecTI] - stat_ele[sendTI]
        if singel_frame_delay < 0:
            singel_frame_delay += 1000000
        self.frame_delay_window.append(singel_frame_delay)
        print("singel_frame_delay:", singel_frame_delay)

        if len(self.frame_delay_window) == self.window_size:
            self.acc_frame_delay = 0
            for i in range(len(self.frame_delay_window)):
                self.acc_frame_delay += pow(2, -i-1) * self.frame_delay_window[i]
            print("acc_frame_delay:",self.acc_frame_delay)
            print("frame_delay_window:", self.frame_delay_window)
            self.calculate_frame_delay_gradient()
            print("frame_delay_gradient:", self.frame_delay_gradient)
            self.frame_delay_window.clear()

            if self.acc_frame_delay >= self.threshold:
                if self.active_loss == 1:
                    self.active_loss = 2
                elif self.active_loss == 3:
                    self.active_loss = 1
            else:
                if self.frame_delay_gradient <= 0:
                    if self.active_loss == 2:
                        self.active_loss = 1
                    elif self.active_loss == 1:
                        self.active_loss = 3

            self.update_threshold()
            print("threshold:", self.threshold)


    # def acc_frame_delay(self, single_frame_delay):
    #     return single_frame_delay
