# coding: utf-8

"""
    Laserfiche API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>561590</p>  # noqa: E501

    OpenAPI spec version: 1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ParentEntryIdFileNameBody(object):
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
        'electronic_document': 'str',
        'request': 'PostEntryWithEdocMetadataRequest'
    }

    attribute_map = {
        'electronic_document': 'electronicDocument',
        'request': 'request'
    }

    def __init__(self, electronic_document=None, request=None):  # noqa: E501
        """ParentEntryIdFileNameBody - a model defined in Swagger"""  # noqa: E501
        self._electronic_document = None
        self._request = None
        self.discriminator = None
        if electronic_document is not None:
            self.electronic_document = electronic_document
        if request is not None:
            self.request = request

    @property
    def electronic_document(self):
        """Gets the electronic_document of this ParentEntryIdFileNameBody.  # noqa: E501

        The electronic document that will be uploaded.  # noqa: E501

        :return: The electronic_document of this ParentEntryIdFileNameBody.  # noqa: E501
        :rtype: str
        """
        return self._electronic_document

    @electronic_document.setter
    def electronic_document(self, electronic_document):
        """Sets the electronic_document of this ParentEntryIdFileNameBody.

        The electronic document that will be uploaded.  # noqa: E501

        :param electronic_document: The electronic_document of this ParentEntryIdFileNameBody.  # noqa: E501
        :type: str
        """

        self._electronic_document = electronic_document

    @property
    def request(self):
        """Gets the request of this ParentEntryIdFileNameBody.  # noqa: E501


        :return: The request of this ParentEntryIdFileNameBody.  # noqa: E501
        :rtype: PostEntryWithEdocMetadataRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this ParentEntryIdFileNameBody.


        :param request: The request of this ParentEntryIdFileNameBody.  # noqa: E501
        :type: PostEntryWithEdocMetadataRequest
        """

        self._request = request

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
        if issubclass(ParentEntryIdFileNameBody, dict):
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
        if not isinstance(other, ParentEntryIdFileNameBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other