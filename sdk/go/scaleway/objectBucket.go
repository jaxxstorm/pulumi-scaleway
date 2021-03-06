// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates and manages Scaleway object storage buckets. For more information, see [the documentation](https://www.scaleway.com/en/docs/object-storage-feature/).
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
// 		_, err := scaleway.NewObjectBucket(ctx, "someBucket", &scaleway.ObjectBucketArgs{
// 			Acl: pulumi.String("private"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ObjectBucket struct {
	pulumi.CustomResourceState

	// The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) you want to apply to the bucket.
	Acl pulumi.StringPtrOutput `pulumi:"acl"`
	// The name of the bucket.
	Name pulumi.StringOutput `pulumi:"name"`
	// The [region](https://developers.scaleway.com/en/quickstart/#region-definition) in which the bucket should be created.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewObjectBucket registers a new resource with the given unique name, arguments, and options.
func NewObjectBucket(ctx *pulumi.Context,
	name string, args *ObjectBucketArgs, opts ...pulumi.ResourceOption) (*ObjectBucket, error) {
	if args == nil {
		args = &ObjectBucketArgs{}
	}
	var resource ObjectBucket
	err := ctx.RegisterResource("scaleway:index/objectBucket:ObjectBucket", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetObjectBucket gets an existing ObjectBucket resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetObjectBucket(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ObjectBucketState, opts ...pulumi.ResourceOption) (*ObjectBucket, error) {
	var resource ObjectBucket
	err := ctx.ReadResource("scaleway:index/objectBucket:ObjectBucket", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ObjectBucket resources.
type objectBucketState struct {
	// The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) you want to apply to the bucket.
	Acl *string `pulumi:"acl"`
	// The name of the bucket.
	Name *string `pulumi:"name"`
	// The [region](https://developers.scaleway.com/en/quickstart/#region-definition) in which the bucket should be created.
	Region *string `pulumi:"region"`
}

type ObjectBucketState struct {
	// The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) you want to apply to the bucket.
	Acl pulumi.StringPtrInput
	// The name of the bucket.
	Name pulumi.StringPtrInput
	// The [region](https://developers.scaleway.com/en/quickstart/#region-definition) in which the bucket should be created.
	Region pulumi.StringPtrInput
}

func (ObjectBucketState) ElementType() reflect.Type {
	return reflect.TypeOf((*objectBucketState)(nil)).Elem()
}

type objectBucketArgs struct {
	// The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) you want to apply to the bucket.
	Acl *string `pulumi:"acl"`
	// The name of the bucket.
	Name *string `pulumi:"name"`
	// The [region](https://developers.scaleway.com/en/quickstart/#region-definition) in which the bucket should be created.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a ObjectBucket resource.
type ObjectBucketArgs struct {
	// The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) you want to apply to the bucket.
	Acl pulumi.StringPtrInput
	// The name of the bucket.
	Name pulumi.StringPtrInput
	// The [region](https://developers.scaleway.com/en/quickstart/#region-definition) in which the bucket should be created.
	Region pulumi.StringPtrInput
}

func (ObjectBucketArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*objectBucketArgs)(nil)).Elem()
}
