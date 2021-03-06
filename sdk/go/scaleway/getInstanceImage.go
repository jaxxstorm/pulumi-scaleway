// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets information about an instance image.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-scaleway/sdk/go/scaleway"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "11111111-1111-1111-1111-111111111111"
// 		_, err := scaleway.GetInstanceImage(ctx, &scaleway.GetInstanceImageArgs{
// 			ImageId: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetInstanceImage(ctx *pulumi.Context, args *GetInstanceImageArgs, opts ...pulumi.InvokeOption) (*GetInstanceImageResult, error) {
	var rv GetInstanceImageResult
	err := ctx.Invoke("scaleway:index/getInstanceImage:getInstanceImage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInstanceImage.
type GetInstanceImageArgs struct {
	// The architecture the image is compatible with. Possible values are: `x8664` or `arm`.
	Architecture *string `pulumi:"architecture"`
	// The image id. Only one of `name` and `imageId` should be specified.
	ImageId *string `pulumi:"imageId"`
	// Use the latest image ID.
	Latest *bool `pulumi:"latest"`
	// The image name. Only one of `name` and `imageId` should be specified.
	Name *string `pulumi:"name"`
	// The ID of the organization the image is associated with.
	OrganizationId *string `pulumi:"organizationId"`
	// `zone`) The zone in which the image exists.
	Zone *string `pulumi:"zone"`
}

// A collection of values returned by getInstanceImage.
type GetInstanceImageResult struct {
	// IDs of the additional volumes in this image.
	AdditionalVolumeIds []string `pulumi:"additionalVolumeIds"`
	Architecture        *string  `pulumi:"architecture"`
	// Date of the image creation.
	CreationDate string `pulumi:"creationDate"`
	// ID of the default bootscript for this image.
	DefaultBootscriptId string `pulumi:"defaultBootscriptId"`
	// ID of the server the image if based from.
	FromServerId string `pulumi:"fromServerId"`
	// The provider-assigned unique ID for this managed resource.
	Id      string  `pulumi:"id"`
	ImageId *string `pulumi:"imageId"`
	Latest  *bool   `pulumi:"latest"`
	// Date of image latest update.
	ModificationDate string  `pulumi:"modificationDate"`
	Name             *string `pulumi:"name"`
	// The ID of the organization the image is associated with.
	OrganizationId string `pulumi:"organizationId"`
	// Set to `true` if the image is public.
	Public bool `pulumi:"public"`
	// ID of the root volume in this image.
	RootVolumeId string `pulumi:"rootVolumeId"`
	// State of the image. Possible values are: `available`, `creating` or `error`.
	State string `pulumi:"state"`
	Zone  string `pulumi:"zone"`
}
