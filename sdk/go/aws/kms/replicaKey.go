// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).
type ReplicaKey struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	KeyId   pulumi.StringOutput  `pulumi:"keyId"`
	// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
	KeyPolicy pulumi.AnyOutput `pulumi:"keyPolicy"`
	// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
	PendingWindowInDays pulumi.IntPtrOutput `pulumi:"pendingWindowInDays"`
	// Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
	PrimaryKeyArn pulumi.StringOutput `pulumi:"primaryKeyArn"`
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewReplicaKey registers a new resource with the given unique name, arguments, and options.
func NewReplicaKey(ctx *pulumi.Context,
	name string, args *ReplicaKeyArgs, opts ...pulumi.ResourceOption) (*ReplicaKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.KeyPolicy == nil {
		return nil, errors.New("invalid value for required argument 'KeyPolicy'")
	}
	if args.PrimaryKeyArn == nil {
		return nil, errors.New("invalid value for required argument 'PrimaryKeyArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"primaryKeyArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ReplicaKey
	err := ctx.RegisterResource("aws-native:kms:ReplicaKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReplicaKey gets an existing ReplicaKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReplicaKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReplicaKeyState, opts ...pulumi.ResourceOption) (*ReplicaKey, error) {
	var resource ReplicaKey
	err := ctx.ReadResource("aws-native:kms:ReplicaKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReplicaKey resources.
type replicaKeyState struct {
}

type ReplicaKeyState struct {
}

func (ReplicaKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*replicaKeyState)(nil)).Elem()
}

type replicaKeyArgs struct {
	// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
	Description *string `pulumi:"description"`
	// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
	Enabled *bool `pulumi:"enabled"`
	// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
	KeyPolicy interface{} `pulumi:"keyPolicy"`
	// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
	PendingWindowInDays *int `pulumi:"pendingWindowInDays"`
	// Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
	PrimaryKeyArn string `pulumi:"primaryKeyArn"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a ReplicaKey resource.
type ReplicaKeyArgs struct {
	// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
	Description pulumi.StringPtrInput
	// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
	Enabled pulumi.BoolPtrInput
	// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
	KeyPolicy pulumi.Input
	// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
	PendingWindowInDays pulumi.IntPtrInput
	// Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
	PrimaryKeyArn pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayInput
}

func (ReplicaKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*replicaKeyArgs)(nil)).Elem()
}

type ReplicaKeyInput interface {
	pulumi.Input

	ToReplicaKeyOutput() ReplicaKeyOutput
	ToReplicaKeyOutputWithContext(ctx context.Context) ReplicaKeyOutput
}

func (*ReplicaKey) ElementType() reflect.Type {
	return reflect.TypeOf((**ReplicaKey)(nil)).Elem()
}

func (i *ReplicaKey) ToReplicaKeyOutput() ReplicaKeyOutput {
	return i.ToReplicaKeyOutputWithContext(context.Background())
}

func (i *ReplicaKey) ToReplicaKeyOutputWithContext(ctx context.Context) ReplicaKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReplicaKeyOutput)
}

type ReplicaKeyOutput struct{ *pulumi.OutputState }

func (ReplicaKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ReplicaKey)(nil)).Elem()
}

func (o ReplicaKeyOutput) ToReplicaKeyOutput() ReplicaKeyOutput {
	return o
}

func (o ReplicaKeyOutput) ToReplicaKeyOutputWithContext(ctx context.Context) ReplicaKeyOutput {
	return o
}

func (o ReplicaKeyOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
func (o ReplicaKeyOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
func (o ReplicaKeyOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.BoolPtrOutput { return v.Enabled }).(pulumi.BoolPtrOutput)
}

func (o ReplicaKeyOutput) KeyId() pulumi.StringOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.StringOutput { return v.KeyId }).(pulumi.StringOutput)
}

// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::ReplicaKey` for more information about the expected schema for this property.
func (o ReplicaKeyOutput) KeyPolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.AnyOutput { return v.KeyPolicy }).(pulumi.AnyOutput)
}

// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
func (o ReplicaKeyOutput) PendingWindowInDays() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.IntPtrOutput { return v.PendingWindowInDays }).(pulumi.IntPtrOutput)
}

// Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
func (o ReplicaKeyOutput) PrimaryKeyArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ReplicaKey) pulumi.StringOutput { return v.PrimaryKeyArn }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o ReplicaKeyOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *ReplicaKey) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ReplicaKeyInput)(nil)).Elem(), &ReplicaKey{})
	pulumi.RegisterOutputType(ReplicaKeyOutput{})
}
