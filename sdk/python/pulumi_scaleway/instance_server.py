# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['InstanceServer']


class InstanceServer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_volume_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cloud_init: Optional[pulumi.Input[str]] = None,
                 enable_dynamic_ip: Optional[pulumi.Input[bool]] = None,
                 enable_ipv6: Optional[pulumi.Input[bool]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 ip_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 placement_group_id: Optional[pulumi.Input[str]] = None,
                 root_volume: Optional[pulumi.Input[pulumi.InputType['InstanceServerRootVolumeArgs']]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_datas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceServerUserDataArgs']]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates and manages Scaleway Compute Instance servers. For more information, see [the documentation](https://developers.scaleway.com/en/products/instance/api/#servers-8bf7d7).

        ## Examples

        ### Basic

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        public_ip = scaleway.InstanceIP("publicIp")
        web = scaleway.InstanceServer("web",
            type="DEV1-S",
            image="ubuntu_focal",
            ip_id=public_ip.id)
        ```

        ### With additional volumes and tags

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        data = scaleway.InstanceVolume("data",
            size_in_gb=100,
            type="b_ssd")
        web = scaleway.InstanceServer("web",
            type="DEV1-L",
            image="ubuntu_focal",
            tags=[
                "hello",
                "public",
            ],
            root_volume={
                "deleteOnTermination": False,
            },
            additional_volume_ids=[data.id])
        ```

        ### With a reserved IP

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        ip = scaleway.InstanceIP("ip")
        web = scaleway.InstanceServer("web",
            type="DEV1-L",
            image="f974feac-abae-4365-b988-8ec7d1cec10d",
            tags=[
                "hello",
                "public",
            ],
            ip_id=ip.id)
        ```

        ### With security group

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        www = scaleway.InstanceSecurityGroup("www",
            inbound_default_policy="drop",
            outbound_default_policy="accept",
            inbound_rules=[
                {
                    "action": "accept",
                    "port": 22,
                    "ip": "212.47.225.64",
                },
                {
                    "action": "accept",
                    "port": 80,
                },
                {
                    "action": "accept",
                    "port": 443,
                },
            ],
            outbound_rules=[{
                "action": "drop",
                "ip_range": "10.20.0.0/24",
            }])
        web = scaleway.InstanceServer("web",
            type="DEV1-S",
            image="ubuntu_focal",
            security_group_id=www.id)
        ```

        ### With user data and cloud-init

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        web = scaleway.InstanceServer("web",
            type="DEV1-L",
            image="ubuntu_focal",
            tags=[
                "web",
                "public",
            ],
            user_datas=[
                {
                    "key": "plop",
                    "value": "world",
                },
                {
                    "key": "xavier",
                    "value": "niel",
                },
            ],
            cloud_init=(lambda path: open(path).read())(f"{path['module']}/cloud-init.yml"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_volume_ids: The [additional volumes](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39)
               attached to the server. Updates to this field will trigger a stop/start of the server.
        :param pulumi.Input[str] cloud_init: The cloud init script associated with this server. Updates to this field will trigger a stop/start of the server.
        :param pulumi.Input[bool] enable_dynamic_ip: If true a dynamic IP will be attached to the server.
        :param pulumi.Input[bool] enable_ipv6: Determines if IPv6 is enabled for the server.
        :param pulumi.Input[str] image: The UUID or the label of the base image used by the server. You can use [this endpoint](https://api-marketplace.scaleway.com/images?page=1&per_page=100)
               to find either the right `label` or the right local image `ID` for a given `type`.
        :param pulumi.Input[str] ip_id: = (Optional) The ID of the reserved IP that is attached to the server.
        :param pulumi.Input[str] name: The name of the server.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the server is associated with.
        :param pulumi.Input[str] placement_group_id: The [placement group](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) the server is attached to.
        :param pulumi.Input[pulumi.InputType['InstanceServerRootVolumeArgs']] root_volume: Root [volume](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39) attached to the server on creation.
        :param pulumi.Input[str] security_group_id: The [security group](https://developers.scaleway.com/en/products/instance/api/#security-groups-8d7f89) the server is attached to.
        :param pulumi.Input[str] state: The state of the server. Possible values are: `started`, `stopped` or `standby`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the server.
        :param pulumi.Input[str] type: The commercial type of the server.
               You find all the available types on the [pricing page](https://www.scaleway.com/en/pricing/).
               Updates to this field will recreate a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceServerUserDataArgs']]]] user_datas: The user data associated with the server.
        :param pulumi.Input[str] zone: `zone`) The zone in which the server should be created.
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

            __props__['additional_volume_ids'] = additional_volume_ids
            __props__['cloud_init'] = cloud_init
            __props__['enable_dynamic_ip'] = enable_dynamic_ip
            __props__['enable_ipv6'] = enable_ipv6
            if image is None:
                raise TypeError("Missing required property 'image'")
            __props__['image'] = image
            __props__['ip_id'] = ip_id
            __props__['name'] = name
            __props__['organization_id'] = organization_id
            __props__['placement_group_id'] = placement_group_id
            __props__['root_volume'] = root_volume
            __props__['security_group_id'] = security_group_id
            __props__['state'] = state
            __props__['tags'] = tags
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['user_datas'] = user_datas
            __props__['zone'] = zone
            __props__['boot_type'] = None
            __props__['ipv6_address'] = None
            __props__['ipv6_gateway'] = None
            __props__['ipv6_prefix_length'] = None
            __props__['placement_group_policy_respected'] = None
            __props__['private_ip'] = None
            __props__['public_ip'] = None
        super(InstanceServer, __self__).__init__(
            'scaleway:index/instanceServer:InstanceServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_volume_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            boot_type: Optional[pulumi.Input[str]] = None,
            cloud_init: Optional[pulumi.Input[str]] = None,
            enable_dynamic_ip: Optional[pulumi.Input[bool]] = None,
            enable_ipv6: Optional[pulumi.Input[bool]] = None,
            image: Optional[pulumi.Input[str]] = None,
            ip_id: Optional[pulumi.Input[str]] = None,
            ipv6_address: Optional[pulumi.Input[str]] = None,
            ipv6_gateway: Optional[pulumi.Input[str]] = None,
            ipv6_prefix_length: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            placement_group_id: Optional[pulumi.Input[str]] = None,
            placement_group_policy_respected: Optional[pulumi.Input[bool]] = None,
            private_ip: Optional[pulumi.Input[str]] = None,
            public_ip: Optional[pulumi.Input[str]] = None,
            root_volume: Optional[pulumi.Input[pulumi.InputType['InstanceServerRootVolumeArgs']]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            user_datas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceServerUserDataArgs']]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'InstanceServer':
        """
        Get an existing InstanceServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_volume_ids: The [additional volumes](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39)
               attached to the server. Updates to this field will trigger a stop/start of the server.
        :param pulumi.Input[str] boot_type: The boot Type of the server. Possible values are: `local`, `bootscript` or `rescue`.
        :param pulumi.Input[str] cloud_init: The cloud init script associated with this server. Updates to this field will trigger a stop/start of the server.
        :param pulumi.Input[bool] enable_dynamic_ip: If true a dynamic IP will be attached to the server.
        :param pulumi.Input[bool] enable_ipv6: Determines if IPv6 is enabled for the server.
        :param pulumi.Input[str] image: The UUID or the label of the base image used by the server. You can use [this endpoint](https://api-marketplace.scaleway.com/images?page=1&per_page=100)
               to find either the right `label` or the right local image `ID` for a given `type`.
        :param pulumi.Input[str] ip_id: = (Optional) The ID of the reserved IP that is attached to the server.
        :param pulumi.Input[str] ipv6_address: The default ipv6 address routed to the server. ( Only set when enable_ipv6 is set to true )
        :param pulumi.Input[str] ipv6_gateway: The ipv6 gateway address. ( Only set when enable_ipv6 is set to true )
        :param pulumi.Input[int] ipv6_prefix_length: The prefix length of the ipv6 subnet routed to the server. ( Only set when enable_ipv6 is set to true )
        :param pulumi.Input[str] name: The name of the server.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the server is associated with.
        :param pulumi.Input[str] placement_group_id: The [placement group](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) the server is attached to.
        :param pulumi.Input[bool] placement_group_policy_respected: True when the placement group policy is respected.
               - `root_volume`
        :param pulumi.Input[str] private_ip: The Scaleway internal IP address of the server.
        :param pulumi.Input[str] public_ip: The public IPv4 address of the server.
        :param pulumi.Input[pulumi.InputType['InstanceServerRootVolumeArgs']] root_volume: Root [volume](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39) attached to the server on creation.
        :param pulumi.Input[str] security_group_id: The [security group](https://developers.scaleway.com/en/products/instance/api/#security-groups-8d7f89) the server is attached to.
        :param pulumi.Input[str] state: The state of the server. Possible values are: `started`, `stopped` or `standby`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the server.
        :param pulumi.Input[str] type: The commercial type of the server.
               You find all the available types on the [pricing page](https://www.scaleway.com/en/pricing/).
               Updates to this field will recreate a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceServerUserDataArgs']]]] user_datas: The user data associated with the server.
        :param pulumi.Input[str] zone: `zone`) The zone in which the server should be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["additional_volume_ids"] = additional_volume_ids
        __props__["boot_type"] = boot_type
        __props__["cloud_init"] = cloud_init
        __props__["enable_dynamic_ip"] = enable_dynamic_ip
        __props__["enable_ipv6"] = enable_ipv6
        __props__["image"] = image
        __props__["ip_id"] = ip_id
        __props__["ipv6_address"] = ipv6_address
        __props__["ipv6_gateway"] = ipv6_gateway
        __props__["ipv6_prefix_length"] = ipv6_prefix_length
        __props__["name"] = name
        __props__["organization_id"] = organization_id
        __props__["placement_group_id"] = placement_group_id
        __props__["placement_group_policy_respected"] = placement_group_policy_respected
        __props__["private_ip"] = private_ip
        __props__["public_ip"] = public_ip
        __props__["root_volume"] = root_volume
        __props__["security_group_id"] = security_group_id
        __props__["state"] = state
        __props__["tags"] = tags
        __props__["type"] = type
        __props__["user_datas"] = user_datas
        __props__["zone"] = zone
        return InstanceServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalVolumeIds")
    def additional_volume_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The [additional volumes](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39)
        attached to the server. Updates to this field will trigger a stop/start of the server.
        """
        return pulumi.get(self, "additional_volume_ids")

    @property
    @pulumi.getter(name="bootType")
    def boot_type(self) -> pulumi.Output[str]:
        """
        The boot Type of the server. Possible values are: `local`, `bootscript` or `rescue`.
        """
        return pulumi.get(self, "boot_type")

    @property
    @pulumi.getter(name="cloudInit")
    def cloud_init(self) -> pulumi.Output[Optional[str]]:
        """
        The cloud init script associated with this server. Updates to this field will trigger a stop/start of the server.
        """
        return pulumi.get(self, "cloud_init")

    @property
    @pulumi.getter(name="enableDynamicIp")
    def enable_dynamic_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        If true a dynamic IP will be attached to the server.
        """
        return pulumi.get(self, "enable_dynamic_ip")

    @property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if IPv6 is enabled for the server.
        """
        return pulumi.get(self, "enable_ipv6")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[str]:
        """
        The UUID or the label of the base image used by the server. You can use [this endpoint](https://api-marketplace.scaleway.com/images?page=1&per_page=100)
        to find either the right `label` or the right local image `ID` for a given `type`.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="ipId")
    def ip_id(self) -> pulumi.Output[Optional[str]]:
        """
        = (Optional) The ID of the reserved IP that is attached to the server.
        """
        return pulumi.get(self, "ip_id")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[str]:
        """
        The default ipv6 address routed to the server. ( Only set when enable_ipv6 is set to true )
        """
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter(name="ipv6Gateway")
    def ipv6_gateway(self) -> pulumi.Output[str]:
        """
        The ipv6 gateway address. ( Only set when enable_ipv6 is set to true )
        """
        return pulumi.get(self, "ipv6_gateway")

    @property
    @pulumi.getter(name="ipv6PrefixLength")
    def ipv6_prefix_length(self) -> pulumi.Output[int]:
        """
        The prefix length of the ipv6 subnet routed to the server. ( Only set when enable_ipv6 is set to true )
        """
        return pulumi.get(self, "ipv6_prefix_length")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        `organization_id`) The ID of the organization the server is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The [placement group](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) the server is attached to.
        """
        return pulumi.get(self, "placement_group_id")

    @property
    @pulumi.getter(name="placementGroupPolicyRespected")
    def placement_group_policy_respected(self) -> pulumi.Output[bool]:
        """
        True when the placement group policy is respected.
        - `root_volume`
        """
        return pulumi.get(self, "placement_group_policy_respected")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[str]:
        """
        The Scaleway internal IP address of the server.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        """
        The public IPv4 address of the server.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="rootVolume")
    def root_volume(self) -> pulumi.Output['outputs.InstanceServerRootVolume']:
        """
        Root [volume](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39) attached to the server on creation.
        """
        return pulumi.get(self, "root_volume")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[str]:
        """
        The [security group](https://developers.scaleway.com/en/products/instance/api/#security-groups-8d7f89) the server is attached to.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        The state of the server. Possible values are: `started`, `stopped` or `standby`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with the server.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The commercial type of the server.
        You find all the available types on the [pricing page](https://www.scaleway.com/en/pricing/).
        Updates to this field will recreate a new resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userDatas")
    def user_datas(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceServerUserData']]]:
        """
        The user data associated with the server.
        """
        return pulumi.get(self, "user_datas")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        `zone`) The zone in which the server should be created.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

