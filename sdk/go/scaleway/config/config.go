// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

// The Scaleway access key.
func GetAccessKey(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "scaleway:accessKey")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "SCW_ACCESS_KEY").(string)
}

// Deprecated: Use `organization_id` instead.
func GetOrganization(ctx *pulumi.Context) string {
	return config.Get(ctx, "scaleway:organization")
}

// The Scaleway organization ID.
func GetOrganizationId(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "scaleway:organizationId")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "SCW_DEFAULT_ORGANIZATION_ID").(string)
}

// The Scaleway default region to use for your resources.
func GetRegion(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "scaleway:region")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "SCW_DEFAULT_REGION").(string)
}

// The Scaleway secret Key.
func GetSecretKey(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "scaleway:secretKey")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "SCW_SECRET_KEY").(string)
}

// Deprecated: Use `secret_key` instead.
func GetToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "scaleway:token")
}

// The Scaleway default zone to use for your resources.
func GetZone(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "scaleway:zone")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "SCW_DEFAULT_ZONE").(string)
}
