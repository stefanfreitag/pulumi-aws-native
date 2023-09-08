// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lightsail

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Lightsail::Distribution
func LookupDistribution(ctx *pulumi.Context, args *LookupDistributionArgs, opts ...pulumi.InvokeOption) (*LookupDistributionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDistributionResult
	err := ctx.Invoke("aws-native:lightsail:getDistribution", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDistributionArgs struct {
	// The name for the distribution.
	DistributionName string `pulumi:"distributionName"`
}

type LookupDistributionResult struct {
	// Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.
	AbleToUpdateBundle *bool `pulumi:"ableToUpdateBundle"`
	// The bundle ID to use for the distribution.
	BundleId *string `pulumi:"bundleId"`
	// An object that describes the cache behavior settings for the distribution.
	CacheBehaviorSettings *DistributionCacheSettings `pulumi:"cacheBehaviorSettings"`
	// An array of objects that describe the per-path cache behavior for the distribution.
	CacheBehaviors []DistributionCacheBehaviorPerPath `pulumi:"cacheBehaviors"`
	// The certificate attached to the Distribution.
	CertificateName *string `pulumi:"certificateName"`
	// An object that describes the default cache behavior for the distribution.
	DefaultCacheBehavior *DistributionCacheBehavior `pulumi:"defaultCacheBehavior"`
	DistributionArn      *string                    `pulumi:"distributionArn"`
	// Indicates whether the distribution is enabled.
	IsEnabled *bool `pulumi:"isEnabled"`
	// An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.
	Origin *DistributionInputOrigin `pulumi:"origin"`
	// The status of the distribution.
	Status *string `pulumi:"status"`
	// An array of key-value pairs to apply to this resource.
	Tags []DistributionTag `pulumi:"tags"`
}

func LookupDistributionOutput(ctx *pulumi.Context, args LookupDistributionOutputArgs, opts ...pulumi.InvokeOption) LookupDistributionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDistributionResult, error) {
			args := v.(LookupDistributionArgs)
			r, err := LookupDistribution(ctx, &args, opts...)
			var s LookupDistributionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDistributionResultOutput)
}

type LookupDistributionOutputArgs struct {
	// The name for the distribution.
	DistributionName pulumi.StringInput `pulumi:"distributionName"`
}

func (LookupDistributionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDistributionArgs)(nil)).Elem()
}

type LookupDistributionResultOutput struct{ *pulumi.OutputState }

func (LookupDistributionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDistributionResult)(nil)).Elem()
}

func (o LookupDistributionResultOutput) ToLookupDistributionResultOutput() LookupDistributionResultOutput {
	return o
}

func (o LookupDistributionResultOutput) ToLookupDistributionResultOutputWithContext(ctx context.Context) LookupDistributionResultOutput {
	return o
}

func (o LookupDistributionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDistributionResult] {
	return pulumix.Output[LookupDistributionResult]{
		OutputState: o.OutputState,
	}
}

// Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.
func (o LookupDistributionResultOutput) AbleToUpdateBundle() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *bool { return v.AbleToUpdateBundle }).(pulumi.BoolPtrOutput)
}

// The bundle ID to use for the distribution.
func (o LookupDistributionResultOutput) BundleId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *string { return v.BundleId }).(pulumi.StringPtrOutput)
}

// An object that describes the cache behavior settings for the distribution.
func (o LookupDistributionResultOutput) CacheBehaviorSettings() DistributionCacheSettingsPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *DistributionCacheSettings { return v.CacheBehaviorSettings }).(DistributionCacheSettingsPtrOutput)
}

// An array of objects that describe the per-path cache behavior for the distribution.
func (o LookupDistributionResultOutput) CacheBehaviors() DistributionCacheBehaviorPerPathArrayOutput {
	return o.ApplyT(func(v LookupDistributionResult) []DistributionCacheBehaviorPerPath { return v.CacheBehaviors }).(DistributionCacheBehaviorPerPathArrayOutput)
}

// The certificate attached to the Distribution.
func (o LookupDistributionResultOutput) CertificateName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *string { return v.CertificateName }).(pulumi.StringPtrOutput)
}

// An object that describes the default cache behavior for the distribution.
func (o LookupDistributionResultOutput) DefaultCacheBehavior() DistributionCacheBehaviorPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *DistributionCacheBehavior { return v.DefaultCacheBehavior }).(DistributionCacheBehaviorPtrOutput)
}

func (o LookupDistributionResultOutput) DistributionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *string { return v.DistributionArn }).(pulumi.StringPtrOutput)
}

// Indicates whether the distribution is enabled.
func (o LookupDistributionResultOutput) IsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *bool { return v.IsEnabled }).(pulumi.BoolPtrOutput)
}

// An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.
func (o LookupDistributionResultOutput) Origin() DistributionInputOriginPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *DistributionInputOrigin { return v.Origin }).(DistributionInputOriginPtrOutput)
}

// The status of the distribution.
func (o LookupDistributionResultOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *string { return v.Status }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupDistributionResultOutput) Tags() DistributionTagArrayOutput {
	return o.ApplyT(func(v LookupDistributionResult) []DistributionTag { return v.Tags }).(DistributionTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDistributionResultOutput{})
}
