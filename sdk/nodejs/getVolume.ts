// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Gets information about a Volume.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * const dataVolume = scaleway.getVolume({
 *     name: "data",
 * });
 * const test = new scaleway.Server("test", {});
 * // ...
 * const dataVolumeAttachment = new scaleway.VolumeAttachment("dataVolumeAttachment", {
 *     server: test.id,
 *     volume: scaleway_volume.data.id,
 * });
 * ```
 */
export function getVolume(args: GetVolumeArgs, opts?: pulumi.InvokeOptions): Promise<GetVolumeResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("scaleway:index/getVolume:getVolume", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getVolume.
 */
export interface GetVolumeArgs {
    /**
     * Exact name of the Volume.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getVolume.
 */
export interface GetVolumeResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    /**
     * The ID of the Server which this Volume is currently attached to.
     */
    readonly server: string;
    /**
     * (Required) size of the volume in GB
     */
    readonly sizeInGb: number;
    /**
     * The type of volume this is, such as `lSsd`.
     */
    readonly type: string;
}
