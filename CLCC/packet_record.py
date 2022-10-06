#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class PacketRecord:
    # feature_interval can be modified
    def __init__(self, base_delay_ms=200):          #change to 200 KOYONYONG
        self.base_delay_ms = base_delay_ms
        self.last_delay = None
        self.reset()

    def reset(self):
        self.packet_num = 0
        self.packet_list = []
        self.packet_list122 = []  # ms
        self.packet_list125 = []
        self.last_seqNo = {}
        self.timer_delta = None  # ms
        self.timer_delta_Recv = None  # ms
        self.timer_delta_Send = None  # ms
        self.min_seen_delay = self.base_delay_ms  # ms
        self.last_delay = None
        # ms, record the rtime of the last packet in last interval,
        self.last_interval_rtime = None
        '''
        self.sequence_122_Base = 0
        self.sequence_122_65535Flag = False
        self.sequence_122_Cnt = None

        self.sequence_125_Base = 0
        self.sequence_125_65535Flag = False
        self.sequence_125_Cnt = None
        '''
        self.sequence_state_122 = False
        self.sequence_state_cnt_122 = 0
        self.sequence_base_cnt_122 = None
        self.sequence_base_122 = 0

        self.sequence_state_125 = False
        self.sequence_state_cnt_125 = 0
        self.sequence_base_cnt_125 = None
        self.sequence_base_125 = 0


    def clear(self):
        self.packet_num = 0
        if self.packet_list:
            self.last_interval_rtime = self.packet_list[-1]['timestamp']
        if self.packet_list122:
            self.last_interval_rtime = self.packet_list122[-1]['timestamp']
        if self.packet_list125:
            self.last_interval_rtime = self.packet_list125[-1]['timestamp']
        self.packet_list = []
        self.packet_list122 = []
        self.packet_list125 = []

    def turnToPositive(self, m):
        cnt = 1
        while m + 10 ** cnt < 0:
            cnt += 1
        return m + 10 ** cnt

    def on_receive(self, packet_info, firstPkt):
        print("packetSeq: " , packet_info.sequence_number, flush=True)
        print("len(self.packet_list):", len(self.packet_list), flush= True)
        print("packets receive_timestamp: " , packet_info.receive_timestamp, flush=True)
        if len(self.packet_list)  > 0:
            print("self.packet_list[-1]['timestamp']: ", self.packet_list[-1]['timestamp'], flush=True)
        if not firstPkt:
            assert (len(self.packet_list) == 0
                    or packet_info.receive_timestamp
                    >= self.packet_list[-1]['timestamp']), \
                "The incoming packets receive_timestamp disordered"

        ##what about disordered???
        # Calculate the loss count
        loss_count = 0
        if packet_info.ssrc in self.last_seqNo:
            loss_count = max(0,
                packet_info.sequence_number - self.last_seqNo[packet_info.ssrc] - 1)
        self.last_seqNo[packet_info.ssrc] = packet_info.sequence_number

        # Calculate packet delay
        if self.timer_delta is None:
             # shift delay of the first packet to base delay
            self.timer_delta = self.base_delay_ms - (packet_info.receive_timestamp - packet_info.send_timestamp)
            self.timer_delta_Send = packet_info.send_timestamp
            self.timer_delta_Recv = packet_info.receive_timestamp
        print("this delay = :", self.timer_delta, packet_info.receive_timestamp, packet_info.send_timestamp)
        delay = self.timer_delta + packet_info.receive_timestamp - packet_info.send_timestamp
        if packet_info.receive_timestamp - self.timer_delta_Recv >= 0:
            if packet_info.send_timestamp - self.timer_delta_Send >= 0:
                delay = self.base_delay_ms + (packet_info.receive_timestamp - self.timer_delta_Recv)\
                     - (packet_info.send_timestamp - self.timer_delta_Send)
            else:
                print("delay!: send: ", packet_info.send_timestamp, self.timer_delta_Send)
                delay = self.base_delay_ms + (packet_info.receive_timestamp - self.timer_delta_Recv)\
                     - self.turnToPositive(packet_info.send_timestamp - self.timer_delta_Send)
                    
        else:
            print("delay!: recv: ", packet_info.receive_timestamp, self.timer_delta_Recv)
            if packet_info.send_timestamp - self.timer_delta_Send >= 0:
                delay = self.base_delay_ms + self.turnToPositive(packet_info.receive_timestamp - self.timer_delta_Recv)\
                     - (packet_info.send_timestamp - self.timer_delta_Send)
            else:
                print("delay!: send: ", packet_info.send_timestamp, self.timer_delta_Send)
                delay = self.base_delay_ms + self.turnToPositive(packet_info.receive_timestamp - self.timer_delta_Recv)\
                     - self.turnToPositive(packet_info.send_timestamp - self.timer_delta_Send)
        print("this delay: ", delay)
        self.min_seen_delay = min(delay, self.min_seen_delay)


        # Check the last interval rtime
        if self.last_interval_rtime is None:
            self.last_interval_rtime = packet_info.receive_timestamp
        else:
            if packet_info.receive_timestamp < self.last_interval_rtime:
                self.last_interval_rtime = packet_info.receive_timestamp
        '''
        if packet_info.payload_type == 122:
            if packet_info.sequence_number > 65500 and (self.sequence_122_Cnt == None or self.sequence_122_Cnt > 30000):
                self.sequence_122_65535Flag = True
            if packet_info.sequence_number < 100 and self.sequence_122_65535Flag:
                self.sequence_122_Base += 65536
                self.sequence_122_65535Flag = False
                self.sequence_122_Cnt = 0
            if self.sequence_122_Cnt != None:
                self.sequence_122_Cnt += 1
            print(f"122sequence and sequence_Base: {packet_info.sequence_number}, {self.sequence_122_Base}")
        
        if packet_info.payload_type == 125:
            if packet_info.sequence_number > 65500 and (self.sequence_125_Cnt == None or self.sequence_125_Cnt > 30000):
                self.sequence_125_65535Flag = True
            if packet_info.sequence_number < 100 and self.sequence_125_65535Flag:
                self.sequence_125_Base += 65536
                self.sequence_125_65535Flag = False
                self.sequence_125_Cnt = 0
            if self.sequence_125_Cnt != None:
                self.sequence_125_Cnt += 1
            print(f"125sequence and sequence_Base: {packet_info.sequence_number}, {self.sequence_125_Base}")
        '''
        tmpBase = 0
        sequenceThreshHold = 64000
        cntThreshHold = 10000
        if packet_info.payload_type == 122:
            if self.sequence_state_cnt_122 != None and self.sequence_state_cnt_122 >= cntThreshHold:
                self.sequence_state_122 = False
                self.sequence_state_cnt_122 = 0
                self.sequence_base_122 += 65536
                print("Out of 122State!")
            if self.sequence_state_122 or packet_info.sequence_number >= sequenceThreshHold:    #enter sequence edge state
                self.sequence_state_122 = True
                if self.sequence_state_cnt_122 == None:
                    self.sequence_state_cnt_122 = 0
                if packet_info.sequence_number >= sequenceThreshHold:
                    tmpBase = self.sequence_base_122
                else:
                    tmpBase = self.sequence_base_122 + 65536
                self.sequence_state_cnt_122 += 1
            else:
                tmpBase = self.sequence_base_122

        if packet_info.payload_type == 125:
            if self.sequence_state_cnt_125 != None and self.sequence_state_cnt_125 >= cntThreshHold:
                self.sequence_state_125 = False
                self.sequence_state_cnt_125 = 0
                self.sequence_base_125 += 65536
                print("Out of 125State!")
            if self.sequence_state_125 or packet_info.sequence_number >= sequenceThreshHold:    #enter sequence edge state
                self.sequence_state_125 = True
                if self.sequence_state_cnt_125 == None:
                    self.sequence_state_cnt_125 = 0
                if packet_info.sequence_number >= sequenceThreshHold:
                    tmpBase = self.sequence_base_125
                else:
                    tmpBase = self.sequence_base_125 + 65536
                self.sequence_state_cnt_125 += 1
            else:
                tmpBase = self.sequence_base_125
            
        # Record result in current packet
        packet_result = {
            'timestamp': packet_info.receive_timestamp,  # ms
            'delay': delay,  # ms
            'payload_byte': packet_info.payload_size,  # B
            'loss_count': loss_count,  # p
            'bandwidth_prediction': packet_info.bandwidth_prediction,  # bps
            'size': packet_info.size,    #B
            'payload_type': packet_info.payload_type,     #122 or 125
            'sequence_number': packet_info.sequence_number + tmpBase    #sequence number
        }
        self.packet_list.append(packet_result)
        if packet_info.payload_type == 122:
            self.packet_list122.append(packet_result)
        if packet_info.payload_type == 125:
            self.packet_list125.append(packet_result)
        self.packet_num += 1

    def _get_result_list(self, interval, key):
        if self.packet_num == 0:
            return []

        result_list = []
        if interval == 0:
            interval = self.packet_list[-1]['timestamp'] -\
                self.last_interval_rtime
        start_time = self.packet_list[-1]['timestamp'] - interval
        index = self.packet_num - 1
        while index >= 0 and self.packet_list[index]['timestamp'] > start_time:
            result_list.append(self.packet_list[index][key])
            index -= 1
        return result_list

    def calculate_average_delay(self, interval=0):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        delay_list = self._get_result_list(interval=interval, key='delay')
        if delay_list:
            return np.mean(delay_list)
            # return np.mean(delay_list)
        else:
            return 0

    def calculate_delay_gradient(self, interval=0):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        delay_list = self._get_result_list(interval=interval, key='delay')
        last_delay = self.last_delay
        print("last_delay: ", last_delay)
        if delay_list != []:

            self.last_delay = np.mean(delay_list)
        else:
            self.last_delay = 0
        #print("this_delay_list: ", delay_list)
        #if delay_list == []:
        #    print("delay_list is [], nan is coming")
        #for i in delay_list:
        #    print("this_delay_list: ", i)
        print("this_delay: ", self.last_delay)
        if delay_list != []:
            if last_delay == None: #no last delay
                return 0
            else:   #there is last delay
                return np.mean(delay_list) - last_delay

            # return np.mean(delay_list)
        else:
            return 0


    def calculate_total_delay(self):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        delay_list = self._get_result_list(interval=0, key='delay')
        if delay_list:
            return np.mean(delay_list)
            # return np.mean(delay_list)
        else:
            return 0

    def base_calculate_total_delay(self):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        delay_list = self._get_result_list(interval=0, key='delay')
        if delay_list:
            return delay_list, np.mean(delay_list)
            # return np.mean(delay_list)
        else:
            return [], 0

    def calculate_max_min_95_delay(self):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        delay_list = self._get_result_list(interval=0, key='delay')
        delay_max = max(delay_list)
        delay_min = min(delay_list)
        delay_list.sort()
        delay_95th = np.mean(delay_list[0:int(len(delay_list) * 0.95)])
        delay_95th = np.percentile(delay_list, 95)
        return delay_max, delay_min, delay_95th

    def calculate_loss_ratio(self, interval=0):
        '''
        Calulate the loss ratio in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: packet/packet
        '''
        if self.packet_list == []:
            return 0, 0


        
        self.packet_list122 = sorted(self.packet_list122, key = lambda x: x['sequence_number'])
        self.packet_list125 = sorted(self.packet_list125, key = lambda x: x['sequence_number'])
        start_time = self.packet_list[-1]['timestamp'] - interval
        min122N, max122N, min125N, max125N = None, None, None, None

        recv122Num = 0
        index122 = len(self.packet_list122) - 1
        headLoss122 = 0
        recved122 = []
        list122New = False
        while index122 >= 0:
            pkt122 = self.packet_list122[index122]
            recved122.append(pkt122['sequence_number'])
            print("122sequence: ", pkt122['sequence_number'])
            if pkt122['timestamp'] > start_time:
                list122New = True
                recv122Num += 1
                if min122N == None:
                    min122N = pkt122['sequence_number']
                else:
                    min122N = min(min122N, pkt122['sequence_number'])

                if max122N == None:
                    max122N = pkt122['sequence_number']
                else:
                    max122N = max(max122N, pkt122['sequence_number'])
            else:
                if min122N == None:
                    headLoss122 = 0
                else:
                    print(f"min122N: {min122N} - pkt122['sequence_number']: {pkt122['sequence_number']}")
                    headLoss122 = min122N - pkt122['sequence_number'] - 1
                break
            index122 -= 1

        recv125Num = 0
        index125 = len(self.packet_list125) - 1
        headLoss125 = 0
        recved125 = []
        list125New = False
        while index125 >= 0:
            pkt125 = self.packet_list125[index125]
            recved125.append(pkt125['sequence_number'])
            print("125sequence: ", pkt125['sequence_number'])
            if pkt125['timestamp'] > start_time:
                list125New = True
                recv125Num += 1
                if min125N == None:
                    min125N = pkt125['sequence_number']
                else:
                    min125N = min(min125N, pkt125['sequence_number'])

                if max125N == None:
                    max125N = pkt125['sequence_number']
                else:
                    max125N = max(max125N, pkt125['sequence_number'])
            else:
                if min125N == None:
                    headLoss125 = 0
                else:
                    print(f"min125N: {min125N} - pkt125['sequence_number']: {pkt125['sequence_number']}")
                    headLoss125 = min125N - pkt125['sequence_number'] - 1
                break
            index125 -= 1

        if not list122New and len(recved122) == 1:
            recved122.pop()
        recved122.sort()

        print("recved122: ", recved122)
        list122Loss = 0
        listBurst122 = 0
        listHeadLoss122 = 0
        if (len(recved122) <= 1):
            list122Loss = 0
            listHeadLoss122 = 0
            listTotal122 = len(recved122)
        else:
            for i in range(1, len(recved122)):
                listBurst122 = max(listBurst122, recved122[i] - recved122[i - 1] - 1)
                list122Loss += recved122[i] - recved122[i - 1] - 1

            listTotal122 = recved122[-1] - recved122[1] + 1
            if (recved122[0] != recved122[1] - 1):  #exist head_loss
                listHeadLoss122 = recved122[1] - recved122[0] - 1
                listTotal122 = recved122[-1] - recved122[0]


        if not list125New and len(recved125) == 1:
            recved125.pop()
        recved125.sort()
        print("recved125: ", recved125)
        list125Loss = 0
        listBurst125 = 0
        listHeadLoss125 = 0
        if (len(recved125) <= 1):
            list125Loss = 0
            listHeadLoss125 = 0
            listTotal125 = len(recved125)
        else:
            for i in range(1, len(recved125)):
                listBurst125 = max(listBurst125, recved125[i] - recved125[i - 1] - 1)
                list125Loss += recved125[i] - recved125[i - 1] - 1

            listTotal125 = recved125[-1] - recved125[1] + 1
            if (recved125[0] != recved125[1] - 1):
                listHeadLoss125 = recved125[1] - recved125[0] - 1
                listTotal125 = recved125[-1] - recved125[0]

        listBurst122 = 0 if listBurst122 == 1 else listBurst122
        listBurst125 = 0 if listBurst125 == 1 else listBurst125

        print(f"KOYONG List122 loss_num: {list122Loss}, 122head_loss: {listHeadLoss122}, listBurst122: {listBurst122}, totalNum: {listTotal122}")
        print(f"KOYONG List125 loss_num: {list125Loss}, 125head_loss: {listHeadLoss125}, listBurst125: {listBurst125}, totalNum: {listTotal125}")
        if (listTotal122 + listTotal125 == 0):
            listTotalNum = 0
            listTotalLoss = 0
            listTotalBurst = 0
        else:
            listTotalNum = listTotal122 + listTotal125
            listTotalLoss = list125Loss + list122Loss
            listTotalBurst = listBurst122 + listBurst125

        if max122N != None:
            print("pkt122Num", [max122N , min122N , recv122Num, headLoss122])
            pkt122Num = max122N - min122N + 1 + headLoss122
            loss122Num = max122N - min122N + 1 - recv122Num + headLoss122
        else:
            pkt122Num = 0
            loss122Num = 0

        if max125N != None:
            print("pkt125Num", [max125N , min125N , recv125Num, headLoss125])
            pkt125Num = max125N - min125N + 1 + headLoss125
            loss125Num = max125N - min125N + 1 - recv125Num + headLoss125
        else:
            pkt125Num = 0
            loss125Num = 0

        totalLoss = loss122Num + loss125Num
        totalNum = pkt122Num + pkt125Num
        print(f"KOYONG 122loss_num: {loss122Num}, 122head_loss: {headLoss122}, totalNum: {pkt122Num}")
        print(f"KOYONG 125loss_num: {loss125Num}, 125head_loss: {headLoss125}, totalNum: {pkt125Num}")
        #if (listTotalLoss / listTotalNum if listTotalNum != 0 else 0 != totalLoss / totalNum):
        #    print(f"not same!! listLoss: {listTotalLoss / listTotalNum if listTotalNum != 0 else 0} v.s. loss: {totalLoss / totalNum}")

        '''
        loss_list = self._get_result_list(interval=interval, key='loss_count')
        if loss_list:
            loss_num = np.sum(loss_list)
            received_num = len(loss_list)
            print("loss_list len: ", len(loss_list))
            print(f"R3Net loss_num: {loss_num}, totalNum: {loss_num + received_num}")
        else:
            print("R3Net loss: ",  0)

        if loss_num != totalLoss:
            test_loss_list = self._get_result_list(interval=interval, key='sequence_number')
            print("test_loss_list len: ", len(test_loss_list))
            for i in test_loss_list:
                print("R3net loss != KOYONG loss: ", i)
        '''

        return listTotalLoss / listTotalNum if listTotalNum != 0 else 0, listTotalBurst / listTotalNum if listTotalNum != 0 else 0

    def calculate_total_loss_ratio(self):
        '''
        Calulate the loss ratio in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: packet/packet
        '''
        self.packet_list122 = sorted(self.packet_list122, key = lambda x: x['sequence_number'])
        self.packet_list125 = sorted(self.packet_list125, key = lambda x: x['sequence_number'])
        start_time = 0
        min122N, max122N, min125N, max125N = None, None, None, None

        recv122Num = 0
        for pkt122 in self.packet_list122:
            if pkt122['timestamp'] >= start_time:
                recv122Num += 1
                if min122N == None:
                    min122N = pkt122['sequence_number']
                else:
                    min122N = min(min122N, pkt122['sequence_number'])

                if max122N == None:
                    max122N = pkt122['sequence_number']
                else:
                    max122N = max(max122N, pkt122['sequence_number'])
        print(f"122 max and min: {max122N}, {min122N}")
        recv125Num = 0
        for pkt125 in self.packet_list125:
            if pkt125['timestamp'] >= start_time:
                recv125Num += 1
                if min125N == None:
                    min125N = pkt125['sequence_number']
                else:
                    min125N = min(min125N, pkt125['sequence_number'])

                if max125N == None:
                    max125N = pkt125['sequence_number']
                else:
                    max125N = max(max125N, pkt125['sequence_number'])
        print(f"125 max and min: {max125N}, {min125N}")
        if max122N != None:
            pkt122Num = max122N - min122N + 1
            loss122Num = pkt122Num - recv122Num
            print("pkt122Num: ", pkt122Num)
            print("loss122Num: ", loss122Num)
        else:
            pkt122Num = 0
            loss122Num = 0

        if max125N != None:
            pkt125Num = max125N - min125N + 1
            loss125Num = pkt125Num - recv125Num
            print("pkt125Num: ", pkt125Num)
            print("loss125Num: ", loss125Num)
        else:
            pkt125Num = 0
            loss125Num = 0

        totalLoss = loss122Num + loss125Num
        totalNum = pkt122Num + pkt125Num
        print(f"KOYONG 122loss_num: {loss122Num}, totalNum: {pkt122Num}")
        print(f"KOYONG 125loss_num: {loss125Num}, totalNum: {pkt125Num}")

        loss_list = self._get_result_list(interval=0, key='loss_count')
        if loss_list:
            loss_num = np.sum(loss_list)
            received_num = len(loss_list)
            print(f"R3Net loss_num: {loss_num}, totalNum: {loss_num + received_num}")
        else:
            loss_num  = 0
            print("R3Net loss: ",  0)

        if loss_num != totalLoss:
            send_sorted_packet_list125 = sorted(self.packet_list125, key = lambda x: x['timestamp'])
            for i in send_sorted_packet_list125:
                print("R3net loss != KOYONG loss: ", i['sequence_number'])

            
        if totalNum == 0:
            return 0
        else:
            if (totalLoss / totalNum < 0):
                print(f"The loss is negative!!! totalLoss: {totalLoss}, totalNum: {totalNum}")
            return totalLoss / totalNum

    def calculate_receiving_rate(self, interval=0):
        '''
        Calulate the receiving rate in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: bps
        '''
        received_size_list = self._get_result_list(interval=interval, key='size')
        if received_size_list:
            received_nbytes = np.sum(received_size_list)
            if interval == 0:
                interval = self.packet_list[-1]['timestamp'] -\
                    self.last_interval_rtime
            return received_nbytes * 8 / interval * 1000
        else:
            return 0

    def calculate_total_receiving_rate(self):
        '''
        Calulate the receiving rate in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: bps
        '''
        received_size_list = self._get_result_list(interval=0, key='size')
        if received_size_list:
            received_nbytes = np.sum(received_size_list)
            interval = self.packet_list[-1]['timestamp'] -\
                    self.last_interval_rtime
            return received_nbytes * 8 / interval * 1000
        else:
            return 0

    def calculate_latest_prediction(self):
        '''
        The unit of return value: bps
        '''
        if self.packet_num > 0:
            return self.packet_list[-1]['bandwidth_prediction']
        else:
            return 0

    def getDelayList(self):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        delay_list = self._get_result_list(interval=0, key='delay')
        return delay_list

    def getRecvSizeList(self):
        '''
        Calulate the average delay in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: ms
        '''
        received_size_list = self._get_result_list(interval=0, key='size')
        return received_size_list

    def getLossList(self):
        '''
        Calulate the loss ratio in the last interval time,
        interval=0 means based on the whole packets
        The unit of return value: packet/packet
        '''
        loss_list = self._get_result_list(interval=0, key='loss_count')
        return loss_list