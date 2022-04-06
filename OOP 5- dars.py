# class  VEKTOR_XY:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def get_vektor(self):
#         return f"{self.x}i+{self.y}j"
#
# class VEKTOR_XY_AMAL(VEKTOR_XY):
#     def __init__(self,x,y):
#         super().__init__(x,y)
#     def __add__(self, other):
#         return f"{self.x+other.x}i+{self.y+other.y}j"
#     def __sub__(self, other):
#         return f"{self.x-other.x}i-{self.y-other.y}j"
#     def __mul__(self, other):
#         return (self.x*other.x)+(self.y*other.y)
#     def len_vektor(self):
#         return (self.x**2+self.y**2)**(1/2)
# vektor1=VEKTOR_XY_AMAL(5,-2)
# vektor2=VEKTOR_XY_AMAL(8,5)
# print('vektor1:',vektor1.get_vektor())
# print('vektor2:',vektor2.get_vektor())
# print('yigindi:',vektor1+vektor2)
# print('ayirma:',vektor1-vektor2)
# print('skalyar kopaytma:',vektor1*vektor2)
# print('birinchi vektor uzunligi:',vektor1.len_vektor())
# print('ikkinchi vektor uzunligi:',vektor2.len_vektor())