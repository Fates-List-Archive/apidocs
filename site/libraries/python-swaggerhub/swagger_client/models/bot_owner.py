# coding: utf-8

"""
    Fates List

                 Current API: v2 beta 3             Default API: v2             API URL: https://api.fateslist.xyz             API Docs: https://apidocs.fateslist.xyz             Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen           # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BotOwner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user': 'BaseUser',
        'main': 'bool'
    }

    attribute_map = {
        'user': 'user',
        'main': 'main'
    }

    def __init__(self, user=None, main=None):  # noqa: E501
        """BotOwner - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._main = None
        self.discriminator = None
        self.user = user
        self.main = main

    @property
    def user(self):
        """Gets the user of this BotOwner.  # noqa: E501


        :return: The user of this BotOwner.  # noqa: E501
        :rtype: BaseUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BotOwner.


        :param user: The user of this BotOwner.  # noqa: E501
        :type: BaseUser
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def main(self):
        """Gets the main of this BotOwner.  # noqa: E501


        :return: The main of this BotOwner.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this BotOwner.


        :param main: The main of this BotOwner.  # noqa: E501
        :type: bool
        """
        if main is None:
            raise ValueError("Invalid value for `main`, must not be `None`")  # noqa: E501

        self._main = main

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BotOwner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BotOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
