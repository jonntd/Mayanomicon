import math 
import maya.OpenMaya as OpenMaya


class PropertySettings(object):
    DEFAULT_FLOAT_VALUE = 0.0

    DEFAULT_INDEX_VALUE = 0

    ATTRIBUTE_NON_KEYABLE_STATUS = False

    ATTRIBUTE_KEYABLE_STATUS = True

    ATTRIBUTE_HIDDEN_STATUS = True

    ATTRIBUTE_NOT_HIDDEN_STATUS = False

    ATTRIBUTE_NON_STORABLE_STATUS = False

    ATTRIBUTE_STORABLE_STATUS = True

    ATTRIBUTE_EXPOSED_STATUS = True

    HIDE_MATRIX_ATTRIBUTES = True