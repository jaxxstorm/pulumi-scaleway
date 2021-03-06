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

__all__ = ['InstanceSecurityGroup']


class InstanceSecurityGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_rules: Optional[pulumi.Input[bool]] = None,
                 inbound_default_policy: Optional[pulumi.Input[str]] = None,
                 inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 outbound_default_policy: Optional[pulumi.Input[str]] = None,
                 outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]]] = None,
                 stateful: Optional[pulumi.Input[bool]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a InstanceSecurityGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the security group.
        :param pulumi.Input[bool] external_rules: A boolean to specify whether to use instance_security_group_rules. If `external_rules` is set to `true`, `inbound_rule` and `outbound_rule` can not be set directly in the security group.
        :param pulumi.Input[str] inbound_default_policy: The default policy on incoming traffic. Possible values are: `accept` or `drop`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]] inbound_rules: A list of inbound rule to add to the security group. (Structure is documented below.)
        :param pulumi.Input[str] name: The name of the security group.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the project the security group is associated with.
        :param pulumi.Input[str] outbound_default_policy: The default policy on outgoing traffic. Possible values are: `accept` or `drop`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]] outbound_rules: A list of outbound rule to add to the security group. (Structure is documented below.)
        :param pulumi.Input[bool] stateful: A boolean to specify whether the security group should be stateful or not.
        :param pulumi.Input[str] zone: `zone`) The zone in which the security group should be created.
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
            __props__['external_rules'] = external_rules
            __props__['inbound_default_policy'] = inbound_default_policy
            __props__['inbound_rules'] = inbound_rules
            __props__['name'] = name
            __props__['organization_id'] = organization_id
            __props__['outbound_default_policy'] = outbound_default_policy
            __props__['outbound_rules'] = outbound_rules
            __props__['stateful'] = stateful
            __props__['zone'] = zone
        super(InstanceSecurityGroup, __self__).__init__(
            'scaleway:index/instanceSecurityGroup:InstanceSecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            external_rules: Optional[pulumi.Input[bool]] = None,
            inbound_default_policy: Optional[pulumi.Input[str]] = None,
            inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            outbound_default_policy: Optional[pulumi.Input[str]] = None,
            outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]]] = None,
            stateful: Optional[pulumi.Input[bool]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'InstanceSecurityGroup':
        """
        Get an existing InstanceSecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the security group.
        :param pulumi.Input[bool] external_rules: A boolean to specify whether to use instance_security_group_rules. If `external_rules` is set to `true`, `inbound_rule` and `outbound_rule` can not be set directly in the security group.
        :param pulumi.Input[str] inbound_default_policy: The default policy on incoming traffic. Possible values are: `accept` or `drop`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]] inbound_rules: A list of inbound rule to add to the security group. (Structure is documented below.)
        :param pulumi.Input[str] name: The name of the security group.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the project the security group is associated with.
        :param pulumi.Input[str] outbound_default_policy: The default policy on outgoing traffic. Possible values are: `accept` or `drop`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]] outbound_rules: A list of outbound rule to add to the security group. (Structure is documented below.)
        :param pulumi.Input[bool] stateful: A boolean to specify whether the security group should be stateful or not.
        :param pulumi.Input[str] zone: `zone`) The zone in which the security group should be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["external_rules"] = external_rules
        __props__["inbound_default_policy"] = inbound_default_policy
        __props__["inbound_rules"] = inbound_rules
        __props__["name"] = name
        __props__["organization_id"] = organization_id
        __props__["outbound_default_policy"] = outbound_default_policy
        __props__["outbound_rules"] = outbound_rules
        __props__["stateful"] = stateful
        __props__["zone"] = zone
        return InstanceSecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the security group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalRules")
    def external_rules(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean to specify whether to use instance_security_group_rules. If `external_rules` is set to `true`, `inbound_rule` and `outbound_rule` can not be set directly in the security group.
        """
        return pulumi.get(self, "external_rules")

    @property
    @pulumi.getter(name="inboundDefaultPolicy")
    def inbound_default_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The default policy on incoming traffic. Possible values are: `accept` or `drop`.
        """
        return pulumi.get(self, "inbound_default_policy")

    @property
    @pulumi.getter(name="inboundRules")
    def inbound_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceSecurityGroupInboundRule']]]:
        """
        A list of inbound rule to add to the security group. (Structure is documented below.)
        """
        return pulumi.get(self, "inbound_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the security group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        `organization_id`) The ID of the project the security group is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="outboundDefaultPolicy")
    def outbound_default_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The default policy on outgoing traffic. Possible values are: `accept` or `drop`.
        """
        return pulumi.get(self, "outbound_default_policy")

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceSecurityGroupOutboundRule']]]:
        """
        A list of outbound rule to add to the security group. (Structure is documented below.)
        """
        return pulumi.get(self, "outbound_rules")

    @property
    @pulumi.getter
    def stateful(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean to specify whether the security group should be stateful or not.
        """
        return pulumi.get(self, "stateful")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        `zone`) The zone in which the security group should be created.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

