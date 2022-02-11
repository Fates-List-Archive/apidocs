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

class BotReviews(object):
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
        'reviews': 'BotReviewList',
        'average_stars': 'float',
        'pager': 'BasePager'
    }

    attribute_map = {
        'reviews': 'reviews',
        'average_stars': 'average_stars',
        'pager': 'pager'
    }

    def __init__(self, reviews=None, average_stars=None, pager=None):  # noqa: E501
        """BotReviews - a model defined in Swagger"""  # noqa: E501
        self._reviews = None
        self._average_stars = None
        self._pager = None
        self.discriminator = None
        self.reviews = reviews
        self.average_stars = average_stars
        self.pager = pager

    @property
    def reviews(self):
        """Gets the reviews of this BotReviews.  # noqa: E501


        :return: The reviews of this BotReviews.  # noqa: E501
        :rtype: BotReviewList
        """
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        """Sets the reviews of this BotReviews.


        :param reviews: The reviews of this BotReviews.  # noqa: E501
        :type: BotReviewList
        """
        if reviews is None:
            raise ValueError("Invalid value for `reviews`, must not be `None`")  # noqa: E501

        self._reviews = reviews

    @property
    def average_stars(self):
        """Gets the average_stars of this BotReviews.  # noqa: E501


        :return: The average_stars of this BotReviews.  # noqa: E501
        :rtype: float
        """
        return self._average_stars

    @average_stars.setter
    def average_stars(self, average_stars):
        """Sets the average_stars of this BotReviews.


        :param average_stars: The average_stars of this BotReviews.  # noqa: E501
        :type: float
        """
        if average_stars is None:
            raise ValueError("Invalid value for `average_stars`, must not be `None`")  # noqa: E501

        self._average_stars = average_stars

    @property
    def pager(self):
        """Gets the pager of this BotReviews.  # noqa: E501


        :return: The pager of this BotReviews.  # noqa: E501
        :rtype: BasePager
        """
        return self._pager

    @pager.setter
    def pager(self, pager):
        """Sets the pager of this BotReviews.


        :param pager: The pager of this BotReviews.  # noqa: E501
        :type: BasePager
        """
        if pager is None:
            raise ValueError("Invalid value for `pager`, must not be `None`")  # noqa: E501

        self._pager = pager

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
        if issubclass(BotReviews, dict):
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
        if not isinstance(other, BotReviews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
