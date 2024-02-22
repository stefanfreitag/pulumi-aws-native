// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::Endpoint
func LookupEndpoint(ctx *pulumi.Context, args *LookupEndpointArgs, opts ...pulumi.InvokeOption) (*LookupEndpointResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEndpointResult
	err := ctx.Invoke("aws-native:sagemaker:getEndpoint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupEndpointArgs struct {
	Id string `pulumi:"id"`
}

type LookupEndpointResult struct {
	DeploymentConfig                 *EndpointDeploymentConfig `pulumi:"deploymentConfig"`
	EndpointConfigName               *string                   `pulumi:"endpointConfigName"`
	ExcludeRetainedVariantProperties []EndpointVariantProperty `pulumi:"excludeRetainedVariantProperties"`
	Id                               *string                   `pulumi:"id"`
	RetainAllVariantProperties       *bool                     `pulumi:"retainAllVariantProperties"`
	RetainDeploymentConfig           *bool                     `pulumi:"retainDeploymentConfig"`
	Tags                             []aws.Tag                 `pulumi:"tags"`
}

func LookupEndpointOutput(ctx *pulumi.Context, args LookupEndpointOutputArgs, opts ...pulumi.InvokeOption) LookupEndpointResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEndpointResult, error) {
			args := v.(LookupEndpointArgs)
			r, err := LookupEndpoint(ctx, &args, opts...)
			var s LookupEndpointResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupEndpointResultOutput)
}

type LookupEndpointOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupEndpointOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEndpointArgs)(nil)).Elem()
}

type LookupEndpointResultOutput struct{ *pulumi.OutputState }

func (LookupEndpointResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEndpointResult)(nil)).Elem()
}

func (o LookupEndpointResultOutput) ToLookupEndpointResultOutput() LookupEndpointResultOutput {
	return o
}

func (o LookupEndpointResultOutput) ToLookupEndpointResultOutputWithContext(ctx context.Context) LookupEndpointResultOutput {
	return o
}

func (o LookupEndpointResultOutput) DeploymentConfig() EndpointDeploymentConfigPtrOutput {
	return o.ApplyT(func(v LookupEndpointResult) *EndpointDeploymentConfig { return v.DeploymentConfig }).(EndpointDeploymentConfigPtrOutput)
}

func (o LookupEndpointResultOutput) EndpointConfigName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEndpointResult) *string { return v.EndpointConfigName }).(pulumi.StringPtrOutput)
}

func (o LookupEndpointResultOutput) ExcludeRetainedVariantProperties() EndpointVariantPropertyArrayOutput {
	return o.ApplyT(func(v LookupEndpointResult) []EndpointVariantProperty { return v.ExcludeRetainedVariantProperties }).(EndpointVariantPropertyArrayOutput)
}

func (o LookupEndpointResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEndpointResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupEndpointResultOutput) RetainAllVariantProperties() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupEndpointResult) *bool { return v.RetainAllVariantProperties }).(pulumi.BoolPtrOutput)
}

func (o LookupEndpointResultOutput) RetainDeploymentConfig() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupEndpointResult) *bool { return v.RetainDeploymentConfig }).(pulumi.BoolPtrOutput)
}

func (o LookupEndpointResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupEndpointResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEndpointResultOutput{})
}
