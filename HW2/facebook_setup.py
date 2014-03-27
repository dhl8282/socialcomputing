#!/usr/bin/env python
"""
Facebook api setup.

Date   : 2014 March 24
Author : donghun.lee7@gmail.com
"""

import facebook 

ACCESS_TOKEN='CAACEdEose0cBAJjHh9LZAEEzCZBcSZBnD3PSntwSgaFoWE3srOJFqp8gxlZArmBFEKvW9zU53JuAcwPZBr5xNZCEkG6GxZBOLejeZBfxhBK3N3dZAXGmxmP3HOtOurxPwBT56q5f67pK92ppPGZBa9YOIZBZANBF72zuNpM2gXu001tnq69NnM23XZAirs93XHAiRPZB2jZBEbRkJj5XAZDZD'

def connectFacebookApi():
    """Connect to facebook api."""

    return facebook.GraphAPI(ACCESS_TOKEN)
