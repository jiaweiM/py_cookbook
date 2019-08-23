# -*- coding: utf-8 -*-
'''
The text is bound by a box. This box is used to relatively align the text to the coordinates
passed to pyplot.text(). Using the verticalalignment and horizontalalignment
parameters (respective shortcut equivalents are va and ha), we can control how the alignment
is done.

The vertical alignment options are as follows:
 'center': This is relative to the center of the textbox
 'top': This is relative to the upper side of the textbox
 'bottom': This is relative to the lower side of the textbox
 'baseline': This is relative to the text's baseline

The horizontal alignment options are as follows:
 'center': This is relative to the center of the textbox
 'left': This is relative to the left side of the textbox
 'right': This is relative to the right-hand side of the textbox

The pyplot.text() function supports a bbox parameter that takes a dictionary as the
input. This dictionary defines the various settings for the text box.

'''

import test_numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
box = {
    'facecolor': '.75',
    'edgecolor': 'k',
    'boxstyle': 'round'
}
plt.text(-0.5, -0.20, 'Brackmard minimum', bbox=box)
plt.plot(X, Y, c='k')
plt.show()
