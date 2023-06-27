// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appstream

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppStream::AppBlockBuilder.
func LookupAppBlockBuilder(ctx *pulumi.Context, args *LookupAppBlockBuilderArgs, opts ...pulumi.InvokeOption) (*LookupAppBlockBuilderResult, error) {
	var rv LookupAppBlockBuilderResult
	err := ctx.Invoke("aws-native:appstream:getAppBlockBuilder", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAppBlockBuilderArgs struct {
	Name string `pulumi:"name"`
}

type LookupAppBlockBuilderResult struct {
	AccessEndpoints             []AppBlockBuilderAccessEndpoint `pulumi:"accessEndpoints"`
	Arn                         *string                         `pulumi:"arn"`
	CreatedTime                 *string                         `pulumi:"createdTime"`
	Description                 *string                         `pulumi:"description"`
	DisplayName                 *string                         `pulumi:"displayName"`
	EnableDefaultInternetAccess *bool                           `pulumi:"enableDefaultInternetAccess"`
	IamRoleArn                  *string                         `pulumi:"iamRoleArn"`
	InstanceType                *string                         `pulumi:"instanceType"`
	Platform                    *string                         `pulumi:"platform"`
	VpcConfig                   *AppBlockBuilderVpcConfig       `pulumi:"vpcConfig"`
}

func LookupAppBlockBuilderOutput(ctx *pulumi.Context, args LookupAppBlockBuilderOutputArgs, opts ...pulumi.InvokeOption) LookupAppBlockBuilderResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAppBlockBuilderResult, error) {
			args := v.(LookupAppBlockBuilderArgs)
			r, err := LookupAppBlockBuilder(ctx, &args, opts...)
			var s LookupAppBlockBuilderResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAppBlockBuilderResultOutput)
}

type LookupAppBlockBuilderOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupAppBlockBuilderOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAppBlockBuilderArgs)(nil)).Elem()
}

type LookupAppBlockBuilderResultOutput struct{ *pulumi.OutputState }

func (LookupAppBlockBuilderResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAppBlockBuilderResult)(nil)).Elem()
}

func (o LookupAppBlockBuilderResultOutput) ToLookupAppBlockBuilderResultOutput() LookupAppBlockBuilderResultOutput {
	return o
}

func (o LookupAppBlockBuilderResultOutput) ToLookupAppBlockBuilderResultOutputWithContext(ctx context.Context) LookupAppBlockBuilderResultOutput {
	return o
}

func (o LookupAppBlockBuilderResultOutput) AccessEndpoints() AppBlockBuilderAccessEndpointArrayOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) []AppBlockBuilderAccessEndpoint { return v.AccessEndpoints }).(AppBlockBuilderAccessEndpointArrayOutput)
}

func (o LookupAppBlockBuilderResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) CreatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.CreatedTime }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) EnableDefaultInternetAccess() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *bool { return v.EnableDefaultInternetAccess }).(pulumi.BoolPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) IamRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.IamRoleArn }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) InstanceType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.InstanceType }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) Platform() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *string { return v.Platform }).(pulumi.StringPtrOutput)
}

func (o LookupAppBlockBuilderResultOutput) VpcConfig() AppBlockBuilderVpcConfigPtrOutput {
	return o.ApplyT(func(v LookupAppBlockBuilderResult) *AppBlockBuilderVpcConfig { return v.VpcConfig }).(AppBlockBuilderVpcConfigPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAppBlockBuilderResultOutput{})
}
