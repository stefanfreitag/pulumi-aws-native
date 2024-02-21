// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ecr

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::ECR::RegistryPolicy is used to specify permissions for another AWS account and is used when configuring cross-account replication. For more information, see Registry permissions in the Amazon Elastic Container Registry User Guide: https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html
type RegistryPolicy struct {
	pulumi.CustomResourceState

	// The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the Amazon Elastic Container Registry User Guide.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::RegistryPolicy` for more information about the expected schema for this property.
	PolicyText pulumi.AnyOutput    `pulumi:"policyText"`
	RegistryId pulumi.StringOutput `pulumi:"registryId"`
}

// NewRegistryPolicy registers a new resource with the given unique name, arguments, and options.
func NewRegistryPolicy(ctx *pulumi.Context,
	name string, args *RegistryPolicyArgs, opts ...pulumi.ResourceOption) (*RegistryPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PolicyText == nil {
		return nil, errors.New("invalid value for required argument 'PolicyText'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RegistryPolicy
	err := ctx.RegisterResource("aws-native:ecr:RegistryPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegistryPolicy gets an existing RegistryPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegistryPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegistryPolicyState, opts ...pulumi.ResourceOption) (*RegistryPolicy, error) {
	var resource RegistryPolicy
	err := ctx.ReadResource("aws-native:ecr:RegistryPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegistryPolicy resources.
type registryPolicyState struct {
}

type RegistryPolicyState struct {
}

func (RegistryPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*registryPolicyState)(nil)).Elem()
}

type registryPolicyArgs struct {
	// The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the Amazon Elastic Container Registry User Guide.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::RegistryPolicy` for more information about the expected schema for this property.
	PolicyText interface{} `pulumi:"policyText"`
}

// The set of arguments for constructing a RegistryPolicy resource.
type RegistryPolicyArgs struct {
	// The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the Amazon Elastic Container Registry User Guide.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::RegistryPolicy` for more information about the expected schema for this property.
	PolicyText pulumi.Input
}

func (RegistryPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registryPolicyArgs)(nil)).Elem()
}

type RegistryPolicyInput interface {
	pulumi.Input

	ToRegistryPolicyOutput() RegistryPolicyOutput
	ToRegistryPolicyOutputWithContext(ctx context.Context) RegistryPolicyOutput
}

func (*RegistryPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**RegistryPolicy)(nil)).Elem()
}

func (i *RegistryPolicy) ToRegistryPolicyOutput() RegistryPolicyOutput {
	return i.ToRegistryPolicyOutputWithContext(context.Background())
}

func (i *RegistryPolicy) ToRegistryPolicyOutputWithContext(ctx context.Context) RegistryPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegistryPolicyOutput)
}

type RegistryPolicyOutput struct{ *pulumi.OutputState }

func (RegistryPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RegistryPolicy)(nil)).Elem()
}

func (o RegistryPolicyOutput) ToRegistryPolicyOutput() RegistryPolicyOutput {
	return o
}

func (o RegistryPolicyOutput) ToRegistryPolicyOutputWithContext(ctx context.Context) RegistryPolicyOutput {
	return o
}

// The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the Amazon Elastic Container Registry User Guide.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::RegistryPolicy` for more information about the expected schema for this property.
func (o RegistryPolicyOutput) PolicyText() pulumi.AnyOutput {
	return o.ApplyT(func(v *RegistryPolicy) pulumi.AnyOutput { return v.PolicyText }).(pulumi.AnyOutput)
}

func (o RegistryPolicyOutput) RegistryId() pulumi.StringOutput {
	return o.ApplyT(func(v *RegistryPolicy) pulumi.StringOutput { return v.RegistryId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RegistryPolicyInput)(nil)).Elem(), &RegistryPolicy{})
	pulumi.RegisterOutputType(RegistryPolicyOutput{})
}
