Another option is to get acquainted with pip and virtualenv. These tools make installing 3rd party modules a breeze. Although I don't know how well they are supported on Windows (I mainly do Python development on Linux).

You'll need to download and install the following libraries:

The Python Imaging Library
Numpy
PyWin
All of the above have self installers; Running them will automatically install the modules into your \lib\site-packages directory and, in theory, adjust your pythonPath accordingly. However in practice this doesn't always happen. Should you begin receiving any Import Error messages after installation, you'll probably need to manually adjust your Environment Variables. More information on adjusting Path Variables may be found here.