import os
from sikuli import *  # NOQA
from common import WebApp


class Gsearch(WebApp):
    """
        The GSearch library for Sikuli cases.
        The component structure:
            <COMPONENT-NAME> = [
                [<COMPONENT-IMAGE-PLATFORM-FOO>, <OFFSET-X>, <OFFSET-Y>],
                [<COMPONENT-IMAGE-PLATFORM-BAR>, <OFFSET-X>, <OFFSET-Y>]
            ]
    """

    GSEARCH_IMAGE_HEADER = [
        [os.path.join('pics', 'gsearch_image_header.png'), 0, 0]
    ]

    GSEARCH_HOMEPAGE_BUTTONS = [
        [os.path.join('pics', 'gsearch_homepage_buttons.png'), 0, 0]
    ]

    GSEARCH_FOCUS_SEARCH_INPUTBOX = [
        [os.path.join('pics', 'gsearch_homepage_buttons.png'), -7, -71]
    ]

    def wait_gsearch_loaded(self, similarity=0.70):
        return self._wait_for_loaded(component=Gsearch.GSEARCH_HOMEPAGE_BUTTONS, similarity=similarity)

    def wait_gimage_loaded(self, similarity=0.70):
        return self._wait_for_loaded(component=Gsearch.GSEARCH_IMAGE_HEADER, similarity=similarity)

    def focus_search_inputbox(self):
        return self._click(action_name='Focus search inputbox',
                           component=Gsearch.GSEARCH_FOCUS_SEARCH_INPUTBOX)

    # click the image located in xth row and yth column (1 based)
    # for example, the very first image is (1,1).
    # this calculation is based on english version of google image search only
    def click_result_image(self, x, y):
        a = -120 + 280 * (x - 1)
        b = 275 + 200 * (y - 1)
        GSEARCH_CLICK_RESULT_IMAGE = [
            [os.path.join('pics', 'gsearch_image_header.png'), a, b]
        ]
        return self._click(action_name='Click result image',
                           component=GSEARCH_CLICK_RESULT_IMAGE)

    def hover_result_image(self, x, y):
        a = -120 + 280 * (x - 1)
        b = 275 + 200 * (y - 1)
        GSEARCH_HOVER_RESULT_IMAGE = [
            [os.path.join('pics', 'gsearch_image_header.png'), a, b]
        ]
        return self._click(action_name='Hover result image',
                           component=GSEARCH_HOVER_RESULT_IMAGE)
