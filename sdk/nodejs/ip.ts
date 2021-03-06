// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
 * Please use `scaleway.InstanceIP` instead.
 *
 * Provides IPs for servers. This allows IPs to be created, updated and deleted.
 * For additional details please refer to [API documentation](https://developer.scaleway.com/#ips).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * const testIp = new scaleway.IP("test_ip", {});
 * ```
 */
export class IP extends pulumi.CustomResource {
    /**
     * Get an existing IP resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IPState, opts?: pulumi.CustomResourceOptions): IP {
        return new IP(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'scaleway:index/iP:IP';

    /**
     * Returns true if the given object is an instance of IP.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IP {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IP.__pulumiType;
    }

    /**
     * IP of the new resource
     */
    public /*out*/ readonly ip!: pulumi.Output<string>;
    /**
     * Please us the scaleway.IPReverseDNS resource instead.
     *
     * @deprecated use scaleway_ip_reverse_dns resource instead
     */
    public readonly reverse!: pulumi.Output<string>;
    /**
     * ID of server to associate IP with
     */
    public readonly server!: pulumi.Output<string>;

    /**
     * Create a IP resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: IPArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IPArgs | IPState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IPState | undefined;
            inputs["ip"] = state ? state.ip : undefined;
            inputs["reverse"] = state ? state.reverse : undefined;
            inputs["server"] = state ? state.server : undefined;
        } else {
            const args = argsOrState as IPArgs | undefined;
            inputs["reverse"] = args ? args.reverse : undefined;
            inputs["server"] = args ? args.server : undefined;
            inputs["ip"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(IP.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IP resources.
 */
export interface IPState {
    /**
     * IP of the new resource
     */
    readonly ip?: pulumi.Input<string>;
    /**
     * Please us the scaleway.IPReverseDNS resource instead.
     *
     * @deprecated use scaleway_ip_reverse_dns resource instead
     */
    readonly reverse?: pulumi.Input<string>;
    /**
     * ID of server to associate IP with
     */
    readonly server?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IP resource.
 */
export interface IPArgs {
    /**
     * Please us the scaleway.IPReverseDNS resource instead.
     *
     * @deprecated use scaleway_ip_reverse_dns resource instead
     */
    readonly reverse?: pulumi.Input<string>;
    /**
     * ID of server to associate IP with
     */
    readonly server?: pulumi.Input<string>;
}
