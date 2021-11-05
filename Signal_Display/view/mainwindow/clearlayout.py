# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:50:06 2020

@author: Carlos Mateo Jurado Díaz
"""

def CLEARLAYOUT(layout):
    for i in reversed(range(layout.count())):
        layoutItem = layout.itemAt(i)
        if layoutItem.widget() is not None:
            widgetToRemove = layoutItem.widget()
            widgetToRemove.setParent(None)
            layout.removeWidget(widgetToRemove)
        else:
            layoutToRemove = layout.itemAt(i)
            CLEARLAYOUT(layoutToRemove)