// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package greengrass

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Greengrass::DeviceDefinition
func LookupDeviceDefinition(ctx *pulumi.Context, args *LookupDeviceDefinitionArgs, opts ...pulumi.InvokeOption) (*LookupDeviceDefinitionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDeviceDefinitionResult
	err := ctx.Invoke("aws-native:greengrass:getDeviceDefinition", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDeviceDefinitionArgs struct {
	Id string `pulumi:"id"`
}

type LookupDeviceDefinitionResult struct {
	Arn              *string     `pulumi:"arn"`
	Id               *string     `pulumi:"id"`
	LatestVersionArn *string     `pulumi:"latestVersionArn"`
	Name             *string     `pulumi:"name"`
	Tags             interface{} `pulumi:"tags"`
}

func LookupDeviceDefinitionOutput(ctx *pulumi.Context, args LookupDeviceDefinitionOutputArgs, opts ...pulumi.InvokeOption) LookupDeviceDefinitionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDeviceDefinitionResult, error) {
			args := v.(LookupDeviceDefinitionArgs)
			r, err := LookupDeviceDefinition(ctx, &args, opts...)
			var s LookupDeviceDefinitionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDeviceDefinitionResultOutput)
}

type LookupDeviceDefinitionOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDeviceDefinitionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDeviceDefinitionArgs)(nil)).Elem()
}

type LookupDeviceDefinitionResultOutput struct{ *pulumi.OutputState }

func (LookupDeviceDefinitionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDeviceDefinitionResult)(nil)).Elem()
}

func (o LookupDeviceDefinitionResultOutput) ToLookupDeviceDefinitionResultOutput() LookupDeviceDefinitionResultOutput {
	return o
}

func (o LookupDeviceDefinitionResultOutput) ToLookupDeviceDefinitionResultOutputWithContext(ctx context.Context) LookupDeviceDefinitionResultOutput {
	return o
}

func (o LookupDeviceDefinitionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDeviceDefinitionResult] {
	return pulumix.Output[LookupDeviceDefinitionResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupDeviceDefinitionResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeviceDefinitionResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupDeviceDefinitionResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeviceDefinitionResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDeviceDefinitionResultOutput) LatestVersionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeviceDefinitionResult) *string { return v.LatestVersionArn }).(pulumi.StringPtrOutput)
}

func (o LookupDeviceDefinitionResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeviceDefinitionResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupDeviceDefinitionResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupDeviceDefinitionResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDeviceDefinitionResultOutput{})
}
