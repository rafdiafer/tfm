import re
import sys

string = '84 /salud/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/facebook.png'
new_string = string.split('/',1)
print(new_string[1])
print(new_string)