import gui
import init
#This is kind of like a bootstrapper for the other two scripts

try: 
    l = init.login()
    temp = l.return_vals
    #TODO: l.close doesnt work, try and fix
    l.root.quit() #cant get it to work, now assume its a bug with the library itself
    win = gui.Window(temp[0], temp[1], temp[2]) #connector, db and table
except:
    print("DBG: Failed to connect to DB. Fatal")
    pass