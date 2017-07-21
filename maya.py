import csv
import time
d = {}
with open('/Users/chandanidoshi/Downloads/arms.csv', 'rb') as csvfile:
    linereader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    t = 0
    for row in linereader:
        d[t] = {}
        rowstring = row[0]
        rowsplit = rowstring.split(',')
        d[t]['head'] = [float(rowsplit[9]), float(rowsplit[10]), float(rowsplit[11])]
        d[t]['hip_center'] = [float(rowsplit[0]), float(rowsplit[1]), float(rowsplit[2])]
        d[t]['right_hip'] = [float(rowsplit[48]), float(rowsplit[49]), float(rowsplit[50])]
        d[t]['left_elbow']= [float(rowsplit[15]), float(rowsplit[16]), float(rowsplit[17])]
        d[t]['left_foot'] = [float(rowsplit[45]), float(rowsplit[46]), float(rowsplit[47])]
        d[t]['left_hip'] = [float(rowsplit[36]), float(rowsplit[37]), float(rowsplit[38])]
        d[t]['left_knee'] = [float(rowsplit[39]), float(rowsplit[40]), float(rowsplit[41])]
        d[t]['left_shoulder'] = [float(rowsplit[12]), float(rowsplit[13]), float(rowsplit[14])]
        d[t]['left_wrist'] = [float(rowsplit[18]), float(rowsplit[19]), float(rowsplit[20])]
        d[t]['neck'] = [float(rowsplit[6]), float(rowsplit[7]), float(rowsplit[8])]
        d[t]['right_elbow'] = [float(rowsplit[27]), float(rowsplit[28]), float(rowsplit[29])]
        d[t]['right_foot']= [float(rowsplit[57]), float(rowsplit[58]), float(rowsplit[59])]
        d[t]['right_knee']= [float(rowsplit[51]), float(rowsplit[52]), float(rowsplit[53])]
        d[t]['right_shoulder'] = [float(rowsplit[24]), float(rowsplit[25]), float(rowsplit[26])]
        d[t]['right_wrist'] = [float(rowsplit[30]), float(rowsplit[31]), float(rowsplit[32])]
        d[t]['spine'] = [float(rowsplit[3]), float(rowsplit[4]), float(rowsplit[5])]
        t+=1

cmds.select(clear=True)
joints = cmds.ls(type='joint')
s=150

for i in sorted(d.keys()):
    cmds.setKeyframe(joints,time=10*i)
    for j in joints:
        newJ = j[9:]
        cmds.select(clear=True)
        cmds.select(j)
        cmds.move(s*d[i][newJ][0], s*d[i][newJ][1], s*d[i][newJ][2])
        cmds.select(clear=True)