#
import splash
from wizard import Wizard


def main():
    list_of_wizard=[]
    continu=splash.splashscreen()
    if continu==True:
        wizard = Wizard()
        wizard.start_wizard()
        list_of_wizard.append(wizard)



if __name__ == "__main__":
    main()


