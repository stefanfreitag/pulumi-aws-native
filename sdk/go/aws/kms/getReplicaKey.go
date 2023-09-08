// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).
func LookupReplicaKey(ctx *pulumi.Context, args *LookupReplicaKeyArgs, opts ...pulumi.InvokeOption) (*LookupReplicaKeyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupReplicaKeyResult
	err := ctx.Invoke("aws-native:kms:getReplicaKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupReplicaKeyArgs struct {
	KeyId string `pulumi:"keyId"`
}

type LookupReplicaKeyResult struct {
	Arn *string `pulumi:"arn"`
	// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
	Description *string `pulumi:"description"`
	// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
	Enabled *bool   `pulumi:"enabled"`
	KeyId   *string `pulumi:"keyId"`
	// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
	KeyPolicy interface{} `pulumi:"keyPolicy"`
	// An array of key-value pairs to apply to this resource.
	Tags []ReplicaKeyTag `pulumi:"tags"`
}

func LookupReplicaKeyOutput(ctx *pulumi.Context, args LookupReplicaKeyOutputArgs, opts ...pulumi.InvokeOption) LookupReplicaKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupReplicaKeyResult, error) {
			args := v.(LookupReplicaKeyArgs)
			r, err := LookupReplicaKey(ctx, &args, opts...)
			var s LookupReplicaKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupReplicaKeyResultOutput)
}

type LookupReplicaKeyOutputArgs struct {
	KeyId pulumi.StringInput `pulumi:"keyId"`
}

func (LookupReplicaKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupReplicaKeyArgs)(nil)).Elem()
}

type LookupReplicaKeyResultOutput struct{ *pulumi.OutputState }

func (LookupReplicaKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupReplicaKeyResult)(nil)).Elem()
}

func (o LookupReplicaKeyResultOutput) ToLookupReplicaKeyResultOutput() LookupReplicaKeyResultOutput {
	return o
}

func (o LookupReplicaKeyResultOutput) ToLookupReplicaKeyResultOutputWithContext(ctx context.Context) LookupReplicaKeyResultOutput {
	return o
}

func (o LookupReplicaKeyResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupReplicaKeyResult] {
	return pulumix.Output[LookupReplicaKeyResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupReplicaKeyResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicaKeyResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
func (o LookupReplicaKeyResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicaKeyResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
func (o LookupReplicaKeyResultOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupReplicaKeyResult) *bool { return v.Enabled }).(pulumi.BoolPtrOutput)
}

func (o LookupReplicaKeyResultOutput) KeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicaKeyResult) *string { return v.KeyId }).(pulumi.StringPtrOutput)
}

// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
func (o LookupReplicaKeyResultOutput) KeyPolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupReplicaKeyResult) interface{} { return v.KeyPolicy }).(pulumi.AnyOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupReplicaKeyResultOutput) Tags() ReplicaKeyTagArrayOutput {
	return o.ApplyT(func(v LookupReplicaKeyResult) []ReplicaKeyTag { return v.Tags }).(ReplicaKeyTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupReplicaKeyResultOutput{})
}
