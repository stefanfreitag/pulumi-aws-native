// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Connect::Instance
func LookupInstance(ctx *pulumi.Context, args *LookupInstanceArgs, opts ...pulumi.InvokeOption) (*LookupInstanceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupInstanceResult
	err := ctx.Invoke("aws-native:connect:getInstance", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupInstanceArgs struct {
	// An instanceArn is automatically generated on creation based on instanceId.
	Arn string `pulumi:"arn"`
}

type LookupInstanceResult struct {
	// An instanceArn is automatically generated on creation based on instanceId.
	Arn *string `pulumi:"arn"`
	// The attributes for the instance.
	Attributes *InstanceAttributes `pulumi:"attributes"`
	// Timestamp of instance creation logged as part of instance creation.
	CreatedTime *string `pulumi:"createdTime"`
	// An instanceId is automatically generated on creation and assigned as the unique identifier.
	Id *string `pulumi:"id"`
	// Specifies the creation status of new instance.
	InstanceStatus *InstanceStatus `pulumi:"instanceStatus"`
	// Service linked role created as part of instance creation.
	ServiceRole *string `pulumi:"serviceRole"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupInstanceOutput(ctx *pulumi.Context, args LookupInstanceOutputArgs, opts ...pulumi.InvokeOption) LookupInstanceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInstanceResult, error) {
			args := v.(LookupInstanceArgs)
			r, err := LookupInstance(ctx, &args, opts...)
			var s LookupInstanceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupInstanceResultOutput)
}

type LookupInstanceOutputArgs struct {
	// An instanceArn is automatically generated on creation based on instanceId.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupInstanceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceArgs)(nil)).Elem()
}

type LookupInstanceResultOutput struct{ *pulumi.OutputState }

func (LookupInstanceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceResult)(nil)).Elem()
}

func (o LookupInstanceResultOutput) ToLookupInstanceResultOutput() LookupInstanceResultOutput {
	return o
}

func (o LookupInstanceResultOutput) ToLookupInstanceResultOutputWithContext(ctx context.Context) LookupInstanceResultOutput {
	return o
}

// An instanceArn is automatically generated on creation based on instanceId.
func (o LookupInstanceResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The attributes for the instance.
func (o LookupInstanceResultOutput) Attributes() InstanceAttributesPtrOutput {
	return o.ApplyT(func(v LookupInstanceResult) *InstanceAttributes { return v.Attributes }).(InstanceAttributesPtrOutput)
}

// Timestamp of instance creation logged as part of instance creation.
func (o LookupInstanceResultOutput) CreatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceResult) *string { return v.CreatedTime }).(pulumi.StringPtrOutput)
}

// An instanceId is automatically generated on creation and assigned as the unique identifier.
func (o LookupInstanceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Specifies the creation status of new instance.
func (o LookupInstanceResultOutput) InstanceStatus() InstanceStatusPtrOutput {
	return o.ApplyT(func(v LookupInstanceResult) *InstanceStatus { return v.InstanceStatus }).(InstanceStatusPtrOutput)
}

// Service linked role created as part of instance creation.
func (o LookupInstanceResultOutput) ServiceRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceResult) *string { return v.ServiceRole }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupInstanceResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupInstanceResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInstanceResultOutput{})
}
