class pata_nhi_kya_naam_dau:
    def __init__(self):
        self.something = ''
    def msg(self):
        self.something = input("enter a msg: ")
    def dms(self):
        print("you message in upper sting is: ", self.something.upper())
ob = pata_nhi_kya_naam_dau()
ob.msg()
ob.dms()