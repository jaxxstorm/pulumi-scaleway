# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Token']


class Token(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 expires: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.

        Provides Tokens for scaleway API access. For additional details please refer to [API documentation](https://developer.scaleway.com/#tokens-tokens-post).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        karls_token = scaleway.Token("karlsToken",
            description="karls scaleway access: karl@company.com",
            expires=False)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Token description
        :param pulumi.Input[str] email: Scaleway account email. Defaults to registered account
        :param pulumi.Input[bool] expires: Define if the token should automatically expire or not
        :param pulumi.Input[str] password: Scaleway account password. Required for cross-account token management
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

            __props__['description'] = description
            __props__['email'] = email
            __props__['expires'] = expires
            __props__['password'] = password
            __props__['access_key'] = None
            __props__['creation_ip'] = None
            __props__['expiration_date'] = None
            __props__['secret_key'] = None
            __props__['user_id'] = None
        super(Token, __self__).__init__(
            'scaleway:index/token:Token',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key: Optional[pulumi.Input[str]] = None,
            creation_ip: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            expiration_date: Optional[pulumi.Input[str]] = None,
            expires: Optional[pulumi.Input[bool]] = None,
            password: Optional[pulumi.Input[str]] = None,
            secret_key: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'Token':
        """
        Get an existing Token resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: Token Access Key
        :param pulumi.Input[str] creation_ip: IP used to create the token
        :param pulumi.Input[str] description: Token description
        :param pulumi.Input[str] email: Scaleway account email. Defaults to registered account
        :param pulumi.Input[str] expiration_date: Expiration date of token, if expiration is requested
        :param pulumi.Input[bool] expires: Define if the token should automatically expire or not
        :param pulumi.Input[str] password: Scaleway account password. Required for cross-account token management
        :param pulumi.Input[str] secret_key: Token Secret Key
        :param pulumi.Input[str] user_id: The userid of the associated user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_key"] = access_key
        __props__["creation_ip"] = creation_ip
        __props__["description"] = description
        __props__["email"] = email
        __props__["expiration_date"] = expiration_date
        __props__["expires"] = expires
        __props__["password"] = password
        __props__["secret_key"] = secret_key
        __props__["user_id"] = user_id
        return Token(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[str]:
        """
        Token Access Key
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="creationIp")
    def creation_ip(self) -> pulumi.Output[str]:
        """
        IP used to create the token
        """
        return pulumi.get(self, "creation_ip")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Token description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Scaleway account email. Defaults to registered account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[str]:
        """
        Expiration date of token, if expiration is requested
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def expires(self) -> pulumi.Output[Optional[bool]]:
        """
        Define if the token should automatically expire or not
        """
        return pulumi.get(self, "expires")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Scaleway account password. Required for cross-account token management
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[str]:
        """
        Token Secret Key
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The userid of the associated user.
        """
        return pulumi.get(self, "user_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

