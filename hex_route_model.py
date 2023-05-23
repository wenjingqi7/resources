'''#筛出与开关矩阵有关的信息
with open('xc7k325t.xdlrc','r') as f1,open('tile','w') as f2,open('sw','w') as f3:
    i=0
    for everyline in f1:
        i=i+1
        if (everyline[2:6] == 'tile' ):
            f2.write(str(i))
            f2.write(',')
            everyline=everyline.rstrip( )
            if (everyline[-1] == '1' and 'INT' in everyline):
                f3.write(str(i))
                f3.write(',')

'''
'''
import sys
with open('xc7k325t.xdlrc','r') as f1,open('tileXY', 'w') as f2:
    i = 0
    j = 0
    nu = 0
    loopnumber=sw.index(376919878)
    for everyline in f1:
        # print('j',j)
        i = i + 1
        p = tile.index(sw[j])
        if (i >= sw[j] and i <= tile[p+1]-1):  #输出sw有关的线型
           # print('i',i)
           # print(sw[j])
           # print(tile[p + 1])
           # print(tile[p + 1] - 1)
            f2.write(everyline)
            if (i == tile[p + 1] - 1):
                j = j + 1
        if(j > loopnumber):
            sys.exit()
'''
"""
#输出所有开关矩阵所在tile的坐标信息
with open('xc7k325t.xdlrc','r') as f1,open('tileXY','w') as f2:
    everyline_flag = 0
    for everyline in f1:
        #print(everyline_flag)
        everyline = everyline.rstrip()
        #print(everyline)
        if (everyline[2:6] == 'tile' and  everyline[-1] == '1' and 'INT' in everyline):
            everyline_flag = 1
        if (everyline[1:2] == ')'):
            everyline_flag = 0
        if (everyline_flag == 1):
            f2.write(everyline)
            f2.write('\n')
"""

