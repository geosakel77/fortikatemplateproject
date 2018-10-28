__project__="hellofortika"


class HelloFortika:

    def __init__(self,public_param=1,private_param=2):
        """
        Put a short description here
        @param public_param:
        @param private_param:
        """
        self.public_param=public_param
        self._private_param=private_param
        self._fortika = "Hello FORTIKA"

    def print_fortika(self):
        """
        Put a short description here
        @return: 0
        """
        try:
            print(self._fortika)
            return 0
        except OSError as e:
            print(e.args)
            return -1
        else:
            print("General Exception Handling")
            return 1
