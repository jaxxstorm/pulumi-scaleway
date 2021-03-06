// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets information about a registry namespace.
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
// 		_, err := scaleway.LookupRegistryNamespaceBeta(ctx, &scaleway.LookupRegistryNamespaceBetaArgs{
// 			NamespaceId: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupRegistryNamespaceBeta(ctx *pulumi.Context, args *LookupRegistryNamespaceBetaArgs, opts ...pulumi.InvokeOption) (*LookupRegistryNamespaceBetaResult, error) {
	var rv LookupRegistryNamespaceBetaResult
	err := ctx.Invoke("scaleway:index/getRegistryNamespaceBeta:getRegistryNamespaceBeta", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegistryNamespaceBeta.
type LookupRegistryNamespaceBetaArgs struct {
	// The namespace name.
	// Only one of `name` and `namespaceId` should be specified.
	Name *string `pulumi:"name"`
	// The namespace id.
	// Only one of `name` and `namespaceId` should be specified.
	NamespaceId *string `pulumi:"namespaceId"`
	// `region`) The region in which the namespace exists.
	Region *string `pulumi:"region"`
}

// A collection of values returned by getRegistryNamespaceBeta.
type LookupRegistryNamespaceBetaResult struct {
	Description string `pulumi:"description"`
	// The endpoint of the Registry Namespace.
	Endpoint string `pulumi:"endpoint"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The Namespace Privacy Policy: whether or not the images are public.
	IsPublic       bool    `pulumi:"isPublic"`
	Name           *string `pulumi:"name"`
	NamespaceId    *string `pulumi:"namespaceId"`
	OrganizationId string  `pulumi:"organizationId"`
	Region         *string `pulumi:"region"`
}
