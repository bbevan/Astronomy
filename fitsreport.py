import os
from astropy.io import fits
import fnmatch

a = os.walk('/home/brandon/Documents/a')

def report():
    for root, dir, files in a:
        for items in files:
            #for name in items:
            #fits_image_filename = fits.util.get_testdata_filepath(name)
                if fnmatch.fnmatch(items, "*.fits"):
                    name = os.path.join(root, items)
                    print(name)
                    hdul = fits.open(name)
                    print("Date:\t\t" + hdul[0].header['DATE'])
                    print("Filter:\t\t" + hdul[0].header['FILTER2'])
                    print("Object:\t\t" + hdul[0].header['OBJECT'])
                    print("Binning:\t" + hdul[1].header['CCDSUM'])
                    print("\n\n")
                    hdul.close()

#run report
report()
