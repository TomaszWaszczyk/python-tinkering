import bmp
from scipy import ndimage

# Przykład prostych operacji na grafice 2D traktowanej jako tablica z liczbami.
# Wymaga bibliotek numpy i scipy oraz obecności pliku tiger.bmp.
# Samo wczytywanie plików bmp jest realizowane przez dodatkowy moduł bmp.py - on z kolei
#   korzysta ze standardowego modułu struct do obsługi danych binarnych "podobnie jak to się robi w C".

# Każdy piksel to wartosci barw B G R jako liczby z przedziału od 0 do 255
pixels = bmp.read_bmp('tiger.bmp')

print(pixels.shape)

print('Jeden z punktów obrazka ma takie kolory:', pixels[200,300])

wycinek = pixels[100:, 190:430]
bmp.write_bmp('tiger1.bmp', wycinek)

# tutaj działa technika "broadcasting"
# kolory = pixels * [0, 0.5, 1]
kolory = pixels[:,:] * [1, 0, 1]
bmp.write_bmp('tiger2.bmp', kolory)

negatyw = 255 - pixels
bmp.write_bmp('tiger3.bmp', negatyw)

obrocony = ndimage.rotate(input=pixels, angle=45)
bmp.write_bmp('tiger4.bmp', obrocony)

rozmyty = ndimage.gaussian_filter(pixels, sigma=[3, 3, 0])
bmp.write_bmp('tiger5.bmp', rozmyty)

print('Gotowe')
