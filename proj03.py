#Project 03
#Created by Hafed
#November 7,2016
#CIT-125 Python

iscol=True
def headers(column): # This function create a table column headers
      iscol=True
      headers=["Player name" ,"TeamId" , "Games", "At bats" ,"Runs scored", "Hits" ,"Doubles","Triples","Homeruns",column]
      header=''
      for hedr in headers:
           if hedr== headers[0]:
                header+='| '+hedr.center(24,' ')
           else:
                if hedr=='':
                      iscol=False
                      break
                header+='|'+hedr.center(11,' ')
      if iscol:
          print('-'.ljust(135, '-'))
          print(header+'|')
          print('-'.ljust(135, '-'))           
      else:
          print('-'.ljust(123, '-'))
          print(header+'|')
          print('-'.ljust(123, '-'))
    
Tids=[]
fcounter=1
while True:
      # Commands validation section-----------------------------------------
      cmd=input(">> Please, Enter a command: ")
      wcmd=cmd
      if not cmd:
          print("Null value is not recognized as a valid command.")
          continue
      cmd=cmd.upper()
      CMD=cmd.split()
      cmd=CMD[0]
      if  cmd=='QUIT':
           if len(CMD)>1:
                print("Invalid command ! Try again.")
                continue
           else:
                quit()
      elif cmd=='HELP':
           if len(CMD)>1:
                print("Invalid command ! Try again.")
                continue
           else:
                print()
                print("HELP                Displays all available commands)")
                print("INPUT [filename]    Displays all players in the 'mlb.2013.txt' file.")
                print("TEAM [team id]      Displays a team with a specific identifier.")
                print("REPORT [int n][str] Displays all information about the top n players in a given category:") 
                print("                    HITS -- number of hits")
                print("                    BATTING -- batting average ")
                print("                    SLUGGING -- slugging percentage.")
                print("QUIT                Halts the execution.")
                print()

      #Read from file section------------------------------------
      elif cmd=='INPUT':
           if len(CMD)>2 or len(CMD)==1 :
                print("Invalid command ! Try again.")
                continue
           elif CMD[1]!='MLB.2013.TXT':
                if fcounter==3:
                      print("Maximum attempts to open the file exceeded.")
                      quit()
                else:
                      print("Invalid file name ! Try again.")
                      fcounter+=1
                      continue
           else:
                tline=()
                headers('')
                f=open('mlb.2013.txt')
                for lin in f:
                     tline=lin.strip().split(';')
                     header=''
                     for word in tline:
                             if word== tline[0]:
                                  header+='| '+word.ljust(24,' ')
                             elif word== tline[1]:
                                  header+='|'+'  '+word.center(4,' ')
                             else:
                                  header+='     |'+word.rjust(6,' ')
                     print(header+'     |')
                f.close()
                print('-'.ljust(123, '-')) 
      elif cmd=='TEAM':
           if len(CMD)>2 or len(CMD)==1 :
                print("Invalid command ! Try again.")
                continue
           else:
                f=open('mlb.2013.txt')
                for ln in f:
                     line=ln.strip().split(';')
                     if line[1].strip()  not in Tids:
                          Tids.append(line[1].strip() )
                f.close()
                CMD[1]=CMD[1].upper()
                if CMD[1] not in Tids:
                     print("Invalid team identifier !")
                     continue
                else:
                     headers('')
                     f=open('mlb.2013.txt')
                     for player in f:
                          pline=player.strip().split(';')
                          if pline[1].strip()==CMD[1]:
                               header=''
                               for word in pline:
                                   if word== pline[0]:
                                        header+='| '+word.ljust(24,' ')
                                   elif word== pline[1]:
                                        header+='|'+'  '+word.center(4,' ')
                                   else:
                                        header+='     |'+word.rjust(6,' ')
                               print(header+'     |')
                     f.close()
                     print('-'.ljust(123, '-'))
      elif cmd=='REPORT':
           if len(CMD)>3 or len(CMD)<3 :
                print("Invalid command ! Try again.")
                continue
           else:
                if not CMD[1].isnumeric() or int(CMD[1])==0:
                     print("REPORT command has to be followed by an integer greater than zero !")
                     continue
                elif CMD[2] not in["HITS","BATTING","SLUGGING"]:
                     print("Invalid identifier ! ")
                     continue
                else:
                    result=[]
                    f=open('mlb.2013.txt')
                    for player in f:
                          pline=player.strip().split(';')
                          if CMD[2]=='HITS':
                               column=''
                               iscol=False
                               if int(pline[5]) not in result:
                                    result.append(int(pline[5]))
                          if CMD[2]=='BATTING':
                               column='Batting'
                               iscol=True
                               btg='%.3f' %(int(pline[5])/int(pline[3]))#Batting percentage calculation
                               if btg not in result:
                                    result.append(btg)
                          if CMD[2]=='SLUGGING':
                               column='Slugging'
                               iscol=True
                               single=int(pline[5])-int(pline[6])-int(pline[7])-int(pline[8])
                               slg=(single+2*int(pline[6])+3*int(pline[7])+4*int(pline[8]))/int(pline[3])#Slugging percentage calculation 
                               if slg not in result:
                                    result.append('%.3f' %slg)
                    result.sort()
                    result.reverse()
                    result=result[:int(CMD[1])]
                    f.close()
                    i=0
                    headers(column)
                    for score in result:
                        if i==int(CMD[1]):
                             break 
                         
                        f=open('mlb.2013.txt')
                        for pl in f:
                            pls=pl.strip().split(';')
                            if CMD[2]=='HITS':
                                if int(pls[5])==score:
                                      if i==int(CMD[1]):
                                           break
                                      header=''
                                      for word in pls:
                                               if word== pls[0]:
                                                    header+='| '+word.ljust(24,' ')
                                               elif word== pls[1]:
                                                    header+='|'+'  '+word.center(4,' ')
                                               else:
                                                    header+='     |'+word.rjust(6,' ')
                                      print(header+'     |')
                                      i+=1
                            elif CMD[2]=='BATTING':
                                if score=='%.3f' %(int(pls[5])/int(pls[3])): #Batting percentage calculation
                                      if i==int(CMD[1]):
                                           break
                                      header=''
                                      pls.append(score)
                                      for word in pls:
                                         if word== pls[0]:
                                              header+='| '+word.ljust(24,' ')
                                         elif word== pls[1]:
                                              header+='|'+'  '+word.center(4,' ')
                                         elif word== pls[9]:
                                              header+='     |'+'   '+word.center(6,' ')
                                         else:
                                              header+='     |'+word.rjust(6,' ')
                                      print(header+'  |')
                                      i+=1
                            else:
                                single=int(pls[5])-int(pls[6])-int(pls[7])-int(pls[8]) #Slugging percentage calculation 
                                slg=(single+2*int(pls[6])+3*int(pls[7])+4*int(pls[8]))/int(pls[3])
                                if score=='%.3f' %slg:  
                                      if i==int(CMD[1]):
                                           break
                                      header=''
                                      pls.append(score)
                                      for word in pls:
                                         if word== pls[0]:
                                              header+='| '+word.ljust(24,' ')
                                         elif word== pls[1]:
                                              header+='|'+'  '+word.center(4,' ')
                                         elif word== pls[9]:
                                              header+='     |'+'   '+word.center(6,' ')
                                         else:
                                              header+='     |'+word.rjust(6,' ')
                                      print(header+'  |')

                                      i+=1

                    f.close()
                    if iscol:
                         print('-'.ljust(135, '-'))
                    else:
                         print('-'.ljust(123, '-'))
                    
      else:
          print("'"+wcmd+"' is not recognized as a valid command.")
          continue
      print()
