// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudfront

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::CloudFront::Distribution
func LookupDistribution(ctx *pulumi.Context, args *LookupDistributionArgs, opts ...pulumi.InvokeOption) (*LookupDistributionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDistributionResult
	err := ctx.Invoke("aws-native:cloudfront:getDistribution", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDistributionArgs struct {
	Id string `pulumi:"id"`
}

type LookupDistributionResult struct {
	DistributionConfig *DistributionConfig `pulumi:"distributionConfig"`
	DomainName         *string             `pulumi:"domainName"`
	Id                 *string             `pulumi:"id"`
	Tags               []DistributionTag   `pulumi:"tags"`
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
	Id pulumi.StringInput `pulumi:"id"`
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

func (o LookupDistributionResultOutput) DistributionConfig() DistributionConfigPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *DistributionConfig { return v.DistributionConfig }).(DistributionConfigPtrOutput)
}

func (o LookupDistributionResultOutput) DomainName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *string { return v.DomainName }).(pulumi.StringPtrOutput)
}

func (o LookupDistributionResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDistributionResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDistributionResultOutput) Tags() DistributionTagArrayOutput {
	return o.ApplyT(func(v LookupDistributionResult) []DistributionTag { return v.Tags }).(DistributionTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDistributionResultOutput{})
}
