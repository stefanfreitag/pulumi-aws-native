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

// The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider
func LookupVerifiedAccessTrustProvider(ctx *pulumi.Context, args *LookupVerifiedAccessTrustProviderArgs, opts ...pulumi.InvokeOption) (*LookupVerifiedAccessTrustProviderResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVerifiedAccessTrustProviderResult
	err := ctx.Invoke("aws-native:ec2:getVerifiedAccessTrustProvider", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupVerifiedAccessTrustProviderArgs struct {
	// The ID of the Amazon Web Services Verified Access trust provider.
	VerifiedAccessTrustProviderId string `pulumi:"verifiedAccessTrustProviderId"`
}

type LookupVerifiedAccessTrustProviderResult struct {
	// The creation time.
	CreationTime *string `pulumi:"creationTime"`
	// A description for the Amazon Web Services Verified Access trust provider.
	Description *string `pulumi:"description"`
	// The last updated time.
	LastUpdatedTime *string                                 `pulumi:"lastUpdatedTime"`
	OidcOptions     *VerifiedAccessTrustProviderOidcOptions `pulumi:"oidcOptions"`
	// An array of key-value pairs to apply to this resource.
	Tags []VerifiedAccessTrustProviderTag `pulumi:"tags"`
	// The ID of the Amazon Web Services Verified Access trust provider.
	VerifiedAccessTrustProviderId *string `pulumi:"verifiedAccessTrustProviderId"`
}

func LookupVerifiedAccessTrustProviderOutput(ctx *pulumi.Context, args LookupVerifiedAccessTrustProviderOutputArgs, opts ...pulumi.InvokeOption) LookupVerifiedAccessTrustProviderResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVerifiedAccessTrustProviderResult, error) {
			args := v.(LookupVerifiedAccessTrustProviderArgs)
			r, err := LookupVerifiedAccessTrustProvider(ctx, &args, opts...)
			var s LookupVerifiedAccessTrustProviderResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVerifiedAccessTrustProviderResultOutput)
}

type LookupVerifiedAccessTrustProviderOutputArgs struct {
	// The ID of the Amazon Web Services Verified Access trust provider.
	VerifiedAccessTrustProviderId pulumi.StringInput `pulumi:"verifiedAccessTrustProviderId"`
}

func (LookupVerifiedAccessTrustProviderOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVerifiedAccessTrustProviderArgs)(nil)).Elem()
}

type LookupVerifiedAccessTrustProviderResultOutput struct{ *pulumi.OutputState }

func (LookupVerifiedAccessTrustProviderResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVerifiedAccessTrustProviderResult)(nil)).Elem()
}

func (o LookupVerifiedAccessTrustProviderResultOutput) ToLookupVerifiedAccessTrustProviderResultOutput() LookupVerifiedAccessTrustProviderResultOutput {
	return o
}

func (o LookupVerifiedAccessTrustProviderResultOutput) ToLookupVerifiedAccessTrustProviderResultOutputWithContext(ctx context.Context) LookupVerifiedAccessTrustProviderResultOutput {
	return o
}

func (o LookupVerifiedAccessTrustProviderResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupVerifiedAccessTrustProviderResult] {
	return pulumix.Output[LookupVerifiedAccessTrustProviderResult]{
		OutputState: o.OutputState,
	}
}

// The creation time.
func (o LookupVerifiedAccessTrustProviderResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVerifiedAccessTrustProviderResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// A description for the Amazon Web Services Verified Access trust provider.
func (o LookupVerifiedAccessTrustProviderResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVerifiedAccessTrustProviderResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The last updated time.
func (o LookupVerifiedAccessTrustProviderResultOutput) LastUpdatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVerifiedAccessTrustProviderResult) *string { return v.LastUpdatedTime }).(pulumi.StringPtrOutput)
}

func (o LookupVerifiedAccessTrustProviderResultOutput) OidcOptions() VerifiedAccessTrustProviderOidcOptionsPtrOutput {
	return o.ApplyT(func(v LookupVerifiedAccessTrustProviderResult) *VerifiedAccessTrustProviderOidcOptions {
		return v.OidcOptions
	}).(VerifiedAccessTrustProviderOidcOptionsPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupVerifiedAccessTrustProviderResultOutput) Tags() VerifiedAccessTrustProviderTagArrayOutput {
	return o.ApplyT(func(v LookupVerifiedAccessTrustProviderResult) []VerifiedAccessTrustProviderTag { return v.Tags }).(VerifiedAccessTrustProviderTagArrayOutput)
}

// The ID of the Amazon Web Services Verified Access trust provider.
func (o LookupVerifiedAccessTrustProviderResultOutput) VerifiedAccessTrustProviderId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVerifiedAccessTrustProviderResult) *string { return v.VerifiedAccessTrustProviderId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVerifiedAccessTrustProviderResultOutput{})
}
