// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package refactorspaces

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::RefactorSpaces::Application Resource Type
func LookupApplication(ctx *pulumi.Context, args *LookupApplicationArgs, opts ...pulumi.InvokeOption) (*LookupApplicationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupApplicationResult
	err := ctx.Invoke("aws-native:refactorspaces:getApplication", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupApplicationArgs struct {
	ApplicationIdentifier string `pulumi:"applicationIdentifier"`
	EnvironmentIdentifier string `pulumi:"environmentIdentifier"`
}

type LookupApplicationResult struct {
	ApiGatewayId          *string `pulumi:"apiGatewayId"`
	ApplicationIdentifier *string `pulumi:"applicationIdentifier"`
	Arn                   *string `pulumi:"arn"`
	NlbArn                *string `pulumi:"nlbArn"`
	NlbName               *string `pulumi:"nlbName"`
	ProxyUrl              *string `pulumi:"proxyUrl"`
	StageName             *string `pulumi:"stageName"`
	// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
	Tags      []aws.Tag `pulumi:"tags"`
	VpcLinkId *string   `pulumi:"vpcLinkId"`
}

func LookupApplicationOutput(ctx *pulumi.Context, args LookupApplicationOutputArgs, opts ...pulumi.InvokeOption) LookupApplicationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupApplicationResult, error) {
			args := v.(LookupApplicationArgs)
			r, err := LookupApplication(ctx, &args, opts...)
			var s LookupApplicationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupApplicationResultOutput)
}

type LookupApplicationOutputArgs struct {
	ApplicationIdentifier pulumi.StringInput `pulumi:"applicationIdentifier"`
	EnvironmentIdentifier pulumi.StringInput `pulumi:"environmentIdentifier"`
}

func (LookupApplicationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationArgs)(nil)).Elem()
}

type LookupApplicationResultOutput struct{ *pulumi.OutputState }

func (LookupApplicationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationResult)(nil)).Elem()
}

func (o LookupApplicationResultOutput) ToLookupApplicationResultOutput() LookupApplicationResultOutput {
	return o
}

func (o LookupApplicationResultOutput) ToLookupApplicationResultOutputWithContext(ctx context.Context) LookupApplicationResultOutput {
	return o
}

func (o LookupApplicationResultOutput) ApiGatewayId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.ApiGatewayId }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) ApplicationIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.ApplicationIdentifier }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) NlbArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.NlbArn }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) NlbName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.NlbName }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) ProxyUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.ProxyUrl }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) StageName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.StageName }).(pulumi.StringPtrOutput)
}

// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
func (o LookupApplicationResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupApplicationResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func (o LookupApplicationResultOutput) VpcLinkId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.VpcLinkId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApplicationResultOutput{})
}
