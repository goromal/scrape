from colorama import Fore, Style

class ColorPrint(object):
    @staticmethod
    def Green(string):
        print(f"{Fore.GREEN}%s{Style.RESET_ALL}" % string)
    @staticmethod
    def Cyan(string):
        print(f"{Fore.CYAN}%s{Style.RESET_ALL}" % string)
    @staticmethod
    def Blue(string):
        print(f"{Fore.BLUE}%s{Style.RESET_ALL}" % string)
    @staticmethod
    def Warn(string):
        print(f"{Fore.YELLOW}%s{Style.RESET_ALL}" % string)
    @staticmethod
    def Fail(string):
        print(f"{Fore.RED}%s{Style.RESET_ALL}" % string)
    @staticmethod
    def Bold(string):
        print(f"{Style.BRIGHT}%s{Style.RESET_ALL}" % string)
