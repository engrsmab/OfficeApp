from setuptools import setup
APP = ['Main_App.py']
Data_Files = ["Official Logo [Azeem Ent.].jpg","RegButton.png","home-32.png","gear-2-32.png",
              "bill-32.png","us-dollar-32.png","group-32.png","account-logout-32.png","exit.png"]

# Data_Files = [*Images,*Databases]

OPTIONS = {
    'argv_emulation': True,
 }
setup(
    app = APP,
    data_files = Data_Files,
    options ={'py2app': OPTIONS},
    setup_requires = ['py2app']
)