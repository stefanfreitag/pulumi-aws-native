// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::RDS::DBProxy
func LookupDbProxy(ctx *pulumi.Context, args *LookupDbProxyArgs, opts ...pulumi.InvokeOption) (*LookupDbProxyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDbProxyResult
	err := ctx.Invoke("aws-native:rds:getDbProxy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDbProxyArgs struct {
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName string `pulumi:"dbProxyName"`
}

type LookupDbProxyResult struct {
	// The authorization mechanism that the proxy uses.
	Auth []DbProxyAuthFormat `pulumi:"auth"`
	// The Amazon Resource Name (ARN) for the proxy.
	DbProxyArn *string `pulumi:"dbProxyArn"`
	// Whether the proxy includes detailed information about SQL statements in its logs.
	DebugLogging *bool `pulumi:"debugLogging"`
	// The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.
	Endpoint *string `pulumi:"endpoint"`
	// The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.
	IdleClientTimeout *int `pulumi:"idleClientTimeout"`
	// A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
	RequireTls *bool `pulumi:"requireTls"`
	// The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
	RoleArn *string `pulumi:"roleArn"`
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
	Tags []aws.Tag `pulumi:"tags"`
	// VPC ID to associate with the new DB proxy.
	VpcId *string `pulumi:"vpcId"`
	// VPC security group IDs to associate with the new proxy.
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
}

func LookupDbProxyOutput(ctx *pulumi.Context, args LookupDbProxyOutputArgs, opts ...pulumi.InvokeOption) LookupDbProxyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDbProxyResult, error) {
			args := v.(LookupDbProxyArgs)
			r, err := LookupDbProxy(ctx, &args, opts...)
			var s LookupDbProxyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDbProxyResultOutput)
}

type LookupDbProxyOutputArgs struct {
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName pulumi.StringInput `pulumi:"dbProxyName"`
}

func (LookupDbProxyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDbProxyArgs)(nil)).Elem()
}

type LookupDbProxyResultOutput struct{ *pulumi.OutputState }

func (LookupDbProxyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDbProxyResult)(nil)).Elem()
}

func (o LookupDbProxyResultOutput) ToLookupDbProxyResultOutput() LookupDbProxyResultOutput {
	return o
}

func (o LookupDbProxyResultOutput) ToLookupDbProxyResultOutputWithContext(ctx context.Context) LookupDbProxyResultOutput {
	return o
}

// The authorization mechanism that the proxy uses.
func (o LookupDbProxyResultOutput) Auth() DbProxyAuthFormatArrayOutput {
	return o.ApplyT(func(v LookupDbProxyResult) []DbProxyAuthFormat { return v.Auth }).(DbProxyAuthFormatArrayOutput)
}

// The Amazon Resource Name (ARN) for the proxy.
func (o LookupDbProxyResultOutput) DbProxyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *string { return v.DbProxyArn }).(pulumi.StringPtrOutput)
}

// Whether the proxy includes detailed information about SQL statements in its logs.
func (o LookupDbProxyResultOutput) DebugLogging() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *bool { return v.DebugLogging }).(pulumi.BoolPtrOutput)
}

// The endpoint that you can use to connect to the proxy. You include the endpoint value in the connection string for a database client application.
func (o LookupDbProxyResultOutput) Endpoint() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *string { return v.Endpoint }).(pulumi.StringPtrOutput)
}

// The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it.
func (o LookupDbProxyResultOutput) IdleClientTimeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *int { return v.IdleClientTimeout }).(pulumi.IntPtrOutput)
}

// A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
func (o LookupDbProxyResultOutput) RequireTls() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *bool { return v.RequireTls }).(pulumi.BoolPtrOutput)
}

// The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
func (o LookupDbProxyResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

// An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
func (o LookupDbProxyResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDbProxyResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// VPC ID to associate with the new DB proxy.
func (o LookupDbProxyResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbProxyResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

// VPC security group IDs to associate with the new proxy.
func (o LookupDbProxyResultOutput) VpcSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDbProxyResult) []string { return v.VpcSecurityGroupIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDbProxyResultOutput{})
}
