// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
 * Please use `scaleway.InstanceServer` instead.
 *
 * Provides servers. This allows servers to be created, updated and deleted.
 * For additional details please refer to [API documentation](https://developer.scaleway.com/#servers).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * const test = new scaleway.Server("test", {
 *     image: "5faef9cd-ea9b-4a63-9171-9e26bec03dbc",
 *     type: "VC1M",
 *     volumes: [{
 *         sizeInGb: 20,
 *         type: "l_ssd",
 *     }],
 * });
 * ```
 * ## Volume
 *
 * You can attach additional volumes to your instance, which will share the lifetime
 * of your `scaleway.Server` resource.
 *
 * > **Warning:** Using the `volume` attribute does not modify the System Volume provided default with every `scaleway.Server` instance. Instead it adds additional volumes to the server instance.
 *
 * > **Warning:** Some instance types require an additional volume to work. This includes for example *START-1M* and *VC1M*. If you run into this issue add an additional volume of the specified size.
 *
 * The `volume` mapping supports the following:
 *
 * * `type` - (Required) The type of volume. Can be `"lSsd"`
 * * `sizeInGb` - (Required) The size of the volume in gigabytes.
 */
export class Server extends pulumi.CustomResource {
    /**
     * Get an existing Server resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState, opts?: pulumi.CustomResourceOptions): Server {
        return new Server(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'scaleway:index/server:Server';

    /**
     * Returns true if the given object is an instance of Server.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Server {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Server.__pulumiType;
    }

    /**
     * the boot mechanism for this server. Possible values include `local` and `bootscript`
     */
    public readonly bootType!: pulumi.Output<string>;
    /**
     * server bootscript
     */
    public readonly bootscript!: pulumi.Output<string | undefined>;
    /**
     * allows you to define cloudinit script for this server
     */
    public readonly cloudinit!: pulumi.Output<string>;
    /**
     * make server publicly available
     */
    public readonly dynamicIpRequired!: pulumi.Output<boolean | undefined>;
    /**
     * enable ipv6
     */
    public readonly enableIpv6!: pulumi.Output<boolean | undefined>;
    /**
     * base image of server
     */
    public readonly image!: pulumi.Output<string>;
    /**
     * name of server
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * private ip of the new resource
     */
    public /*out*/ readonly privateIp!: pulumi.Output<string>;
    /**
     * set a public ip previously created (a real ip is expected here, not its resource id)
     */
    public readonly publicIp!: pulumi.Output<string>;
    /**
     * if `enableIpv6` is set this contains the ipv6 address of your instance
     */
    public /*out*/ readonly publicIpv6!: pulumi.Output<string>;
    /**
     * assign security group to server
     */
    public readonly securityGroup!: pulumi.Output<string | undefined>;
    /**
     * allows you to define the desired state of your server. Valid values include (`stopped`, `running`)
     */
    public readonly state!: pulumi.Output<string>;
    /**
     * contains details from the scaleway API the state of your instance
     */
    public /*out*/ readonly stateDetail!: pulumi.Output<string>;
    /**
     * list of tags for server
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * type of server
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * attach additional volumes to your instance (see below)
     */
    public readonly volumes!: pulumi.Output<outputs.ServerVolume[] | undefined>;

    /**
     * Create a Server resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerArgs | ServerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ServerState | undefined;
            inputs["bootType"] = state ? state.bootType : undefined;
            inputs["bootscript"] = state ? state.bootscript : undefined;
            inputs["cloudinit"] = state ? state.cloudinit : undefined;
            inputs["dynamicIpRequired"] = state ? state.dynamicIpRequired : undefined;
            inputs["enableIpv6"] = state ? state.enableIpv6 : undefined;
            inputs["image"] = state ? state.image : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["privateIp"] = state ? state.privateIp : undefined;
            inputs["publicIp"] = state ? state.publicIp : undefined;
            inputs["publicIpv6"] = state ? state.publicIpv6 : undefined;
            inputs["securityGroup"] = state ? state.securityGroup : undefined;
            inputs["state"] = state ? state.state : undefined;
            inputs["stateDetail"] = state ? state.stateDetail : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["volumes"] = state ? state.volumes : undefined;
        } else {
            const args = argsOrState as ServerArgs | undefined;
            if (!args || args.image === undefined) {
                throw new Error("Missing required property 'image'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["bootType"] = args ? args.bootType : undefined;
            inputs["bootscript"] = args ? args.bootscript : undefined;
            inputs["cloudinit"] = args ? args.cloudinit : undefined;
            inputs["dynamicIpRequired"] = args ? args.dynamicIpRequired : undefined;
            inputs["enableIpv6"] = args ? args.enableIpv6 : undefined;
            inputs["image"] = args ? args.image : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["publicIp"] = args ? args.publicIp : undefined;
            inputs["securityGroup"] = args ? args.securityGroup : undefined;
            inputs["state"] = args ? args.state : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["volumes"] = args ? args.volumes : undefined;
            inputs["privateIp"] = undefined /*out*/;
            inputs["publicIpv6"] = undefined /*out*/;
            inputs["stateDetail"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Server.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Server resources.
 */
export interface ServerState {
    /**
     * the boot mechanism for this server. Possible values include `local` and `bootscript`
     */
    readonly bootType?: pulumi.Input<string>;
    /**
     * server bootscript
     */
    readonly bootscript?: pulumi.Input<string>;
    /**
     * allows you to define cloudinit script for this server
     */
    readonly cloudinit?: pulumi.Input<string>;
    /**
     * make server publicly available
     */
    readonly dynamicIpRequired?: pulumi.Input<boolean>;
    /**
     * enable ipv6
     */
    readonly enableIpv6?: pulumi.Input<boolean>;
    /**
     * base image of server
     */
    readonly image?: pulumi.Input<string>;
    /**
     * name of server
     */
    readonly name?: pulumi.Input<string>;
    /**
     * private ip of the new resource
     */
    readonly privateIp?: pulumi.Input<string>;
    /**
     * set a public ip previously created (a real ip is expected here, not its resource id)
     */
    readonly publicIp?: pulumi.Input<string>;
    /**
     * if `enableIpv6` is set this contains the ipv6 address of your instance
     */
    readonly publicIpv6?: pulumi.Input<string>;
    /**
     * assign security group to server
     */
    readonly securityGroup?: pulumi.Input<string>;
    /**
     * allows you to define the desired state of your server. Valid values include (`stopped`, `running`)
     */
    readonly state?: pulumi.Input<string>;
    /**
     * contains details from the scaleway API the state of your instance
     */
    readonly stateDetail?: pulumi.Input<string>;
    /**
     * list of tags for server
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * type of server
     */
    readonly type?: pulumi.Input<string>;
    /**
     * attach additional volumes to your instance (see below)
     */
    readonly volumes?: pulumi.Input<pulumi.Input<inputs.ServerVolume>[]>;
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    /**
     * the boot mechanism for this server. Possible values include `local` and `bootscript`
     */
    readonly bootType?: pulumi.Input<string>;
    /**
     * server bootscript
     */
    readonly bootscript?: pulumi.Input<string>;
    /**
     * allows you to define cloudinit script for this server
     */
    readonly cloudinit?: pulumi.Input<string>;
    /**
     * make server publicly available
     */
    readonly dynamicIpRequired?: pulumi.Input<boolean>;
    /**
     * enable ipv6
     */
    readonly enableIpv6?: pulumi.Input<boolean>;
    /**
     * base image of server
     */
    readonly image: pulumi.Input<string>;
    /**
     * name of server
     */
    readonly name?: pulumi.Input<string>;
    /**
     * set a public ip previously created (a real ip is expected here, not its resource id)
     */
    readonly publicIp?: pulumi.Input<string>;
    /**
     * assign security group to server
     */
    readonly securityGroup?: pulumi.Input<string>;
    /**
     * allows you to define the desired state of your server. Valid values include (`stopped`, `running`)
     */
    readonly state?: pulumi.Input<string>;
    /**
     * list of tags for server
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * type of server
     */
    readonly type: pulumi.Input<string>;
    /**
     * attach additional volumes to your instance (see below)
     */
    readonly volumes?: pulumi.Input<pulumi.Input<inputs.ServerVolume>[]>;
}
