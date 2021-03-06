# coding: utf-8

"""
    Laserfiche API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>650780</p>  # noqa: E501

    OpenAPI spec version: 1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from laserfiche_api.api_client import ApiClient


class FieldDefinitionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_field_definition_by_id(self, repo_id, field_definition_id, **kwargs):  # noqa: E501
        """get_field_definition_by_id  # noqa: E501

        - Returns a single field definition associated with the specified ID.  - Useful when a route provides a minimal amount of details and more information about the specific field definition is needed. - Allowed OData query options: Select  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_definition_by_id(repo_id, field_definition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param int field_definition_id: The requested field definition ID. (required)
        :param str select: Limits the properties returned in the result.
        :return: WFieldInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_field_definition_by_id_with_http_info(repo_id, field_definition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_field_definition_by_id_with_http_info(repo_id, field_definition_id, **kwargs)  # noqa: E501
            return data

    def get_field_definition_by_id_with_http_info(self, repo_id, field_definition_id, **kwargs):  # noqa: E501
        """get_field_definition_by_id  # noqa: E501

        - Returns a single field definition associated with the specified ID.  - Useful when a route provides a minimal amount of details and more information about the specific field definition is needed. - Allowed OData query options: Select  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_definition_by_id_with_http_info(repo_id, field_definition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param int field_definition_id: The requested field definition ID. (required)
        :param str select: Limits the properties returned in the result.
        :return: WFieldInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'field_definition_id', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_field_definition_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `get_field_definition_by_id`")  # noqa: E501
        # verify the required parameter 'field_definition_id' is set
        if ('field_definition_id' not in params or
                params['field_definition_id'] is None):
            raise ValueError("Missing the required parameter `field_definition_id` when calling `get_field_definition_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501
        if 'field_definition_id' in params:
            path_params['fieldDefinitionId'] = params['field_definition_id']  # noqa: E501

        query_params = []
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1-alpha/Repositories/{repoId}/FieldDefinitions/{fieldDefinitionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WFieldInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_field_definitions(self, repo_id, **kwargs):  # noqa: E501
        """get_field_definitions  # noqa: E501

        - Returns a paged listing of field definitions available in the specified repository. - Useful when trying to find a list of all field definitions available, rather than only those assigned to a specific entry/template. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_definitions(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str prefer: An optional OData header. Can be used to set the maximum page size using odata.maxpagesize.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIListOfWFieldInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_field_definitions_with_http_info(repo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_field_definitions_with_http_info(repo_id, **kwargs)  # noqa: E501
            return data

    def get_field_definitions_with_http_info(self, repo_id, **kwargs):  # noqa: E501
        """get_field_definitions  # noqa: E501

        - Returns a paged listing of field definitions available in the specified repository. - Useful when trying to find a list of all field definitions available, rather than only those assigned to a specific entry/template. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_definitions_with_http_info(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: The requested repository ID. (required)
        :param str prefer: An optional OData header. Can be used to set the maximum page size using odata.maxpagesize.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIListOfWFieldInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id', 'prefer', 'select', 'orderby', 'top', 'skip', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_field_definitions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `get_field_definitions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501

        query_params = []
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('$orderby', params['orderby']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501
        if 'count' in params:
            query_params.append(('$count', params['count']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/v1-alpha/Repositories/{repoId}/FieldDefinitions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIListOfWFieldInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
