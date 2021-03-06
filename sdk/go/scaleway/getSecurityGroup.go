// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
// Please use `InstanceSecurityGroup` instead.
//
// Gets information about a Security Group.
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
// 		_, err := scaleway.LookupSecurityGroup(ctx, &scaleway.LookupSecurityGroupArgs{
// 			Name: "my-security-group",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupSecurityGroup(ctx *pulumi.Context, args *LookupSecurityGroupArgs, opts ...pulumi.InvokeOption) (*LookupSecurityGroupResult, error) {
	var rv LookupSecurityGroupResult
	err := ctx.Invoke("scaleway:index/getSecurityGroup:getSecurityGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSecurityGroup.
type LookupSecurityGroupArgs struct {
	// Exact name of desired Security Group
	Name string `pulumi:"name"`
}

// A collection of values returned by getSecurityGroup.
type LookupSecurityGroupResult struct {
	// description of the security group
	Description string `pulumi:"description"`
	// have default security group rules been added to this security group?
	EnableDefaultSecurity bool `pulumi:"enableDefaultSecurity"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}
