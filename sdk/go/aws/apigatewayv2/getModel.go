// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ApiGatewayV2::Model
func LookupModel(ctx *pulumi.Context, args *LookupModelArgs, opts ...pulumi.InvokeOption) (*LookupModelResult, error) {
	var rv LookupModelResult
	err := ctx.Invoke("aws-native:apigatewayv2:getModel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupModelArgs struct {
	ApiId   string `pulumi:"apiId"`
	ModelId string `pulumi:"modelId"`
}

type LookupModelResult struct {
	ContentType *string     `pulumi:"contentType"`
	Description *string     `pulumi:"description"`
	ModelId     *string     `pulumi:"modelId"`
	Name        *string     `pulumi:"name"`
	Schema      interface{} `pulumi:"schema"`
}

func LookupModelOutput(ctx *pulumi.Context, args LookupModelOutputArgs, opts ...pulumi.InvokeOption) LookupModelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupModelResult, error) {
			args := v.(LookupModelArgs)
			r, err := LookupModel(ctx, &args, opts...)
			var s LookupModelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupModelResultOutput)
}

type LookupModelOutputArgs struct {
	ApiId   pulumi.StringInput `pulumi:"apiId"`
	ModelId pulumi.StringInput `pulumi:"modelId"`
}

func (LookupModelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupModelArgs)(nil)).Elem()
}

type LookupModelResultOutput struct{ *pulumi.OutputState }

func (LookupModelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupModelResult)(nil)).Elem()
}

func (o LookupModelResultOutput) ToLookupModelResultOutput() LookupModelResultOutput {
	return o
}

func (o LookupModelResultOutput) ToLookupModelResultOutputWithContext(ctx context.Context) LookupModelResultOutput {
	return o
}

func (o LookupModelResultOutput) ContentType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelResult) *string { return v.ContentType }).(pulumi.StringPtrOutput)
}

func (o LookupModelResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupModelResultOutput) ModelId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelResult) *string { return v.ModelId }).(pulumi.StringPtrOutput)
}

func (o LookupModelResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupModelResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupModelResultOutput) Schema() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupModelResult) interface{} { return v.Schema }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupModelResultOutput{})
}
