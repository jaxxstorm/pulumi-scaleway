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

__all__ = ['KubernetesNodePoolBeta']


class KubernetesNodePoolBeta(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autohealing: Optional[pulumi.Input[bool]] = None,
                 autoscaling: Optional[pulumi.Input[bool]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 container_runtime: Optional[pulumi.Input[str]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 min_size: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 placement_group_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 wait_for_pool_ready: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates and manages Scaleway Kubernetes cluster pools. For more information, see [the documentation](https://developers.scaleway.com/en/products/k8s/api/).

        ## Examples

        ### Basic

        ```python
        import pulumi
        import pulumi_scaleway as scaleway

        jack = scaleway.KubernetesClusterBeta("jack",
            version="1.18.0",
            cni="cilium")
        bill = scaleway.KubernetesNodePoolBeta("bill",
            cluster_id=jack.id,
            node_type="GP1-S",
            size=3,
            min_size=0,
            max_size=10,
            autoscaling=True,
            autohealing=True,
            container_runtime="docker",
            placement_group_id="1267e3fd-a51c-49ed-ad12-857092ee3a3d")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] autohealing: Enables the autohealing feature for this pool.
        :param pulumi.Input[bool] autoscaling: Enables the autoscaling feature for this pool.
               > **Important:** When enabled, an update of the `size` will not be taken into account.
        :param pulumi.Input[str] cluster_id: The ID of the Kubernetes cluster on which this pool will be created.
        :param pulumi.Input[str] container_runtime: The container runtime of the pool.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[int] max_size: The maximum size of the pool, used by the autoscaling feature.
        :param pulumi.Input[int] min_size: The minimum size of the pool, used by the autoscaling feature.
        :param pulumi.Input[str] name: The name for the pool.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] node_type: The commercial type of the pool instances.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] placement_group_id: The [placement group](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) the nodes of the pool will be attached to.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] region: `region`) The region in which the pool should be created.
        :param pulumi.Input[int] size: The size of the pool.
               > **Important:** This field will only be used at creation if autoscaling is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the pool.
        :param pulumi.Input[bool] wait_for_pool_ready: Whether to wait for the pool to be ready.
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

            __props__['autohealing'] = autohealing
            __props__['autoscaling'] = autoscaling
            if cluster_id is None:
                raise TypeError("Missing required property 'cluster_id'")
            __props__['cluster_id'] = cluster_id
            __props__['container_runtime'] = container_runtime
            __props__['max_size'] = max_size
            __props__['min_size'] = min_size
            __props__['name'] = name
            if node_type is None:
                raise TypeError("Missing required property 'node_type'")
            __props__['node_type'] = node_type
            __props__['placement_group_id'] = placement_group_id
            __props__['region'] = region
            if size is None:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['tags'] = tags
            __props__['wait_for_pool_ready'] = wait_for_pool_ready
            __props__['created_at'] = None
            __props__['current_size'] = None
            __props__['nodes'] = None
            __props__['status'] = None
            __props__['updated_at'] = None
            __props__['version'] = None
        super(KubernetesNodePoolBeta, __self__).__init__(
            'scaleway:index/kubernetesNodePoolBeta:KubernetesNodePoolBeta',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            autohealing: Optional[pulumi.Input[bool]] = None,
            autoscaling: Optional[pulumi.Input[bool]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            container_runtime: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            current_size: Optional[pulumi.Input[int]] = None,
            max_size: Optional[pulumi.Input[int]] = None,
            min_size: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_type: Optional[pulumi.Input[str]] = None,
            nodes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesNodePoolBetaNodeArgs']]]]] = None,
            placement_group_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None,
            wait_for_pool_ready: Optional[pulumi.Input[bool]] = None) -> 'KubernetesNodePoolBeta':
        """
        Get an existing KubernetesNodePoolBeta resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] autohealing: Enables the autohealing feature for this pool.
        :param pulumi.Input[bool] autoscaling: Enables the autoscaling feature for this pool.
               > **Important:** When enabled, an update of the `size` will not be taken into account.
        :param pulumi.Input[str] cluster_id: The ID of the Kubernetes cluster on which this pool will be created.
        :param pulumi.Input[str] container_runtime: The container runtime of the pool.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] created_at: The creation date of the pool.
        :param pulumi.Input[int] current_size: The actual size of the pool
        :param pulumi.Input[int] max_size: The maximum size of the pool, used by the autoscaling feature.
        :param pulumi.Input[int] min_size: The minimum size of the pool, used by the autoscaling feature.
        :param pulumi.Input[str] name: The name for the pool.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] node_type: The commercial type of the pool instances.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesNodePoolBetaNodeArgs']]]] nodes: (List of) The nodes in the default pool.
        :param pulumi.Input[str] placement_group_id: The [placement group](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) the nodes of the pool will be attached to.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] region: `region`) The region in which the pool should be created.
        :param pulumi.Input[int] size: The size of the pool.
               > **Important:** This field will only be used at creation if autoscaling is enabled.
        :param pulumi.Input[str] status: The status of the node.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the pool.
        :param pulumi.Input[str] updated_at: The last update date of the pool.
        :param pulumi.Input[str] version: The version of the pool.
        :param pulumi.Input[bool] wait_for_pool_ready: Whether to wait for the pool to be ready.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["autohealing"] = autohealing
        __props__["autoscaling"] = autoscaling
        __props__["cluster_id"] = cluster_id
        __props__["container_runtime"] = container_runtime
        __props__["created_at"] = created_at
        __props__["current_size"] = current_size
        __props__["max_size"] = max_size
        __props__["min_size"] = min_size
        __props__["name"] = name
        __props__["node_type"] = node_type
        __props__["nodes"] = nodes
        __props__["placement_group_id"] = placement_group_id
        __props__["region"] = region
        __props__["size"] = size
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["updated_at"] = updated_at
        __props__["version"] = version
        __props__["wait_for_pool_ready"] = wait_for_pool_ready
        return KubernetesNodePoolBeta(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def autohealing(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables the autohealing feature for this pool.
        """
        return pulumi.get(self, "autohealing")

    @property
    @pulumi.getter
    def autoscaling(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables the autoscaling feature for this pool.
        > **Important:** When enabled, an update of the `size` will not be taken into account.
        """
        return pulumi.get(self, "autoscaling")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Kubernetes cluster on which this pool will be created.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="containerRuntime")
    def container_runtime(self) -> pulumi.Output[Optional[str]]:
        """
        The container runtime of the pool.
        > **Important:** Updates to this field will recreate a new resource.
        """
        return pulumi.get(self, "container_runtime")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The creation date of the pool.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="currentSize")
    def current_size(self) -> pulumi.Output[int]:
        """
        The actual size of the pool
        """
        return pulumi.get(self, "current_size")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[int]:
        """
        The maximum size of the pool, used by the autoscaling feature.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[Optional[int]]:
        """
        The minimum size of the pool, used by the autoscaling feature.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the pool.
        > **Important:** Updates to this field will recreate a new resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[str]:
        """
        The commercial type of the pool instances.
        > **Important:** Updates to this field will recreate a new resource.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence['outputs.KubernetesNodePoolBetaNode']]:
        """
        (List of) The nodes in the default pool.
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The [placement group](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) the nodes of the pool will be attached to.
        > **Important:** Updates to this field will recreate a new resource.
        """
        return pulumi.get(self, "placement_group_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        `region`) The region in which the pool should be created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size of the pool.
        > **Important:** This field will only be used at creation if autoscaling is enabled.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the node.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with the pool.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The last update date of the pool.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the pool.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="waitForPoolReady")
    def wait_for_pool_ready(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to wait for the pool to be ready.
        """
        return pulumi.get(self, "wait_for_pool_ready")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

