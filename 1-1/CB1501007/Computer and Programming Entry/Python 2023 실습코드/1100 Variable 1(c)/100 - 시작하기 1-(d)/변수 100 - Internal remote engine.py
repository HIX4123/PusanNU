#!/usr/bin/python3
# Zoh Q. 2019

##Python Engines:
##
## 1) Internal
## This Python engine is faster than the other options however if there are problems with the scripts you are running or debugging they could affect the reliability of PyScripter and could cause crashes. Another limitation of this engine is that it cannot run or debug GUI scripts nor it can be reinitialized.
##
## 2) Remote
##   This the default Python engine of PyScripter and is the recommended engine for most Python development tasks. It runs in a child process and communicates with PyScripter using rpyc. It can be used to run and debug any kind of script including GUI scripts. However if you run or debug GUI scripts you may have to reinitialize the engine after each run.
##
##  3) Remote Tk
##
##This remote Python engine is specifically created to run and debug Tkinter applications including pylab using the Tkagg backend. It also supports running pylab in interactive mode. The engine activates a Tkinter mainloop and replaces the mainloop with a dummy function so that the Tkinter scripts you are running or debugging do not block the engine. You may even develop and test Tkinter widgets using the interactive console.
##
##Remote Wx
##
##This remote Python engine is specifically created to run and debug wxPython applications including pylab using the WX and WXAgg backends. It also supports running pylab in interactive mode. The engine activates a wx MainLoop and replaces the MainLoop with a dummy function so that the wxPython scripts you are running or debugging do not block the engine. You may even develop and test wxPython Frames and Apps using the interactive console. Please note that this engine prevents the redirection of wxPython output since that would prevent the communication with Pyscripter. When using the Tk and Wx remote engines you can of course run or debug any other non-GUI Python script. However bear in mind that these engines may be slightly slower than the standard remote engine since they also contain a GUI main loop.
##
##Debugging Wx and Tkinter scirpts using the remote Wx and Tk engines
##
##As mentioned above the Wx and Tk engines activate a main loop and replace the MainLoop with a dummy function. Therefore, when debugging Gui scripts using these engines, as soon as you reach the MainLoop statement debugging ends and you can then test the running application but without further debugging support. This means two things:
##•Breakpoints and debugging would work up to the point the script enters the MainLoop routine
##•You will not be able to debug event triggered code using these two engines.
##
##To debug event code of Wx and Tkinter scripts use the standard remote engine. You may wonder why should you ever use the Wx and Tk specific remote engines. Here is a few reasons:
##•These engine allow you to interactively develop and test frames and widgets. (possible because they run their own main loop.
##•They support running pylab in interactive mode like IPython does, which was a request from many Pyscripter users.
##•There is no need to reinitialize the engines after running Gui scripts.
##•Pyscripter does not stay in running mode while the Gui Windows are showing but instead it returns in ready mode allowing further work and runs.
