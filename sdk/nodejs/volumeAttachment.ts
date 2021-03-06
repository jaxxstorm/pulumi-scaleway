// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
 * Please use `scaleway_instance_server.additional_volumes` instead.
 *
 * This allows volumes to be attached to servers.
 *
 * > **Warning:** Attaching volumes requires the servers to be powered off. This will lead to downtime if the server is already in use.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * const testServer = new scaleway.Server("testServer", {
 *     image: "aecaed73-51a5-4439-a127-6d8229847145",
 *     type: "C2S",
 * });
 * const testVolume = new scaleway.Volume("testVolume", {
 *     sizeInGb: 20,
 *     type: "l_ssd",
 * });
 * const testVolumeAttachment = new scaleway.VolumeAttachment("testVolumeAttachment", {
 *     server: testServer.id,
 *     volume: testVolume.id,
 * });
 * ```
 */
export class VolumeAttachment extends pulumi.CustomResource {
    /**
     * Get an existing VolumeAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeAttachmentState, opts?: pulumi.CustomResourceOptions): VolumeAttachment {
        return new VolumeAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'scaleway:index/volumeAttachment:VolumeAttachment';

    /**
     * Returns true if the given object is an instance of VolumeAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VolumeAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VolumeAttachment.__pulumiType;
    }

    /**
     * id of the server
     */
    public readonly server!: pulumi.Output<string>;
    /**
     * id of the volume to be attached
     */
    public readonly volume!: pulumi.Output<string>;

    /**
     * Create a VolumeAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeAttachmentArgs | VolumeAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VolumeAttachmentState | undefined;
            inputs["server"] = state ? state.server : undefined;
            inputs["volume"] = state ? state.volume : undefined;
        } else {
            const args = argsOrState as VolumeAttachmentArgs | undefined;
            if (!args || args.server === undefined) {
                throw new Error("Missing required property 'server'");
            }
            if (!args || args.volume === undefined) {
                throw new Error("Missing required property 'volume'");
            }
            inputs["server"] = args ? args.server : undefined;
            inputs["volume"] = args ? args.volume : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(VolumeAttachment.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VolumeAttachment resources.
 */
export interface VolumeAttachmentState {
    /**
     * id of the server
     */
    readonly server?: pulumi.Input<string>;
    /**
     * id of the volume to be attached
     */
    readonly volume?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VolumeAttachment resource.
 */
export interface VolumeAttachmentArgs {
    /**
     * id of the server
     */
    readonly server: pulumi.Input<string>;
    /**
     * id of the volume to be attached
     */
    readonly volume: pulumi.Input<string>;
}
