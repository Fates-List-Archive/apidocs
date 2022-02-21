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

class BotReview(object):
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
        'id': 'str',
        'reply': 'bool',
        'user_id': 'str',
        'star_rating': 'float',
        'review': 'str',
        'review_upvotes': 'list[object]',
        'review_downvotes': 'list[object]',
        'flagged': 'bool',
        'epoch': 'list[object]',
        'time_past': 'str',
        'user': 'BaseUser',
        'replies': 'AllOfBotReviewReplies'
    }

    attribute_map = {
        'id': 'id',
        'reply': 'reply',
        'user_id': 'user_id',
        'star_rating': 'star_rating',
        'review': 'review',
        'review_upvotes': 'review_upvotes',
        'review_downvotes': 'review_downvotes',
        'flagged': 'flagged',
        'epoch': 'epoch',
        'time_past': 'time_past',
        'user': 'user',
        'replies': 'replies'
    }

    def __init__(self, id=None, reply=None, user_id=None, star_rating=None, review=None, review_upvotes=None, review_downvotes=None, flagged=None, epoch=None, time_past=None, user=None, replies=None):  # noqa: E501
        """BotReview - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._reply = None
        self._user_id = None
        self._star_rating = None
        self._review = None
        self._review_upvotes = None
        self._review_downvotes = None
        self._flagged = None
        self._epoch = None
        self._time_past = None
        self._user = None
        self._replies = None
        self.discriminator = None
        self.id = id
        self.reply = reply
        self.user_id = user_id
        self.star_rating = star_rating
        self.review = review
        self.review_upvotes = review_upvotes
        self.review_downvotes = review_downvotes
        self.flagged = flagged
        self.epoch = epoch
        self.time_past = time_past
        self.user = user
        if replies is not None:
            self.replies = replies

    @property
    def id(self):
        """Gets the id of this BotReview.  # noqa: E501


        :return: The id of this BotReview.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BotReview.


        :param id: The id of this BotReview.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reply(self):
        """Gets the reply of this BotReview.  # noqa: E501


        :return: The reply of this BotReview.  # noqa: E501
        :rtype: bool
        """
        return self._reply

    @reply.setter
    def reply(self, reply):
        """Sets the reply of this BotReview.


        :param reply: The reply of this BotReview.  # noqa: E501
        :type: bool
        """
        if reply is None:
            raise ValueError("Invalid value for `reply`, must not be `None`")  # noqa: E501

        self._reply = reply

    @property
    def user_id(self):
        """Gets the user_id of this BotReview.  # noqa: E501


        :return: The user_id of this BotReview.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BotReview.


        :param user_id: The user_id of this BotReview.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def star_rating(self):
        """Gets the star_rating of this BotReview.  # noqa: E501


        :return: The star_rating of this BotReview.  # noqa: E501
        :rtype: float
        """
        return self._star_rating

    @star_rating.setter
    def star_rating(self, star_rating):
        """Sets the star_rating of this BotReview.


        :param star_rating: The star_rating of this BotReview.  # noqa: E501
        :type: float
        """
        if star_rating is None:
            raise ValueError("Invalid value for `star_rating`, must not be `None`")  # noqa: E501

        self._star_rating = star_rating

    @property
    def review(self):
        """Gets the review of this BotReview.  # noqa: E501


        :return: The review of this BotReview.  # noqa: E501
        :rtype: str
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this BotReview.


        :param review: The review of this BotReview.  # noqa: E501
        :type: str
        """
        if review is None:
            raise ValueError("Invalid value for `review`, must not be `None`")  # noqa: E501

        self._review = review

    @property
    def review_upvotes(self):
        """Gets the review_upvotes of this BotReview.  # noqa: E501


        :return: The review_upvotes of this BotReview.  # noqa: E501
        :rtype: list[object]
        """
        return self._review_upvotes

    @review_upvotes.setter
    def review_upvotes(self, review_upvotes):
        """Sets the review_upvotes of this BotReview.


        :param review_upvotes: The review_upvotes of this BotReview.  # noqa: E501
        :type: list[object]
        """
        if review_upvotes is None:
            raise ValueError("Invalid value for `review_upvotes`, must not be `None`")  # noqa: E501

        self._review_upvotes = review_upvotes

    @property
    def review_downvotes(self):
        """Gets the review_downvotes of this BotReview.  # noqa: E501


        :return: The review_downvotes of this BotReview.  # noqa: E501
        :rtype: list[object]
        """
        return self._review_downvotes

    @review_downvotes.setter
    def review_downvotes(self, review_downvotes):
        """Sets the review_downvotes of this BotReview.


        :param review_downvotes: The review_downvotes of this BotReview.  # noqa: E501
        :type: list[object]
        """
        if review_downvotes is None:
            raise ValueError("Invalid value for `review_downvotes`, must not be `None`")  # noqa: E501

        self._review_downvotes = review_downvotes

    @property
    def flagged(self):
        """Gets the flagged of this BotReview.  # noqa: E501


        :return: The flagged of this BotReview.  # noqa: E501
        :rtype: bool
        """
        return self._flagged

    @flagged.setter
    def flagged(self, flagged):
        """Sets the flagged of this BotReview.


        :param flagged: The flagged of this BotReview.  # noqa: E501
        :type: bool
        """
        if flagged is None:
            raise ValueError("Invalid value for `flagged`, must not be `None`")  # noqa: E501

        self._flagged = flagged

    @property
    def epoch(self):
        """Gets the epoch of this BotReview.  # noqa: E501


        :return: The epoch of this BotReview.  # noqa: E501
        :rtype: list[object]
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this BotReview.


        :param epoch: The epoch of this BotReview.  # noqa: E501
        :type: list[object]
        """
        if epoch is None:
            raise ValueError("Invalid value for `epoch`, must not be `None`")  # noqa: E501

        self._epoch = epoch

    @property
    def time_past(self):
        """Gets the time_past of this BotReview.  # noqa: E501


        :return: The time_past of this BotReview.  # noqa: E501
        :rtype: str
        """
        return self._time_past

    @time_past.setter
    def time_past(self, time_past):
        """Sets the time_past of this BotReview.


        :param time_past: The time_past of this BotReview.  # noqa: E501
        :type: str
        """
        if time_past is None:
            raise ValueError("Invalid value for `time_past`, must not be `None`")  # noqa: E501

        self._time_past = time_past

    @property
    def user(self):
        """Gets the user of this BotReview.  # noqa: E501


        :return: The user of this BotReview.  # noqa: E501
        :rtype: BaseUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BotReview.


        :param user: The user of this BotReview.  # noqa: E501
        :type: BaseUser
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def replies(self):
        """Gets the replies of this BotReview.  # noqa: E501


        :return: The replies of this BotReview.  # noqa: E501
        :rtype: AllOfBotReviewReplies
        """
        return self._replies

    @replies.setter
    def replies(self, replies):
        """Sets the replies of this BotReview.


        :param replies: The replies of this BotReview.  # noqa: E501
        :type: AllOfBotReviewReplies
        """

        self._replies = replies

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
        if issubclass(BotReview, dict):
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
        if not isinstance(other, BotReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other