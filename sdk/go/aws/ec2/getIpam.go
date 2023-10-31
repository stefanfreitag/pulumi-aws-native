// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Schema of AWS::EC2::IPAM Type
func LookupIpam(ctx *pulumi.Context, args *LookupIpamArgs, opts ...pulumi.InvokeOption) (*LookupIpamResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupIpamResult
	err := ctx.Invoke("aws-native:ec2:getIpam", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupIpamArgs struct {
	// Id of the IPAM.
	IpamId string `pulumi:"ipamId"`
}

type LookupIpamResult struct {
	// The Amazon Resource Name (ARN) of the IPAM.
	Arn *string `pulumi:"arn"`
	// The Id of the default association to the default resource discovery, created with this IPAM.
	DefaultResourceDiscoveryAssociationId *string `pulumi:"defaultResourceDiscoveryAssociationId"`
	// The Id of the default resource discovery, created with this IPAM.
	DefaultResourceDiscoveryId *string `pulumi:"defaultResourceDiscoveryId"`
	Description                *string `pulumi:"description"`
	// Id of the IPAM.
	IpamId *string `pulumi:"ipamId"`
	// The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
	OperatingRegions []IpamOperatingRegion `pulumi:"operatingRegions"`
	// The Id of the default scope for publicly routable IP space, created with this IPAM.
	PrivateDefaultScopeId *string `pulumi:"privateDefaultScopeId"`
	// The Id of the default scope for publicly routable IP space, created with this IPAM.
	PublicDefaultScopeId *string `pulumi:"publicDefaultScopeId"`
	// The count of resource discoveries associated with this IPAM.
	ResourceDiscoveryAssociationCount *int `pulumi:"resourceDiscoveryAssociationCount"`
	// The number of scopes that currently exist in this IPAM.
	ScopeCount *int `pulumi:"scopeCount"`
	// An array of key-value pairs to apply to this resource.
	Tags []IpamTag `pulumi:"tags"`
	// The tier of the IPAM.
	Tier *IpamTier `pulumi:"tier"`
}

func LookupIpamOutput(ctx *pulumi.Context, args LookupIpamOutputArgs, opts ...pulumi.InvokeOption) LookupIpamResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIpamResult, error) {
			args := v.(LookupIpamArgs)
			r, err := LookupIpam(ctx, &args, opts...)
			var s LookupIpamResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIpamResultOutput)
}

type LookupIpamOutputArgs struct {
	// Id of the IPAM.
	IpamId pulumi.StringInput `pulumi:"ipamId"`
}

func (LookupIpamOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpamArgs)(nil)).Elem()
}

type LookupIpamResultOutput struct{ *pulumi.OutputState }

func (LookupIpamResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpamResult)(nil)).Elem()
}

func (o LookupIpamResultOutput) ToLookupIpamResultOutput() LookupIpamResultOutput {
	return o
}

func (o LookupIpamResultOutput) ToLookupIpamResultOutputWithContext(ctx context.Context) LookupIpamResultOutput {
	return o
}

func (o LookupIpamResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupIpamResult] {
	return pulumix.Output[LookupIpamResult]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the IPAM.
func (o LookupIpamResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The Id of the default association to the default resource discovery, created with this IPAM.
func (o LookupIpamResultOutput) DefaultResourceDiscoveryAssociationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.DefaultResourceDiscoveryAssociationId }).(pulumi.StringPtrOutput)
}

// The Id of the default resource discovery, created with this IPAM.
func (o LookupIpamResultOutput) DefaultResourceDiscoveryId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.DefaultResourceDiscoveryId }).(pulumi.StringPtrOutput)
}

func (o LookupIpamResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Id of the IPAM.
func (o LookupIpamResultOutput) IpamId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.IpamId }).(pulumi.StringPtrOutput)
}

// The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
func (o LookupIpamResultOutput) OperatingRegions() IpamOperatingRegionArrayOutput {
	return o.ApplyT(func(v LookupIpamResult) []IpamOperatingRegion { return v.OperatingRegions }).(IpamOperatingRegionArrayOutput)
}

// The Id of the default scope for publicly routable IP space, created with this IPAM.
func (o LookupIpamResultOutput) PrivateDefaultScopeId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.PrivateDefaultScopeId }).(pulumi.StringPtrOutput)
}

// The Id of the default scope for publicly routable IP space, created with this IPAM.
func (o LookupIpamResultOutput) PublicDefaultScopeId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *string { return v.PublicDefaultScopeId }).(pulumi.StringPtrOutput)
}

// The count of resource discoveries associated with this IPAM.
func (o LookupIpamResultOutput) ResourceDiscoveryAssociationCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *int { return v.ResourceDiscoveryAssociationCount }).(pulumi.IntPtrOutput)
}

// The number of scopes that currently exist in this IPAM.
func (o LookupIpamResultOutput) ScopeCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *int { return v.ScopeCount }).(pulumi.IntPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupIpamResultOutput) Tags() IpamTagArrayOutput {
	return o.ApplyT(func(v LookupIpamResult) []IpamTag { return v.Tags }).(IpamTagArrayOutput)
}

// The tier of the IPAM.
func (o LookupIpamResultOutput) Tier() IpamTierPtrOutput {
	return o.ApplyT(func(v LookupIpamResult) *IpamTier { return v.Tier }).(IpamTierPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIpamResultOutput{})
}
