# The following copyright and license apply to this file (utils.py).
#
# Copyright (c) 2022 John Claypool
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHOR OR COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING
# FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import re
from django.conf import settings

def convert_string_to_variable_name(string_to_convert: str):
    """Mutate a string into an acceptable python variable.

    Does not return a variable; rather, removes disallowed characters from the
    input string and returns a string. Allowed characters are a-z, 0-9, and _.
    """

    # Take the string, switch to lowercase, and replace any spaces with
    # underscores.
    string_to_convert = string_to_convert.lower().replace(" ","_")

    # Remove any characters that aren't lowercase a-z, 0-9, or underscores.
    string_to_convert = re.sub('[^a-z0-9_]',"",string_to_convert)

    # Python variables can't start with a number, so if the first character is a
    # number, add an underscore to the beginning.
    if string_to_convert[:1].isdigit():
        string_to_convert = "_" + string_to_convert

    return string_to_convert

def get_sentinel_user(username='deleted'):
    return settings.AUTH_USER_MODEL.objects.get_or_create(username=username)[0]
