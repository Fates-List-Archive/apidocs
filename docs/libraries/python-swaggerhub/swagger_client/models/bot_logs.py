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

class BotLogs(object):
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
        'bot_id': 'str',
        'action': 'int',
        'action_time': 'datetime',
        'context': 'object'
    }

    attribute_map = {
        'bot_id': 'bot_id',
        'action': 'action',
        'action_time': 'action_time',
        'context': 'context'
    }

    def __init__(self, bot_id=None, action=None, action_time=None, context=None):  # noqa: E501
        """BotLogs - a model defined in Swagger"""  # noqa: E501
        self._bot_id = None
        self._action = None
        self._action_time = None
        self._context = None
        self.discriminator = None
        self.bot_id = bot_id
        self.action = action
        self.action_time = action_time
        if context is not None:
            self.context = context

    @property
    def bot_id(self):
        """Gets the bot_id of this BotLogs.  # noqa: E501


        :return: The bot_id of this BotLogs.  # noqa: E501
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """Sets the bot_id of this BotLogs.


        :param bot_id: The bot_id of this BotLogs.  # noqa: E501
        :type: str
        """
        if bot_id is None:
            raise ValueError("Invalid value for `bot_id`, must not be `None`")  # noqa: E501

        self._bot_id = bot_id

    @property
    def action(self):
        """Gets the action of this BotLogs.  # noqa: E501


        :return: The action of this BotLogs.  # noqa: E501
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BotLogs.


        :param action: The action of this BotLogs.  # noqa: E501
        :type: int
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def action_time(self):
        """Gets the action_time of this BotLogs.  # noqa: E501


        :return: The action_time of this BotLogs.  # noqa: E501
        :rtype: datetime
        """
        return self._action_time

    @action_time.setter
    def action_time(self, action_time):
        """Sets the action_time of this BotLogs.


        :param action_time: The action_time of this BotLogs.  # noqa: E501
        :type: datetime
        """
        if action_time is None:
            raise ValueError("Invalid value for `action_time`, must not be `None`")  # noqa: E501

        self._action_time = action_time

    @property
    def context(self):
        """Gets the context of this BotLogs.  # noqa: E501


        :return: The context of this BotLogs.  # noqa: E501
        :rtype: object
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this BotLogs.


        :param context: The context of this BotLogs.  # noqa: E501
        :type: object
        """

        self._context = context

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
        if issubclass(BotLogs, dict):
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
        if not isinstance(other, BotLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other