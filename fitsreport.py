import os
from astropy.io import fits
import fnmatch
from pathlib import Path

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


# Return a list of fits files in all subdirectories

def fitslist():
    p = Path('.') #work in current directory

    #[x for x in p.iterdir() if x.is_dir()]

    return list(p.glob('**/*.fits'))
#end

# Print the fits list
def fitsprint(list):
    
    for x in list:
        print x

#end

# Return a list containing a fits filename and certain header info
def limheaderinfo(fitsfile):
    hdul = fits.open(fitsfile)

    a = [hdul[0].header['DATE'], hdul[0].header['FILTER2'], hdul[0].header['OBJECT'], hdul[1].header['CCDSUM']]

    hdul.close()

    return a

    

#end

# Print out header info for all fits files in a tree
def printlimheaderinfo():
    
    for x in fitslist():
        print x
        for y in limheaderinfo(x):
            print y
        print("\n")

#end


#Main Section for testing.

printlimheaderinfo()


