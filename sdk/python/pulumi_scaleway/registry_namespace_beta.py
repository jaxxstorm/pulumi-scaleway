# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['RegistryNamespaceBeta']


class RegistryNamespaceBeta(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates and manages Scaleway Container Registry. For more information see [the documentation](https://developers.scaleway.com/en/products/registry/api/).

        ## Examples

        ### Basic

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        main = scaleway.RegistryNamespaceBeta("main",
            description="Main container registry",
            is_public=False)
        ```

        ## Attibutes Reference

        In addition to all arguments above, the following attibutes are exported:

        - `id` - The ID of the namespace
        - `endpoint` - Endpoint reachable by docker.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the container registry namespace.
        :param pulumi.Input[bool] is_public: Whether or not the registry images stored in the namespace should be downloadable publicly (docker pull).
        :param pulumi.Input[str] name: The unique name of the container registry namespace.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the registry is associated with.
        :param pulumi.Input[str] region: `region`). The region in which the container registry namespace should be created.
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
            __props__['is_public'] = is_public
            __props__['name'] = name
            __props__['organization_id'] = organization_id
            __props__['region'] = region
            __props__['endpoint'] = None
        super(RegistryNamespaceBeta, __self__).__init__(
            'scaleway:index/registryNamespaceBeta:RegistryNamespaceBeta',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            is_public: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'RegistryNamespaceBeta':
        """
        Get an existing RegistryNamespaceBeta resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the container registry namespace.
        :param pulumi.Input[str] endpoint: The endpoint reachable by docker
        :param pulumi.Input[bool] is_public: Whether or not the registry images stored in the namespace should be downloadable publicly (docker pull).
        :param pulumi.Input[str] name: The unique name of the container registry namespace.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the registry is associated with.
        :param pulumi.Input[str] region: `region`). The region in which the container registry namespace should be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["endpoint"] = endpoint
        __props__["is_public"] = is_public
        __props__["name"] = name
        __props__["organization_id"] = organization_id
        __props__["region"] = region
        return RegistryNamespaceBeta(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the container registry namespace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint reachable by docker
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not the registry images stored in the namespace should be downloadable publicly (docker pull).
        """
        return pulumi.get(self, "is_public")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique name of the container registry namespace.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        `organization_id`) The ID of the organization the registry is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        `region`). The region in which the container registry namespace should be created.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

