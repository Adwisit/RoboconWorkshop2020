import pyautogui
import pyperclip
pyautogui.FAILSAFE = False
"""Example library in Robot Framework format.

- Formatting with *bold* and _italic_.
- URLs like http://example.com are turned to links.
- Custom links like [http://robotframework.org|Robot Framework] are supported.
- Linking to `My Keyword` works.
"""

def get_location(image):
    '''
    Returns the location of an image on the screen. Returns None if not found.
    
    Returns a dictionary containing the location of the top left corner of the
    image searched and the width and height of the image.
    
    {'left': x, 'top': y, 'width': w, 'height': h}
    '''
    location = pyautogui.locateOnScreen(image)
    location = {'left': location[0], 'top': location[1],
                'width': location[2], 'height': location[3]}
    return location

def center(coords):
    '''Returns the center coordinates of an image location'''
    return (coords['left'] + int(coords['width'] / 2), coords['top'] + int(coords['height'] / 2))

def clip_get():
    '''Gets the value in the clipboard'''
    return pyperclip.paste()

def clip_put(value):
    '''Puts a value in the clipboard'''
    return pyperclip.copy(value)

def click(x, y, button='left'):
    '''Does a mouse click on the X and Y coordinates'''
    pyautogui.click(x=int(x), y=int(y), button=button)

def right_click(x, y):
    '''Does a right mouse click on the X and Y coordinates'''
    click(x=x, y=y, button='right')

def double_click(x, y):
    '''Does a double mouse click on the X and Y coordinates'''
    pyautogui.doubleClick(x, y)

def mouse_move(x, y):
    '''Moves the mouse to the X and Y coordinates'''
    pyautogui.moveTo(x, y)

def mouse_down(button='left'):
    '''Presses down the mouse button (default left)'''
    pyautogui.mouseDown(button=button)

def mouse_up(button='left'):
    '''Releases the mouse button (default left)'''
    pyautogui.mouseUp(button=button)

def input_text(text):
    '''Writes the text submitted'''
    pyautogui.typewrite(text)

def press_special_key(key):
    '''Presses a special key'''
    pyautogui.press(key)

def key_down(key):
    '''Presses down a key'''
    pyautogui.keyDown(key)

def key_up(key):
    '''Releases a key'''
    pyautogui.keyUp(key)
