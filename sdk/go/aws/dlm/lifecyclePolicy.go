// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dlm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::DLM::LifecyclePolicy
//
// Deprecated: LifecyclePolicy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type LifecyclePolicy struct {
	pulumi.CustomResourceState

	Arn              pulumi.StringOutput                   `pulumi:"arn"`
	Description      pulumi.StringPtrOutput                `pulumi:"description"`
	ExecutionRoleArn pulumi.StringPtrOutput                `pulumi:"executionRoleArn"`
	PolicyDetails    LifecyclePolicyPolicyDetailsPtrOutput `pulumi:"policyDetails"`
	State            pulumi.StringPtrOutput                `pulumi:"state"`
	Tags             LifecyclePolicyTagArrayOutput         `pulumi:"tags"`
}

// NewLifecyclePolicy registers a new resource with the given unique name, arguments, and options.
func NewLifecyclePolicy(ctx *pulumi.Context,
	name string, args *LifecyclePolicyArgs, opts ...pulumi.ResourceOption) (*LifecyclePolicy, error) {
	if args == nil {
		args = &LifecyclePolicyArgs{}
	}

	var resource LifecyclePolicy
	err := ctx.RegisterResource("aws-native:dlm:LifecyclePolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLifecyclePolicy gets an existing LifecyclePolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLifecyclePolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LifecyclePolicyState, opts ...pulumi.ResourceOption) (*LifecyclePolicy, error) {
	var resource LifecyclePolicy
	err := ctx.ReadResource("aws-native:dlm:LifecyclePolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LifecyclePolicy resources.
type lifecyclePolicyState struct {
}

type LifecyclePolicyState struct {
}

func (LifecyclePolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*lifecyclePolicyState)(nil)).Elem()
}

type lifecyclePolicyArgs struct {
	Description      *string                       `pulumi:"description"`
	ExecutionRoleArn *string                       `pulumi:"executionRoleArn"`
	PolicyDetails    *LifecyclePolicyPolicyDetails `pulumi:"policyDetails"`
	State            *string                       `pulumi:"state"`
	Tags             []LifecyclePolicyTag          `pulumi:"tags"`
}

// The set of arguments for constructing a LifecyclePolicy resource.
type LifecyclePolicyArgs struct {
	Description      pulumi.StringPtrInput
	ExecutionRoleArn pulumi.StringPtrInput
	PolicyDetails    LifecyclePolicyPolicyDetailsPtrInput
	State            pulumi.StringPtrInput
	Tags             LifecyclePolicyTagArrayInput
}

func (LifecyclePolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*lifecyclePolicyArgs)(nil)).Elem()
}

type LifecyclePolicyInput interface {
	pulumi.Input

	ToLifecyclePolicyOutput() LifecyclePolicyOutput
	ToLifecyclePolicyOutputWithContext(ctx context.Context) LifecyclePolicyOutput
}

func (*LifecyclePolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*LifecyclePolicy)(nil))
}

func (i *LifecyclePolicy) ToLifecyclePolicyOutput() LifecyclePolicyOutput {
	return i.ToLifecyclePolicyOutputWithContext(context.Background())
}

func (i *LifecyclePolicy) ToLifecyclePolicyOutputWithContext(ctx context.Context) LifecyclePolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LifecyclePolicyOutput)
}

type LifecyclePolicyOutput struct{ *pulumi.OutputState }

func (LifecyclePolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LifecyclePolicy)(nil))
}

func (o LifecyclePolicyOutput) ToLifecyclePolicyOutput() LifecyclePolicyOutput {
	return o
}

func (o LifecyclePolicyOutput) ToLifecyclePolicyOutputWithContext(ctx context.Context) LifecyclePolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LifecyclePolicyOutput{})
}
