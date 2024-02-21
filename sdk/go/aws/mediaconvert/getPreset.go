// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconvert

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::MediaConvert::Preset
func LookupPreset(ctx *pulumi.Context, args *LookupPresetArgs, opts ...pulumi.InvokeOption) (*LookupPresetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPresetResult
	err := ctx.Invoke("aws-native:mediaconvert:getPreset", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPresetArgs struct {
	Id string `pulumi:"id"`
}

type LookupPresetResult struct {
	Arn         *string `pulumi:"arn"`
	Category    *string `pulumi:"category"`
	Description *string `pulumi:"description"`
	Id          *string `pulumi:"id"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	SettingsJson interface{} `pulumi:"settingsJson"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	Tags interface{} `pulumi:"tags"`
}

func LookupPresetOutput(ctx *pulumi.Context, args LookupPresetOutputArgs, opts ...pulumi.InvokeOption) LookupPresetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPresetResult, error) {
			args := v.(LookupPresetArgs)
			r, err := LookupPreset(ctx, &args, opts...)
			var s LookupPresetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPresetResultOutput)
}

type LookupPresetOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupPresetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPresetArgs)(nil)).Elem()
}

type LookupPresetResultOutput struct{ *pulumi.OutputState }

func (LookupPresetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPresetResult)(nil)).Elem()
}

func (o LookupPresetResultOutput) ToLookupPresetResultOutput() LookupPresetResultOutput {
	return o
}

func (o LookupPresetResultOutput) ToLookupPresetResultOutputWithContext(ctx context.Context) LookupPresetResultOutput {
	return o
}

func (o LookupPresetResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPresetResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupPresetResultOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPresetResult) *string { return v.Category }).(pulumi.StringPtrOutput)
}

func (o LookupPresetResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPresetResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupPresetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPresetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
func (o LookupPresetResultOutput) SettingsJson() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupPresetResult) interface{} { return v.SettingsJson }).(pulumi.AnyOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
func (o LookupPresetResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupPresetResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPresetResultOutput{})
}
