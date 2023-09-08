// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ApiGateway::GatewayResponse
func LookupGatewayResponse(ctx *pulumi.Context, args *LookupGatewayResponseArgs, opts ...pulumi.InvokeOption) (*LookupGatewayResponseResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGatewayResponseResult
	err := ctx.Invoke("aws-native:apigateway:getGatewayResponse", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupGatewayResponseArgs struct {
	Id string `pulumi:"id"`
}

type LookupGatewayResponseResult struct {
	Id                 *string     `pulumi:"id"`
	ResponseParameters interface{} `pulumi:"responseParameters"`
	ResponseTemplates  interface{} `pulumi:"responseTemplates"`
	StatusCode         *string     `pulumi:"statusCode"`
}

func LookupGatewayResponseOutput(ctx *pulumi.Context, args LookupGatewayResponseOutputArgs, opts ...pulumi.InvokeOption) LookupGatewayResponseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGatewayResponseResult, error) {
			args := v.(LookupGatewayResponseArgs)
			r, err := LookupGatewayResponse(ctx, &args, opts...)
			var s LookupGatewayResponseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGatewayResponseResultOutput)
}

type LookupGatewayResponseOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupGatewayResponseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGatewayResponseArgs)(nil)).Elem()
}

type LookupGatewayResponseResultOutput struct{ *pulumi.OutputState }

func (LookupGatewayResponseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGatewayResponseResult)(nil)).Elem()
}

func (o LookupGatewayResponseResultOutput) ToLookupGatewayResponseResultOutput() LookupGatewayResponseResultOutput {
	return o
}

func (o LookupGatewayResponseResultOutput) ToLookupGatewayResponseResultOutputWithContext(ctx context.Context) LookupGatewayResponseResultOutput {
	return o
}

func (o LookupGatewayResponseResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupGatewayResponseResult] {
	return pulumix.Output[LookupGatewayResponseResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupGatewayResponseResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGatewayResponseResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupGatewayResponseResultOutput) ResponseParameters() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupGatewayResponseResult) interface{} { return v.ResponseParameters }).(pulumi.AnyOutput)
}

func (o LookupGatewayResponseResultOutput) ResponseTemplates() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupGatewayResponseResult) interface{} { return v.ResponseTemplates }).(pulumi.AnyOutput)
}

func (o LookupGatewayResponseResultOutput) StatusCode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGatewayResponseResult) *string { return v.StatusCode }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGatewayResponseResultOutput{})
}
