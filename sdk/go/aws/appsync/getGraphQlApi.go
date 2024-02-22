// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppSync::GraphQLApi
func LookupGraphQlApi(ctx *pulumi.Context, args *LookupGraphQlApiArgs, opts ...pulumi.InvokeOption) (*LookupGraphQlApiResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGraphQlApiResult
	err := ctx.Invoke("aws-native:appsync:getGraphQlApi", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupGraphQlApiArgs struct {
	Id string `pulumi:"id"`
}

type LookupGraphQlApiResult struct {
	AdditionalAuthenticationProviders []GraphQlApiAdditionalAuthenticationProvider `pulumi:"additionalAuthenticationProviders"`
	ApiId                             *string                                      `pulumi:"apiId"`
	ApiType                           *string                                      `pulumi:"apiType"`
	Arn                               *string                                      `pulumi:"arn"`
	AuthenticationType                *string                                      `pulumi:"authenticationType"`
	EnhancedMetricsConfig             *GraphQlApiEnhancedMetricsConfig             `pulumi:"enhancedMetricsConfig"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::AppSync::GraphQLApi` for more information about the expected schema for this property.
	EnvironmentVariables      interface{}                       `pulumi:"environmentVariables"`
	GraphQlDns                *string                           `pulumi:"graphQlDns"`
	GraphQlEndpointArn        *string                           `pulumi:"graphQlEndpointArn"`
	GraphQlUrl                *string                           `pulumi:"graphQlUrl"`
	Id                        *string                           `pulumi:"id"`
	IntrospectionConfig       *string                           `pulumi:"introspectionConfig"`
	LambdaAuthorizerConfig    *GraphQlApiLambdaAuthorizerConfig `pulumi:"lambdaAuthorizerConfig"`
	LogConfig                 *GraphQlApiLogConfig              `pulumi:"logConfig"`
	MergedApiExecutionRoleArn *string                           `pulumi:"mergedApiExecutionRoleArn"`
	Name                      *string                           `pulumi:"name"`
	OpenIdConnectConfig       *GraphQlApiOpenIdConnectConfig    `pulumi:"openIdConnectConfig"`
	OwnerContact              *string                           `pulumi:"ownerContact"`
	QueryDepthLimit           *int                              `pulumi:"queryDepthLimit"`
	RealtimeDns               *string                           `pulumi:"realtimeDns"`
	RealtimeUrl               *string                           `pulumi:"realtimeUrl"`
	ResolverCountLimit        *int                              `pulumi:"resolverCountLimit"`
	Tags                      []aws.Tag                         `pulumi:"tags"`
	UserPoolConfig            *GraphQlApiUserPoolConfig         `pulumi:"userPoolConfig"`
	Visibility                *string                           `pulumi:"visibility"`
	XrayEnabled               *bool                             `pulumi:"xrayEnabled"`
}

func LookupGraphQlApiOutput(ctx *pulumi.Context, args LookupGraphQlApiOutputArgs, opts ...pulumi.InvokeOption) LookupGraphQlApiResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGraphQlApiResult, error) {
			args := v.(LookupGraphQlApiArgs)
			r, err := LookupGraphQlApi(ctx, &args, opts...)
			var s LookupGraphQlApiResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGraphQlApiResultOutput)
}

type LookupGraphQlApiOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupGraphQlApiOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGraphQlApiArgs)(nil)).Elem()
}

type LookupGraphQlApiResultOutput struct{ *pulumi.OutputState }

func (LookupGraphQlApiResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGraphQlApiResult)(nil)).Elem()
}

func (o LookupGraphQlApiResultOutput) ToLookupGraphQlApiResultOutput() LookupGraphQlApiResultOutput {
	return o
}

func (o LookupGraphQlApiResultOutput) ToLookupGraphQlApiResultOutputWithContext(ctx context.Context) LookupGraphQlApiResultOutput {
	return o
}

func (o LookupGraphQlApiResultOutput) AdditionalAuthenticationProviders() GraphQlApiAdditionalAuthenticationProviderArrayOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) []GraphQlApiAdditionalAuthenticationProvider {
		return v.AdditionalAuthenticationProviders
	}).(GraphQlApiAdditionalAuthenticationProviderArrayOutput)
}

func (o LookupGraphQlApiResultOutput) ApiId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.ApiId }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) ApiType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.ApiType }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) AuthenticationType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.AuthenticationType }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) EnhancedMetricsConfig() GraphQlApiEnhancedMetricsConfigPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *GraphQlApiEnhancedMetricsConfig { return v.EnhancedMetricsConfig }).(GraphQlApiEnhancedMetricsConfigPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::AppSync::GraphQLApi` for more information about the expected schema for this property.
func (o LookupGraphQlApiResultOutput) EnvironmentVariables() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) interface{} { return v.EnvironmentVariables }).(pulumi.AnyOutput)
}

func (o LookupGraphQlApiResultOutput) GraphQlDns() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.GraphQlDns }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) GraphQlEndpointArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.GraphQlEndpointArn }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) GraphQlUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.GraphQlUrl }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) IntrospectionConfig() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.IntrospectionConfig }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) LambdaAuthorizerConfig() GraphQlApiLambdaAuthorizerConfigPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *GraphQlApiLambdaAuthorizerConfig { return v.LambdaAuthorizerConfig }).(GraphQlApiLambdaAuthorizerConfigPtrOutput)
}

func (o LookupGraphQlApiResultOutput) LogConfig() GraphQlApiLogConfigPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *GraphQlApiLogConfig { return v.LogConfig }).(GraphQlApiLogConfigPtrOutput)
}

func (o LookupGraphQlApiResultOutput) MergedApiExecutionRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.MergedApiExecutionRoleArn }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) OpenIdConnectConfig() GraphQlApiOpenIdConnectConfigPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *GraphQlApiOpenIdConnectConfig { return v.OpenIdConnectConfig }).(GraphQlApiOpenIdConnectConfigPtrOutput)
}

func (o LookupGraphQlApiResultOutput) OwnerContact() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.OwnerContact }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) QueryDepthLimit() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *int { return v.QueryDepthLimit }).(pulumi.IntPtrOutput)
}

func (o LookupGraphQlApiResultOutput) RealtimeDns() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.RealtimeDns }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) RealtimeUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.RealtimeUrl }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) ResolverCountLimit() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *int { return v.ResolverCountLimit }).(pulumi.IntPtrOutput)
}

func (o LookupGraphQlApiResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func (o LookupGraphQlApiResultOutput) UserPoolConfig() GraphQlApiUserPoolConfigPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *GraphQlApiUserPoolConfig { return v.UserPoolConfig }).(GraphQlApiUserPoolConfigPtrOutput)
}

func (o LookupGraphQlApiResultOutput) Visibility() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *string { return v.Visibility }).(pulumi.StringPtrOutput)
}

func (o LookupGraphQlApiResultOutput) XrayEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupGraphQlApiResult) *bool { return v.XrayEnabled }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGraphQlApiResultOutput{})
}
