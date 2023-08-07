def distance(p1,p2):
    d = math.sqrt(math.pow(p1[0] - p2[0], 2) +math.pow(p1[1] - p2[1], 2) +math.pow(p1[2] - p2[2], 2)* 1.0)
    return d
    
def features(landmarks):
    feat=[]
    landmarks=list(landmarks)
    #1st:15-16
    rwrist=[landmarks[16].x,landmarks[16].y,landmarks[16].z]
    lwrist=[landmarks[15].x,landmarks[15].y,landmarks[15].z]
    feat.append(distance(rwrist,lwrist))
                
    #2nd: 15-11
    lshoulder= [landmarks[11].x,landmarks[11].y,landmarks[11].z]  
    feat.append(distance(rwrist,lshoulder))
                
    #3rd: 12-16
    rshoulder = [landmarks[12].x,landmarks[12].y,landmarks[12].z] 
    feat.append(distance(rshoulder,rwrist))
                
    #4th: 15-23
    lhip= [landmarks[23].x,landmarks[23].y,landmarks[23].z]
    feat.append(distance(lhip,lwrist))
                
    #5th: 16-24
    rhip= [landmarks[24].x,landmarks[24].y,landmarks[24].z] 
    feat.append(distance(rhip,lwrist))
                
    #6th: 23-24
    feat.append(distance(lhip,rhip))
    
    #7th: 16-28
    rankle=[landmarks[28].x,landmarks[28].y,landmarks[28].z]
    feat.append(distance(rankle,rwrist))
                
    #8th: 15-27
    lankle=[landmarks[27].x,landmarks[27].y,landmarks[27].z]
    feat.append(distance(lankle,lwrist))
    
    #9th: 23-27
    feat.append(distance(lhip,lankle))
                
    #10th: 24-28
    feat.append(distance(rhip,rankle))
                
    #11th: 28-27
    feat.append(distance(lankle,rankle))
                
    #12th: 5-30
    rheel=[landmarks[30].x,landmarks[30].y,landmarks[30].z]
    reye=[landmarks[5].x,landmarks[5].y,landmarks[5].z]
    feat.append(distance(reye,rheel))
                
    #13th: 2-29
    leye=[landmarks[2].x,landmarks[2].y,landmarks[2].z]
    lheel=[landmarks[29].x,landmarks[29].y,landmarks[29].z]
    feat.append(distance(leye,lheel))
    
    #14th: 14-27
    relbow=[landmarks[14].x,landmarks[14].y,landmarks[14].z]
    feat.append(distance(relbow,lankle))
                
    #15th: 13-28
    lelbow=[landmarks[13].x,landmarks[13].y,landmarks[13].z]
    feat.append(distance(lelbow,rankle))
    
    #16th: 0-15
    nose=[landmarks[0].x,landmarks[0].y,landmarks[0].z]
    feat.append(distance(nose,lwrist))
    
    #17th: 0-16
    feat.append(distance(nose,rwrist))

    lknee=[landmarks[26].x,landmarks[26].y,landmarks[26].z]
    rknee=[landmarks[25].x,landmarks[25].y,landmarks[25].z]
    feat.append(distance(lknee,rknee))
    
    #19th: 31-32
    ltoe=[landmarks[31].x,landmarks[31].y,landmarks[31].z]
    rtoe=[landmarks[32].x,landmarks[32].y,landmarks[32].z]
    feat.append(distance(ltoe,rtoe))
    
    return feat