pipbefore_part= ['BYP_ALT0', 'BYP_ALT1', 'BYP_ALT2', 'BYP_ALT3', 'BYP_ALT4', 'BYP_ALT5', 'BYP_ALT6', 'BYP_ALT7', 'BYP_BOUNCE0', 'BYP_BOUNCE1', 'BYP_BOUNCE2', 'BYP_BOUNCE3', 'BYP_BOUNCE4', 'BYP_BOUNCE5', 'BYP_BOUNCE6', 'BYP_BOUNCE_N3_2', 'BYP_BOUNCE_N3_3', 'BYP_BOUNCE_N3_6', 'BYP_BOUNCE_N3_7', 'EE2END0', 'EE2END1', 'EE2END2', 'EE2END3', 'EE4END0', 'EE4END1', 'EE4END2', 'EE4END3', 'EL1END0', 'EL1END1', 'EL1END2', 'EL1END3', 'EL1END_S3_0', 'ER1END0', 'ER1END1', 'ER1END2', 'ER1END3', 'ER1END_N3_3', 'FAN_ALT0', 'FAN_ALT1', 'FAN_ALT2', 'FAN_ALT3', 'FAN_ALT4', 'FAN_ALT5', 'FAN_ALT6', 'FAN_ALT7', 'FAN_BOUNCE1', 'FAN_BOUNCE2', 'FAN_BOUNCE3', 'FAN_BOUNCE4', 'FAN_BOUNCE5', 'FAN_BOUNCE6', 'FAN_BOUNCE7', 'FAN_BOUNCE_S3_0', 'FAN_BOUNCE_S3_2', 'FAN_BOUNCE_S3_4', 'FAN_BOUNCE_S3_6', 'GCLK_L_B0', 'GCLK_L_B1', 'GCLK_L_B2', 'GCLK_L_B3', 'GCLK_L_B4', 'GCLK_L_B5', 'GCLK_L_B6', 'GCLK_L_B6_WEST', 'GCLK_L_B7', 'GCLK_L_B7_WEST', 'GCLK_L_B8', 'GCLK_L_B8_WEST', 'GCLK_L_B9', 'GCLK_L_B9_WEST', 'GCLK_L_B10', 'GCLK_L_B10_WEST', 'GCLK_L_B11', 'GCLK_L_B11_WEST', 'GFAN0', 'GFAN1', 'GND_WIRE', 'LH0', 'LH0<<', 'LH6', 'LH12', 'LOGIC_OUTS_L0', 'LOGIC_OUTS_L1', 'LOGIC_OUTS_L2', 'LOGIC_OUTS_L3', 'LOGIC_OUTS_L4', 'LOGIC_OUTS_L5', 'LOGIC_OUTS_L6', 'LOGIC_OUTS_L7', 'LOGIC_OUTS_L8', 'LOGIC_OUTS_L9', 'LOGIC_OUTS_L10', 'LOGIC_OUTS_L11', 'LOGIC_OUTS_L12', 'LOGIC_OUTS_L13', 'LOGIC_OUTS_L14', 'LOGIC_OUTS_L15', 'LOGIC_OUTS_L16', 'LOGIC_OUTS_L17', 'LOGIC_OUTS_L18', 'LOGIC_OUTS_L19', 'LOGIC_OUTS_L20', 'LOGIC_OUTS_L21', 'LOGIC_OUTS_L22', 'LOGIC_OUTS_L23', 'LV_L0', 'LV_L0<<', 'LV_L9', 'LV_L18', 'LV_L18<<', 'LVB_L0', 'LVB_L0<<', 'LVB_L12', 'NE2END0', 'NE2END1', 'NE2END2', 'NE2END3', 'NE2END_S3_0', 'NE6END0', 'NE6END1', 'NE6END2', 'NE6END3', 'NL1BEG_N3', 'NL1END0', 'NL1END1', 'NL1END2', 'NL1END_S3_0', 'NN2END0', 'NN2END1', 'NN2END2', 'NN2END3', 'NN2END_S2_0', 'NN6END0', 'NN6END1', 'NN6END2', 'NN6END3', 'NN6END_S1_0', 'NR1END0', 'NR1END1', 'NR1END2', 'NR1END3', 'NW2END0', 'NW2END1', 'NW2END2', 'NW2END3', 'NW2END_S0_0', 'NW6END0', 'NW6END1', 'NW6END2', 'NW6END3', 'NW6END_S0_0', 'SE2END0', 'SE2END1', 'SE2END2', 'SE2END3', 'SE6END0', 'SE6END1', 'SE6END2', 'SE6END3', 'SL1END0', 'SL1END1', 'SL1END2', 'SL1END3', 'SR1BEG_S0', 'SR1END1', 'SR1END2', 'SR1END3', 'SR1END_N3_3', 'SS2END0', 'SS2END1', 'SS2END2', 'SS2END3', 'SS2END_N0_3', 'SS6END0', 'SS6END1', 'SS6END2', 'SS6END3', 'SS6END_N0_3', 'SW2END0', 'SW2END1', 'SW2END2', 'SW2END3', 'SW2END_N0_3', 'SW6END0', 'SW6END1', 'SW6END2', 'SW6END3', 'SW6END_N0_3', 'VCC_WIRE', 'WL1END0', 'WL1END1', 'WL1END2', 'WL1END3', 'WL1END_N1_3', 'WR1END0', 'WR1END1', 'WR1END2', 'WR1END3', 'WR1END_S1_0', 'WW2END0', 'WW2END1', 'WW2END2', 'WW2END3', 'WW2END_N0_3', 'WW4END0', 'WW4END1', 'WW4END2', 'WW4END3', 'WW4END_S0_0']
pipbehind_part= ['BYP_BOUNCE0', 'BYP_L0', 'BYP_BOUNCE1', 'BYP_L1', 'BYP_BOUNCE2', 'BYP_L2', 'BYP_BOUNCE3', 'BYP_L3', 'BYP_BOUNCE4', 'BYP_L4', 'BYP_BOUNCE5', 'BYP_L5', 'BYP_BOUNCE6', 'BYP_L6', 'BYP_BOUNCE7', 'BYP_L7', 'BYP_ALT1', 'BYP_ALT5', 'FAN_ALT2', 'FAN_ALT7', 'IMUX_L2', 'IMUX_L4', 'IMUX_L10', 'IMUX_L12', 'IMUX_L18', 'IMUX_L20', 'IMUX_L26', 'IMUX_L28', 'IMUX_L34', 'IMUX_L36', 'IMUX_L42', 'IMUX_L44', 'BYP_ALT2', 'BYP_ALT4', 'FAN_ALT5', 'FAN_ALT6', 'GFAN0', 'GFAN1', 'IMUX_L3', 'IMUX_L5', 'IMUX_L11', 'IMUX_L13', 'IMUX_L19', 'IMUX_L21', 'IMUX_L27', 'IMUX_L29', 'IMUX_L35', 'IMUX_L37', 'IMUX_L43', 'IMUX_L45', 'BYP_ALT3', 'BYP_ALT7', 'FAN_ALT1', 'IMUX_L6', 'IMUX_L14', 'IMUX_L22', 'IMUX_L30', 'IMUX_L38', 'IMUX_L46', 'BYP_ALT6', 'FAN_ALT3', 'IMUX_L7', 'IMUX_L15', 'IMUX_L23', 'IMUX_L31', 'IMUX_L39', 'IMUX_L47', 'CTRL_L0', 'CTRL_L1', 'FAN_ALT0', 'IMUX_L0', 'IMUX_L8', 'IMUX_L16', 'IMUX_L24', 'IMUX_L32', 'IMUX_L40', 'BYP_ALT0', 'FAN_ALT4', 'IMUX_L1', 'IMUX_L9', 'IMUX_L17', 'IMUX_L25', 'IMUX_L33', 'IMUX_L41', 'EE2BEG0', 'EE4BEG0', 'EL1BEG_N3', 'ER1BEG1', 'NE2BEG0', 'NE6BEG0', 'NN2BEG0', 'NN6BEG0', 'NR1BEG0', 'SE2BEG0', 'SE6BEG0', 'SL1BEG0', 'SS2BEG0', 'SS6BEG0', 'SW6BEG0', 'WR1BEG1', 'EE2BEG1', 'EE4BEG1', 'EL1BEG0', 'ER1BEG2', 'NE2BEG1', 'NE6BEG1', 'NN2BEG1', 'NN6BEG1', 'NR1BEG1', 'SE2BEG1', 'SE6BEG1', 'SL1BEG1', 'SS2BEG1', 'SS6BEG1', 'SW6BEG1', 'WR1BEG2', 'EE2BEG2', 'EE4BEG2', 'EL1BEG1', 'ER1BEG3', 'NE2BEG2', 'NE6BEG2', 'NN2BEG2', 'NN6BEG2', 'NR1BEG2', 'SE2BEG2', 'SE6BEG2', 'SL1BEG2', 'SS2BEG2', 'SS6BEG2', 'SW6BEG2', 'WR1BEG3', 'EE2BEG3', 'EE4BEG3', 'EL1BEG2', 'ER1BEG_S0', 'NE2BEG3', 'NE6BEG3', 'NN2BEG3', 'NN6BEG3', 'NR1BEG3', 'SE2BEG3', 'SE6BEG3', 'SL1BEG3', 'SS2BEG3', 'SS6BEG3', 'SW6BEG3', 'WR1BEG_S0', 'LH0', 'LH12', 'LV_L0', 'LV_L18', 'CLK_L0', 'CLK_L1', 'FAN_BOUNCE0', 'FAN_L0', 'FAN_BOUNCE1', 'FAN_L1', 'FAN_BOUNCE2', 'FAN_L2', 'FAN_BOUNCE3', 'FAN_L3', 'FAN_BOUNCE4', 'FAN_L4', 'FAN_BOUNCE5', 'FAN_L5', 'FAN_BOUNCE6', 'FAN_L6', 'FAN_BOUNCE7', 'FAN_L7', 'GCLK_L_B6_EAST', 'GCLK_L_B6_WEST', 'GCLK_L_B7_EAST', 'GCLK_L_B7_WEST', 'GCLK_L_B8_EAST', 'GCLK_L_B8_WEST', 'GCLK_L_B9_EAST', 'GCLK_L_B9_WEST', 'GCLK_L_B10_EAST', 'GCLK_L_B10_WEST', 'GCLK_L_B11_EAST', 'GCLK_L_B11_WEST', 'LVB_L0', 'LVB_L12', 'NW6BEG3', 'WW4BEG3', 'NW6BEG1', 'WW4BEG1', 'NW6BEG0', 'WW4BEG0', 'NL1BEG_N3', 'NW2BEG0', 'SR1BEG1', 'SW2BEG0', 'WL1BEG_N3', 'WW2BEG0', 'NL1BEG0', 'NW2BEG1', 'SR1BEG2', 'SW2BEG1', 'WL1BEG0', 'WW2BEG1', 'NL1BEG1', 'NW2BEG2', 'NW6BEG2', 'SR1BEG3', 'SW2BEG2', 'WL1BEG1', 'WW2BEG2', 'WW4BEG2', 'NL1BEG2', 'NW2BEG3', 'SR1BEG_S0', 'SW2BEG3', 'WL1BEG2', 'WW2BEG3']

