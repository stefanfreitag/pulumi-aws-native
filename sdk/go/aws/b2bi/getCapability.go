// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package b2bi

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::B2BI::Capability Resource Type
func LookupCapability(ctx *pulumi.Context, args *LookupCapabilityArgs, opts ...pulumi.InvokeOption) (*LookupCapabilityResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCapabilityResult
	err := ctx.Invoke("aws-native:b2bi:getCapability", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCapabilityArgs struct {
	CapabilityId string `pulumi:"capabilityId"`
}

type LookupCapabilityResult struct {
	CapabilityArn         *string                            `pulumi:"capabilityArn"`
	CapabilityId          *string                            `pulumi:"capabilityId"`
	Configuration         *CapabilityConfigurationProperties `pulumi:"configuration"`
	CreatedAt             *string                            `pulumi:"createdAt"`
	InstructionsDocuments []CapabilityS3Location             `pulumi:"instructionsDocuments"`
	ModifiedAt            *string                            `pulumi:"modifiedAt"`
	Name                  *string                            `pulumi:"name"`
	Tags                  []aws.Tag                          `pulumi:"tags"`
}

func LookupCapabilityOutput(ctx *pulumi.Context, args LookupCapabilityOutputArgs, opts ...pulumi.InvokeOption) LookupCapabilityResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCapabilityResult, error) {
			args := v.(LookupCapabilityArgs)
			r, err := LookupCapability(ctx, &args, opts...)
			var s LookupCapabilityResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCapabilityResultOutput)
}

type LookupCapabilityOutputArgs struct {
	CapabilityId pulumi.StringInput `pulumi:"capabilityId"`
}

func (LookupCapabilityOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCapabilityArgs)(nil)).Elem()
}

type LookupCapabilityResultOutput struct{ *pulumi.OutputState }

func (LookupCapabilityResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCapabilityResult)(nil)).Elem()
}

func (o LookupCapabilityResultOutput) ToLookupCapabilityResultOutput() LookupCapabilityResultOutput {
	return o
}

func (o LookupCapabilityResultOutput) ToLookupCapabilityResultOutputWithContext(ctx context.Context) LookupCapabilityResultOutput {
	return o
}

func (o LookupCapabilityResultOutput) CapabilityArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapabilityResult) *string { return v.CapabilityArn }).(pulumi.StringPtrOutput)
}

func (o LookupCapabilityResultOutput) CapabilityId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapabilityResult) *string { return v.CapabilityId }).(pulumi.StringPtrOutput)
}

func (o LookupCapabilityResultOutput) Configuration() CapabilityConfigurationPropertiesPtrOutput {
	return o.ApplyT(func(v LookupCapabilityResult) *CapabilityConfigurationProperties { return v.Configuration }).(CapabilityConfigurationPropertiesPtrOutput)
}

func (o LookupCapabilityResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapabilityResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupCapabilityResultOutput) InstructionsDocuments() CapabilityS3LocationArrayOutput {
	return o.ApplyT(func(v LookupCapabilityResult) []CapabilityS3Location { return v.InstructionsDocuments }).(CapabilityS3LocationArrayOutput)
}

func (o LookupCapabilityResultOutput) ModifiedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapabilityResult) *string { return v.ModifiedAt }).(pulumi.StringPtrOutput)
}

func (o LookupCapabilityResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapabilityResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupCapabilityResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupCapabilityResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCapabilityResultOutput{})
}
