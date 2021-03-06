// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
// Please use `InstanceSecurityGroup` instead.
//
// Provides security groups. This allows security groups to be created, updated and deleted.
// For additional details please refer to [API documentation](https://developer.scaleway.com/#security-groups).
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
// 		_, err := scaleway.NewSecurityGroup(ctx, "test", &scaleway.SecurityGroupArgs{
// 			Description:           pulumi.String("test"),
// 			EnableDefaultSecurity: pulumi.Bool(true),
// 			InboundDefaultPolicy:  pulumi.String("accept"),
// 			OutboundDefaultPolicy: pulumi.String("drop"),
// 			Stateful:              pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SecurityGroup struct {
	pulumi.CustomResourceState

	// description of security group
	Description pulumi.StringOutput `pulumi:"description"`
	// default: true. Add default security group rules
	EnableDefaultSecurity pulumi.BoolPtrOutput `pulumi:"enableDefaultSecurity"`
	// default policy for inbound traffic. Can be one of accept or drop
	InboundDefaultPolicy pulumi.StringPtrOutput `pulumi:"inboundDefaultPolicy"`
	// name of security group
	Name pulumi.StringOutput `pulumi:"name"`
	// default policy for outbound traffic. Can be one of accept or drop
	OutboundDefaultPolicy pulumi.StringPtrOutput `pulumi:"outboundDefaultPolicy"`
	// default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers
	Stateful pulumi.BoolPtrOutput `pulumi:"stateful"`
}

// NewSecurityGroup registers a new resource with the given unique name, arguments, and options.
func NewSecurityGroup(ctx *pulumi.Context,
	name string, args *SecurityGroupArgs, opts ...pulumi.ResourceOption) (*SecurityGroup, error) {
	if args == nil || args.Description == nil {
		return nil, errors.New("missing required argument 'Description'")
	}
	if args == nil {
		args = &SecurityGroupArgs{}
	}
	var resource SecurityGroup
	err := ctx.RegisterResource("scaleway:index/securityGroup:SecurityGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecurityGroup gets an existing SecurityGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecurityGroupState, opts ...pulumi.ResourceOption) (*SecurityGroup, error) {
	var resource SecurityGroup
	err := ctx.ReadResource("scaleway:index/securityGroup:SecurityGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecurityGroup resources.
type securityGroupState struct {
	// description of security group
	Description *string `pulumi:"description"`
	// default: true. Add default security group rules
	EnableDefaultSecurity *bool `pulumi:"enableDefaultSecurity"`
	// default policy for inbound traffic. Can be one of accept or drop
	InboundDefaultPolicy *string `pulumi:"inboundDefaultPolicy"`
	// name of security group
	Name *string `pulumi:"name"`
	// default policy for outbound traffic. Can be one of accept or drop
	OutboundDefaultPolicy *string `pulumi:"outboundDefaultPolicy"`
	// default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers
	Stateful *bool `pulumi:"stateful"`
}

type SecurityGroupState struct {
	// description of security group
	Description pulumi.StringPtrInput
	// default: true. Add default security group rules
	EnableDefaultSecurity pulumi.BoolPtrInput
	// default policy for inbound traffic. Can be one of accept or drop
	InboundDefaultPolicy pulumi.StringPtrInput
	// name of security group
	Name pulumi.StringPtrInput
	// default policy for outbound traffic. Can be one of accept or drop
	OutboundDefaultPolicy pulumi.StringPtrInput
	// default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers
	Stateful pulumi.BoolPtrInput
}

func (SecurityGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*securityGroupState)(nil)).Elem()
}

type securityGroupArgs struct {
	// description of security group
	Description string `pulumi:"description"`
	// default: true. Add default security group rules
	EnableDefaultSecurity *bool `pulumi:"enableDefaultSecurity"`
	// default policy for inbound traffic. Can be one of accept or drop
	InboundDefaultPolicy *string `pulumi:"inboundDefaultPolicy"`
	// name of security group
	Name *string `pulumi:"name"`
	// default policy for outbound traffic. Can be one of accept or drop
	OutboundDefaultPolicy *string `pulumi:"outboundDefaultPolicy"`
	// default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers
	Stateful *bool `pulumi:"stateful"`
}

// The set of arguments for constructing a SecurityGroup resource.
type SecurityGroupArgs struct {
	// description of security group
	Description pulumi.StringInput
	// default: true. Add default security group rules
	EnableDefaultSecurity pulumi.BoolPtrInput
	// default policy for inbound traffic. Can be one of accept or drop
	InboundDefaultPolicy pulumi.StringPtrInput
	// name of security group
	Name pulumi.StringPtrInput
	// default policy for outbound traffic. Can be one of accept or drop
	OutboundDefaultPolicy pulumi.StringPtrInput
	// default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers
	Stateful pulumi.BoolPtrInput
}

func (SecurityGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*securityGroupArgs)(nil)).Elem()
}
