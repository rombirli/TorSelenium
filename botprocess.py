from sys import argv

from config import BOT_FUNCTION
from main import create_browser

if len(argv) == 2 :
    i = int(argv[1])
    try:
        b = create_browser(i)
        BOT_FUNCTION(b)
        b.quit()
    except:
        print(f'A problem happened with botprocess {i}')
else:
    print(f'Error launching a botprocess')
