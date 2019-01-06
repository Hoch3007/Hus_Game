
# coding: utf-8

# In[2]:

def test(auswahl, spieler, gegenspieler, paare):
    
    if auswahl in paare.keys():
    
        if gegenspieler[paare[auswahl][0]]>0:
            #print "3. Reihe " + str(paare[auswahl][0]), gegenspieler[paare[auswahl][0]]
            #print "4. Reihe " + str(paare[auswahl][1]), gegenspieler[paare[auswahl][1]]

            schritte = gegenspieler[paare[auswahl][0]]+gegenspieler[paare[auswahl][1]]+spieler[auswahl]

            gegenspieler[paare[auswahl][0]]=0
            gegenspieler[paare[auswahl][1]]=0

        else: 

            schritte = spieler[auswahl]
    
    else:
        
        schritte = spieler[auswahl]
    
    #print schritte
    return schritte


# In[3]:

def spielbrett(spieler, gegenspieler, nummer1, nummer2):
    
    print "Das Spielbrett aus der Perspektive von "+ nummer1 + "."
    
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(gegenspieler[9])+" | "+str(gegenspieler[10])+" | "+str(gegenspieler[11])+" | "+str(gegenspieler[12])+" | "+str(gegenspieler[13])+" | "+str(gegenspieler[14])+" | "+str(gegenspieler[15])+" | "+str(gegenspieler[16])+" | "
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(gegenspieler[8])+" | "+str(gegenspieler[7])+" | "+str(gegenspieler[6])+" | "+str(gegenspieler[5])+" | "+str(gegenspieler[4])+" | "+str(gegenspieler[3])+" | "+str(gegenspieler[2])+" | "+str(gegenspieler[1])+" | "
    print " --- --- --- --- --- --- --- --- "
    
    
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(spieler[1])+" | "+str(spieler[2])+" | "+str(spieler[3])+" | "+str(spieler[4])+" | "+str(spieler[5])+" | "+str(spieler[6])+" | "+str(spieler[7])+" | "+str(spieler[8])+" | "
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(spieler[16])+" | "+str(spieler[15])+" | "+str(spieler[14])+" | "+str(spieler[13])+" | "+str(spieler[12])+" | "+str(spieler[11])+" | "+str(spieler[10])+" | "+str(spieler[9])+" | "
    print " --- --- --- --- --- --- --- --- "
    
    print ""
    print ""
    
    print "Das Spielbrett aus der Perspektive von "+ nummer2 + "."
    
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(spieler[9])+" | "+str(spieler[10])+" | "+str(spieler[11])+" | "+str(spieler[12])+" | "+str(spieler[13])+" | "+str(spieler[14])+" | "+str(spieler[15])+" | "+str(spieler[16])+" | "
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(spieler[8])+" | "+str(spieler[7])+" | "+str(spieler[6])+" | "+str(spieler[5])+" | "+str(spieler[4])+" | "+str(spieler[3])+" | "+str(spieler[2])+" | "+str(spieler[1])+" | "
    print " --- --- --- --- --- --- --- --- "
    
    
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(gegenspieler[1])+" | "+str(gegenspieler[2])+" | "+str(gegenspieler[3])+" | "+str(gegenspieler[4])+" | "+str(gegenspieler[5])+" | "+str(gegenspieler[6])+" | "+str(gegenspieler[7])+" | "+str(gegenspieler[8])+" | "
    print " --- --- --- --- --- --- --- --- "
    print "| "+str(gegenspieler[16])+" | "+str(gegenspieler[15])+" | "+str(gegenspieler[14])+" | "+str(gegenspieler[13])+" | "+str(gegenspieler[12])+" | "+str(gegenspieler[11])+" | "+str(gegenspieler[10])+" | "+str(gegenspieler[9])+" | "
    print " --- --- --- --- --- --- --- --- "
    
    
    


# In[4]:

def zug(start, schritte, auswahl,spieler, gegenspieler, paare):
    
    
    spieler[auswahl]=0
    
    while schritte>0:
            spieler[start] +=1
            schritte -=1
            
            if schritte >0:
                if start ==16:
                    start =1
                else: 
                    start+=1
            #print "Start: ",start
            
    if spieler[start]>1:
        auswahl = start
        #print "Auswahl: ", auswahl
        
        if start ==16:
            start =1
        else: 
            start+=1
        
        #print "Start: ", start
        schritte = test(auswahl, spieler, gegenspieler, paare)
        #print "Schritte: ", schritte
        zug(start, schritte, auswahl, spieler, gegenspieler, paare)    


# In[5]:

def sieg(spieler, gegenspieler, paare, name1, name2):
    
    steine1 = spieler.values()
    steine2 = gegenspieler.values()
    
    if all(i <=1 for i in steine1):
        
        print "Spieler 2 hat gewonnen! Herzlichen Glückwusch!"

    elif all(i <=1 for i in steine2):
        
        print "Spieler 1 hat gewonnen! Herzlichen Glückwusch!"
    
    else:
        temp = spieler
        spieler=gegenspieler
        gegenspieler = temp
        
        print "Weiter geht's, " + name2 + " ist dran."
        auswahl = raw_input("Welches Feld willst du spielen? ")
        if auswahl =="exit":
            "Vielen Dank! Das Spiel wurde beendet."
        else:
            auswahl=int(auswahl)
            start = auswahl + 1
            schritte = spieler[auswahl]

            zug(start, schritte, auswahl,spieler, gegenspieler, paare)
            spielbrett(spieler, gegenspieler, name2, name1)
            sieg(spieler, gegenspieler, paare, name2, name1)


# In[6]:

def hus():
    
    print "!HUS"
    print "----"
    print "Regeln ..."
    print "Die eigenen Felder sind immer unten."
    print ""
    print "Die Nummerierung ist wie folgt:"
    print "1  2  3  4  5  6  7  8"
    print "16 15 14 13 12 11 10 9"
    
    nummer1 = raw_input("Wie heisst Spieler 1? ")
    nummer2 = raw_input("Wie heisst Spieler 2? ")
    
    spieler1 ={1: 0, 2:0,3:0, 4:0, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2}
    spieler2 ={1: 0, 2:0,3:0, 4:0, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2}

    paare = {16:[8,9], 15:[7,10], 14:[6,11], 13:[5,12], 12:[4,13], 11:[3,14], 10:[2,15], 9:[1,16]}
    print "So sehen die Spielbretter zum Start aus."
    spielbrett(spieler1, spieler2, nummer1, nummer2)
    
    auswahl_spieler1 = int(raw_input("Mit welchem Feld willst du beginnen? "))
       
    auswahl = auswahl_spieler1

    start = auswahl + 1
    schritte = spieler1[auswahl]
    
    zug(start, schritte, auswahl,spieler1, spieler2, paare)
    print "So sieht das Brett nach dem ersten Zug aus: "
    spielbrett(spieler1, spieler2, nummer1, nummer2)
    sieg(spieler1, spieler2, paare, nummer1, nummer2)


# In[7]:

hus()


# In[ ]:



