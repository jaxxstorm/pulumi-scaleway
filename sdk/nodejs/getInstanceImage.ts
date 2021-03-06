// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Gets information about an instance image.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * // Get info by image id
 * const myImage = pulumi.output(scaleway.getInstanceImage({
 *     imageId: "11111111-1111-1111-1111-111111111111",
 * }, { async: true }));
 * ```
 */
export function getInstanceImage(args?: GetInstanceImageArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceImageResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("scaleway:index/getInstanceImage:getInstanceImage", {
        "architecture": args.architecture,
        "imageId": args.imageId,
        "latest": args.latest,
        "name": args.name,
        "organizationId": args.organizationId,
        "zone": args.zone,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstanceImage.
 */
export interface GetInstanceImageArgs {
    /**
     * The architecture the image is compatible with. Possible values are: `x8664` or `arm`.
     */
    readonly architecture?: string;
    /**
     * The image id. Only one of `name` and `imageId` should be specified.
     */
    readonly imageId?: string;
    /**
     * Use the latest image ID.
     */
    readonly latest?: boolean;
    /**
     * The image name. Only one of `name` and `imageId` should be specified.
     */
    readonly name?: string;
    /**
     * The ID of the organization the image is associated with.
     */
    readonly organizationId?: string;
    /**
     * `zone`) The zone in which the image exists.
     */
    readonly zone?: string;
}

/**
 * A collection of values returned by getInstanceImage.
 */
export interface GetInstanceImageResult {
    /**
     * IDs of the additional volumes in this image.
     */
    readonly additionalVolumeIds: string[];
    readonly architecture?: string;
    /**
     * Date of the image creation.
     */
    readonly creationDate: string;
    /**
     * ID of the default bootscript for this image.
     */
    readonly defaultBootscriptId: string;
    /**
     * ID of the server the image if based from.
     */
    readonly fromServerId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly imageId?: string;
    readonly latest?: boolean;
    /**
     * Date of image latest update.
     */
    readonly modificationDate: string;
    readonly name?: string;
    /**
     * The ID of the organization the image is associated with.
     */
    readonly organizationId: string;
    /**
     * Set to `true` if the image is public.
     */
    readonly public: boolean;
    /**
     * ID of the root volume in this image.
     */
    readonly rootVolumeId: string;
    /**
     * State of the image. Possible values are: `available`, `creating` or `error`.
     */
    readonly state: string;
    readonly zone: string;
}
