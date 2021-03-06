# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['UserData']


class UserData(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
        Please use `InstanceServer` instead.

        Provides user data for servers.
        For additional details please refer to [API documentation](https://developer.scaleway.com/#user-data).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        base = scaleway.Server("base",
            image="5faef9cd-ea9b-4a63-9171-9e26bec03dbc",
            type="C1",
            state="stopped")
        gcp = scaleway.UserData("gcp",
            server=base.id,
            key="gcp_username",
            value="supersecret")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The key of the user data object
        :param pulumi.Input[str] server: ID of server to associate the user data with
        :param pulumi.Input[str] value: The value of the user data object
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if key is None:
                raise TypeError("Missing required property 'key'")
            __props__['key'] = key
            if server is None:
                raise TypeError("Missing required property 'server'")
            __props__['server'] = server
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
        super(UserData, __self__).__init__(
            'scaleway:index/userData:UserData',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key: Optional[pulumi.Input[str]] = None,
            server: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'UserData':
        """
        Get an existing UserData resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The key of the user data object
        :param pulumi.Input[str] server: ID of server to associate the user data with
        :param pulumi.Input[str] value: The value of the user data object
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["key"] = key
        __props__["server"] = server
        __props__["value"] = value
        return UserData(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The key of the user data object
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def server(self) -> pulumi.Output[str]:
        """
        ID of server to associate the user data with
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the user data object
        """
        return pulumi.get(self, "value")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

