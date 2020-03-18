# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class SparkSessionOperations(object):
    """SparkSessionOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def list(
            self, workspace_name, spark_pool_name, from_parameter=None, size=None, detailed=None, custom_headers=None, raw=False, **operation_config):
        """List all spark sessions which are running under a particular spark
        pool.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param from_parameter: Optional param specifying which index the list
         should begin from.
        :type from_parameter: int
        :param size: Optional param specifying the size of the returned list.
         By default it is 20 and that is the maximum.
        :type size: int
        :param detailed: Optional query param specifying whether detailed
         response is returned beyond plain livy.
        :type detailed: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExtendedLivyListSessionResponse or ClientRawResponse if
         raw=true
        :rtype: ~azure.synapse.models.ExtendedLivyListSessionResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_parameter is not None:
            query_parameters['from'] = self._serialize.query("from_parameter", from_parameter, 'int')
        if size is not None:
            query_parameters['size'] = self._serialize.query("size", size, 'int')
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ExtendedLivyListSessionResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions'}

    def create(
            self, workspace_name, spark_pool_name, livy_request, detailed=None, custom_headers=None, raw=False, **operation_config):
        """Create new spark session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param livy_request: Livy compatible batch job request payload.
        :type livy_request: ~azure.synapse.models.ExtendedLivySessionRequest
        :param detailed: Optional query param specifying whether detailed
         response is returned beyond plain livy.
        :type detailed: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExtendedLivySessionResponse or ClientRawResponse if raw=true
        :rtype: ~azure.synapse.models.ExtendedLivySessionResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(livy_request, 'ExtendedLivySessionRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ExtendedLivySessionResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions'}

    def get(
            self, workspace_name, spark_pool_name, session_id, detailed=None, custom_headers=None, raw=False, **operation_config):
        """Gets a single spark session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param detailed: Optional query param specifying whether detailed
         response is returned beyond plain livy.
        :type detailed: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExtendedLivySessionResponse or ClientRawResponse if raw=true
        :rtype: ~azure.synapse.models.ExtendedLivySessionResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ExtendedLivySessionResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}'}

    def delete(
            self, workspace_name, spark_pool_name, session_id, custom_headers=None, raw=False, **operation_config):
        """Cancels a running spark session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand"
         targets the ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}'}

    def reset_timeout(
            self, workspace_name, spark_pool_name, session_id, custom_headers=None, raw=False, **operation_config):
        """Sends a keep alive call to the current session to reset the session
        timeout.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand"
         targets the ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.reset_timeout.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    reset_timeout.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/reset-timeout'}

    def list_statements(
            self, workspace_name, spark_pool_name, session_id, custom_headers=None, raw=False, **operation_config):
        """Gets a list of statements within a spark session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LivyStatementsResponseBody or ClientRawResponse if raw=true
        :rtype: ~azure.synapse.models.LivyStatementsResponseBody or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_statements.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LivyStatementsResponseBody', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_statements.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements'}

    def create_statement(
            self, workspace_name, spark_pool_name, session_id, livy_request, custom_headers=None, raw=False, **operation_config):
        """Create statement within a spark session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param livy_request: Livy compatible batch job request payload.
        :type livy_request: ~azure.synapse.models.LivyStatementRequestBody
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LivyStatementResponseBody or ClientRawResponse if raw=true
        :rtype: ~azure.synapse.models.LivyStatementResponseBody or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_statement.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(livy_request, 'LivyStatementRequestBody')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LivyStatementResponseBody', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_statement.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements'}

    def get_statement(
            self, workspace_name, spark_pool_name, session_id, statement_id, custom_headers=None, raw=False, **operation_config):
        """Gets a single statement within a spark session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param statement_id: Identifier for the statement.
        :type statement_id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LivyStatementResponseBody or ClientRawResponse if raw=true
        :rtype: ~azure.synapse.models.LivyStatementResponseBody or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_statement.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
            'statementId': self._serialize.url("statement_id", statement_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LivyStatementResponseBody', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_statement.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements/{statementId}'}

    def delete_statement(
            self, workspace_name, spark_pool_name, session_id, statement_id, custom_headers=None, raw=False, **operation_config):
        """Kill a statement within a session.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param spark_pool_name: Name of the spark pool. "ondemand" targets the
         ondemand pool.
        :type spark_pool_name: str
        :param session_id: Identifier for the session.
        :type session_id: int
        :param statement_id: Identifier for the statement.
        :type statement_id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LivyStatementCancellationResponse or ClientRawResponse if
         raw=true
        :rtype: ~azure.synapse.models.LivyStatementCancellationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_statement.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self.config.livy_api_version", self.config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("spark_pool_name", spark_pool_name, 'str'),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
            'statementId': self._serialize.url("statement_id", statement_id, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LivyStatementCancellationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_statement.metadata = {'url': '/livyApi/versions/{livyApiVersion}/sparkPools/{sparkPoolName}/sessions/{sessionId}/statements/{statementId}/cancel'}