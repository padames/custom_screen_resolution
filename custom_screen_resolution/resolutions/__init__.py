"""Top-level package for Custom Screen Resolution."""

__author__ = """anopensourcecoder"""
__email__ = 'anopensourcecoder@gmail.com'
__version__ = '0.2.0'

import math

class PPI():
    def __init__(self,x,y,size,scale=1):
        self.x=x
        self.y=y
        self.size=size
        self.scale=scale

    def get(self):
        dpx2 =  self.x**2  + self.y**2
        dpx =  math.sqrt(dpx2)
        ppi = (  dpx / self.size ) / self.scale
        return ppi

    def display(self):
        print( str(self.x)+"x"+ str(self.y)+"\t*"+str(self.size)+"\t/"+str(self.scale) + "\t%.2f" % self.get())

class Scale():
    def __init__(self,x,y,size,ppi):
        self.x=x
        self.y=y
        self.size=size
        self.ppi=ppi

    def get(self):
        dpx2 =  self.x**2  + self.y**2
        dpx =  math.sqrt(dpx2)
        scale = self.ppi /(  dpx / self.size )
        return scale

    def display(self):
        print( str(self.x)+"x"+ str(self.y)+"\t*"+str(self.size)+"\t/"+str(self.ppi) + "\t%.2f" % self.get())


class Height( ):
    def __init__(self, ratio_x, ratio_y, width_pixels ):
        self.ratio_x = ratio_x
        self.ratio_y= ratio_y
        self.ratio = self.ratio_x / self.ratio_y
        self.width_pixels = width_pixels
        self.get()
    def get(self):
        self.height_pixels = self.width_pixels / self.ratio
        self.height_pixels = self.width_pixels / self.ratio


    def display(self):
        #print( "width_inches", self.width_inches, "height_inches", self.height_inches )
        print( "width_pixels=",self.width_pixels, "height_pixels=",self.height_pixels )


class Resolution( ):
    def __init__(self,diagonal_size , ppi , ratio_x, ratio_y ):
        self.diagonal_size = float( diagonal_size)
        self.ppi = float(ppi)
        self.ratio_x = float(ratio_x)
        self.ratio_y= float(ratio_y)
        self.ratio = self.ratio_x / self.ratio_y
        self.width_pixels = 0
        self.height_pixels = 0
        self.get()


    def get(self):
        self.width_inches = self.ratio * math.sqrt( (self.diagonal_size**2) / (self.ratio**2 + 1) )
        self.height_inches = math.sqrt( (self.diagonal_size**2 ) / (self.ratio**2 + 1) )

        #Physical Size = Pixels / Density
        #Pixels = Physical Size / Density


        width_pixels = self.width_inches * self.ppi
        height_pixels = self.height_inches * self.ppi

        self.width_pixels = width_pixels + 8 - (width_pixels % 8)
        self.height_pixels = height_pixels + 8 - (height_pixels % 8)

    def get_width_pixels(self):
        return int(self.width_pixels)

    def get_height_pixels(self):
        return int(self.height_pixels)

    def get_ratio_x(self):
        return self.ratio_x

    def get_ratio_y(self):
        return self.ratio_y

    def get_ratio(self):
        return self.ratio

    def get_diagonal_size(self):
        return self.diagonal_size

    def display(self):
        print("\t%.2f" %self.diagonal_size  + "\t%.2f" % self.ppi
              + "\t%.0f" % self.width_pixels + "x%.0f" % self.height_pixels )

