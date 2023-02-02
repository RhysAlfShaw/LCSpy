from astropy.nddata import Cutout2D
import requests 

class cutout_2d:

    def __init__(self,RA,DEC,cutout_size=(28,28)):
        self.RA = RA
        self.DEC = DEC
        self.size = cutout_size
        # for testing
        self.mosaic_id = 'P000+23'
    
    def load_pointing(self):
        url_base = 'https://lofar-surveys.org/public/DR2/mosaics/'+str(self.mosaic_id)+'/mosaic-blanked.fits'
        responce = requests.get(url_base, stream=True)
        print(responce.content)
        #pass

    def find_pointing(self):
        pass

    def preform_cutout(self):
        pass

    def check_poitions_valid(self):
        pass