'''  
with open('tileXY','r') as f1,open('dic_graph', 'w') as f2,open('dic_outdegree', 'w') as f3,open('dic_flag', 'w') as f4:
    lastobj = 'wire'
    wiresite=0
    pipbe=[]
    wirebefore=[]
    i=0
    m=0
    wireflag = 0
    for everyline in f1:
        everyline = everyline.rstrip()
        if(everyline[2:6] == 'tile'):
            start = everyline.index('INT')
            sitenumber = everyline[start:-7]  #提取tile的坐标信息
            pipbe = []
            wirebefore = []
            lastobj = 'wire'
            i = 0
            m = 0
            flag = 1
        elif(everyline[3:7] == 'wire' and everyline[10:14] == '6BEG'):
            if (wirebefore != []):  # 统计pip字典索引情况
                #print('str',m)
                f3.write("'" + lastobj + "':" + str(i) + ',' + '\n')
                f4.write("'" + lastobj + "':" + '1' + ',' + '\n')
                f2.write(']' + ',' +'\n')
                lastobj = 'wire'
                lastpip = 'pip'
                wireflag = 0
                i = 0  # 统计字典索引对象
            c = everyline.rfind(' ')
            lastobj = sitenumber + everyline[8:c]
            f2.write("'" + lastobj + "':[")
            wiresite = lastobj.index('6BEG')
            #print(lastobj)
            wirebefore.append(lastobj)
            wireflag=1   #标志上一个wire已经写入
        elif (everyline[4:8] == 'conn' and wireflag == 1):
            b = everyline.rfind(' ')
            if(everyline[b+3:b+7] == '6END'):
                if (i == 0):
                    f2.write("'" + everyline[9:-1] + "'")
                    i = i + 1
                    #print(m)
                else:
                    f2.write(",'" + everyline[9:-1] + "'")
                    i = i + 1
                    #print(m)
        elif(everyline[2:3] == ')'):
            wireflag = 0
        elif(everyline[2:19] == '(wire WW4END_S0_0' and flag == 1):
            f3.write("'" + lastobj + "':" + str(i) + ',' + '\n')
            f4.write("'" + lastobj + "':" + '1' + ',' + '\n')
            f2.write(']' + ',' + '\n')
            flag = 0
        elif (everyline[3:6] == 'pip'):
            pipsite = everyline.index('-')
            partbe=everyline[:pipsite-1]
            ns=partbe.rfind(' ')
            if(everyline[ns+3:ns+7] == '6END' and everyline[-6:-2] == '6BEG'):
                newpip = everyline[7:pipsite - 1]
                # print(newpip)
                if (newpip not in pipbe):
                    # print('newpip', newpip)
                    if (pipbe != []):  # 统计pip字典索引情况
                        # print('str', m)
                        f3.write("'" + lastpip + "':" + str(m) + ',' + '\n')
                        f4.write("'" + lastpip + "':" + '1' + ',' + '\n')
                        f2.write(']' + ',' + '\n')
                        m = 0  # 统计字典索引对象
                    f2.write("'" + newpip + "':[")
                    f2.write("'" + sitenumber + everyline[pipsite + 3:-1] + "'")
                    pipbe.append(newpip)
                    lastpip = newpip
                    m = m + 1
                    # print('m', m)
                else:
                    # print('newpip', newpip)
                    f2.write(",'" + sitenumber + everyline[pipsite + 3:-1] + "'")
                    m = m + 1
                    # print('m', m)       
        if (everyline[3:15] == 'tile_summary'):
            f3.write("'" + newpip + "':" + str(m) + ',' + '\n')
            f4.write("'" + newpip + "':" + '1' + ',' + '\n')
            f2.write(']' + ',' + '\n')
'''
#建模与参数化过程
with open('tileXY','r') as f1,open('graph', 'w') as f2,open('outdegree', 'w') as f3,open('flag', 'w') as f4:
    for everyline in f1:
        everyline = everyline.rstrip()
        if (everyline[2:6] == 'tile'):
            start = everyline.index('INT')
            sitenumber = everyline[start:-7]  # 提取tile的坐标信息
            wire_BEG = []  #存放wire信息
            wire_END = []
            wireflag = 0
            pipbe = []
            m = 0
        elif (everyline[3:7] == 'wire'):
            if(everyline[10:14] == '6BEG' and 'BEG_' not in everyline):
                wireflag = 1  # 标志上一个wire BEG已经写入
                c = everyline.rfind(' ')
                lastobj = sitenumber + everyline[8:c]
                wire_BEG.append(lastobj)
            if(everyline[10:14] == '6END' and 'END_' not in everyline):
                wireflag = 2  # 标志上一个wire END已经写入
                c = everyline.rfind(' ')
                lastobj = sitenumber + everyline[8:c]
                wire_END.append(lastobj)
        elif (everyline[4:8] == 'conn' and (wireflag == 1 or wireflag == 2)):
            b = everyline.rfind(' ')
            if (everyline[b + 3:b + 7] == '6END' and wireflag == 1 and 'END_' not in everyline):   #将金属连接线的后半部分放入wire
                wire_BEG.append(everyline[9:-1])
                wireflag = 0
            elif (everyline[b + 3:b + 7] == '6BEG' and wireflag == 2 and 'BEG_' not in everyline):
                wire_END.append(everyline[9:-1])
                wireflag = 0
        elif (everyline[3:6] == 'pip' and 'END_' not in everyline and 'BEG_' not in everyline):
            pipsite = everyline.index('-')
            partbe = everyline[:pipsite - 1]
            ns = partbe.rfind(' ')
            if (everyline[ns + 3:ns + 7] == '6END' and everyline[-6:-2] == '6BEG'):
                newpip = everyline[7:pipsite - 1]    #pip的前半部分END结尾
                q = wire_END.index(newpip)
                newpip = wire_END[q+1] + ' ' + wire_END[q]
                #print(newpip)
                if (newpip not in pipbe):    #字典中新的pip
                    # print('newpip', newpip)
                    if (pipbe != []):    #从第二个pip开始完善pip信息
                        # print('str', m)
                        f3.write("'" + lastpip + "':" + str(m) + ',' + '\n')
                        f4.write("'" + lastpip + "':" + '1' + ',' + '\n')
                        f2.write(']' + ',' + '\n')
                        m = 0  # 统计字典索引对象
                    f2.write("'" + newpip + "':[")   #写入键值
                    z = wire_BEG.index(sitenumber + everyline[pipsite + 3:-1])
                    pipafter = wire_BEG[z] + ' ' + wire_BEG[z+1]
                    #print(pipafter)
                    f2.write("'" + pipafter + "'")  #写入value值
                    pipbe.append(newpip)
                    lastpip = newpip
                    m = m + 1
                    # print('m', m)
                else:
                    # print('newpip', newpip)
                    z = wire_BEG.index(sitenumber + everyline[pipsite + 3:-1])
                    pipafter = wire_BEG[z] + ' ' + wire_BEG[z + 1]
                    f2.write(",'" + pipafter + "'")    #写入同键值的value值
                    m = m + 1
                    # print('m', m)
        elif ('tile_summary' in everyline):
            f3.write("'" + newpip + "':" + str(m) + ',' + '\n')
            f4.write("'" + lastpip + "':" + '1' + ',' + '\n')
            f2.write(']' + ',' + '\n')


