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

// Resource Type definition for AWS::Greengrass::ResourceDefinition
func LookupResourceDefinition(ctx *pulumi.Context, args *LookupResourceDefinitionArgs, opts ...pulumi.InvokeOption) (*LookupResourceDefinitionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourceDefinitionResult
	err := ctx.Invoke("aws-native:greengrass:getResourceDefinition", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourceDefinitionArgs struct {
	Id string `pulumi:"id"`
}

type LookupResourceDefinitionResult struct {
	Arn              *string     `pulumi:"arn"`
	Id               *string     `pulumi:"id"`
	LatestVersionArn *string     `pulumi:"latestVersionArn"`
	Name             *string     `pulumi:"name"`
	Tags             interface{} `pulumi:"tags"`
}

func LookupResourceDefinitionOutput(ctx *pulumi.Context, args LookupResourceDefinitionOutputArgs, opts ...pulumi.InvokeOption) LookupResourceDefinitionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResourceDefinitionResult, error) {
			args := v.(LookupResourceDefinitionArgs)
			r, err := LookupResourceDefinition(ctx, &args, opts...)
			var s LookupResourceDefinitionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResourceDefinitionResultOutput)
}

type LookupResourceDefinitionOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupResourceDefinitionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceDefinitionArgs)(nil)).Elem()
}

type LookupResourceDefinitionResultOutput struct{ *pulumi.OutputState }

func (LookupResourceDefinitionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceDefinitionResult)(nil)).Elem()
}

func (o LookupResourceDefinitionResultOutput) ToLookupResourceDefinitionResultOutput() LookupResourceDefinitionResultOutput {
	return o
}

func (o LookupResourceDefinitionResultOutput) ToLookupResourceDefinitionResultOutputWithContext(ctx context.Context) LookupResourceDefinitionResultOutput {
	return o
}

func (o LookupResourceDefinitionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupResourceDefinitionResult] {
	return pulumix.Output[LookupResourceDefinitionResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupResourceDefinitionResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceDefinitionResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupResourceDefinitionResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceDefinitionResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupResourceDefinitionResultOutput) LatestVersionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceDefinitionResult) *string { return v.LatestVersionArn }).(pulumi.StringPtrOutput)
}

func (o LookupResourceDefinitionResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceDefinitionResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupResourceDefinitionResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupResourceDefinitionResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourceDefinitionResultOutput{})
}
