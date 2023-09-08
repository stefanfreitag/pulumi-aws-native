// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Schema for IAM User Policy
type UserPolicy struct {
	pulumi.CustomResourceState

	// The policy document.
	PolicyDocument pulumi.AnyOutput `pulumi:"policyDocument"`
	// The name of the policy document.
	PolicyName pulumi.StringOutput `pulumi:"policyName"`
	// The name of the user to associate the policy with.
	UserName pulumi.StringOutput `pulumi:"userName"`
}

// NewUserPolicy registers a new resource with the given unique name, arguments, and options.
func NewUserPolicy(ctx *pulumi.Context,
	name string, args *UserPolicyArgs, opts ...pulumi.ResourceOption) (*UserPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PolicyName == nil {
		return nil, errors.New("invalid value for required argument 'PolicyName'")
	}
	if args.UserName == nil {
		return nil, errors.New("invalid value for required argument 'UserName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"policyName",
		"userName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserPolicy
	err := ctx.RegisterResource("aws-native:iam:UserPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPolicy gets an existing UserPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPolicyState, opts ...pulumi.ResourceOption) (*UserPolicy, error) {
	var resource UserPolicy
	err := ctx.ReadResource("aws-native:iam:UserPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPolicy resources.
type userPolicyState struct {
}

type UserPolicyState struct {
}

func (UserPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPolicyState)(nil)).Elem()
}

type userPolicyArgs struct {
	// The policy document.
	PolicyDocument interface{} `pulumi:"policyDocument"`
	// The name of the policy document.
	PolicyName string `pulumi:"policyName"`
	// The name of the user to associate the policy with.
	UserName string `pulumi:"userName"`
}

// The set of arguments for constructing a UserPolicy resource.
type UserPolicyArgs struct {
	// The policy document.
	PolicyDocument pulumi.Input
	// The name of the policy document.
	PolicyName pulumi.StringInput
	// The name of the user to associate the policy with.
	UserName pulumi.StringInput
}

func (UserPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPolicyArgs)(nil)).Elem()
}

type UserPolicyInput interface {
	pulumi.Input

	ToUserPolicyOutput() UserPolicyOutput
	ToUserPolicyOutputWithContext(ctx context.Context) UserPolicyOutput
}

func (*UserPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPolicy)(nil)).Elem()
}

func (i *UserPolicy) ToUserPolicyOutput() UserPolicyOutput {
	return i.ToUserPolicyOutputWithContext(context.Background())
}

func (i *UserPolicy) ToUserPolicyOutputWithContext(ctx context.Context) UserPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPolicyOutput)
}

func (i *UserPolicy) ToOutput(ctx context.Context) pulumix.Output[*UserPolicy] {
	return pulumix.Output[*UserPolicy]{
		OutputState: i.ToUserPolicyOutputWithContext(ctx).OutputState,
	}
}

type UserPolicyOutput struct{ *pulumi.OutputState }

func (UserPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPolicy)(nil)).Elem()
}

func (o UserPolicyOutput) ToUserPolicyOutput() UserPolicyOutput {
	return o
}

func (o UserPolicyOutput) ToUserPolicyOutputWithContext(ctx context.Context) UserPolicyOutput {
	return o
}

func (o UserPolicyOutput) ToOutput(ctx context.Context) pulumix.Output[*UserPolicy] {
	return pulumix.Output[*UserPolicy]{
		OutputState: o.OutputState,
	}
}

// The policy document.
func (o UserPolicyOutput) PolicyDocument() pulumi.AnyOutput {
	return o.ApplyT(func(v *UserPolicy) pulumi.AnyOutput { return v.PolicyDocument }).(pulumi.AnyOutput)
}

// The name of the policy document.
func (o UserPolicyOutput) PolicyName() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPolicy) pulumi.StringOutput { return v.PolicyName }).(pulumi.StringOutput)
}

// The name of the user to associate the policy with.
func (o UserPolicyOutput) UserName() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPolicy) pulumi.StringOutput { return v.UserName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserPolicyInput)(nil)).Elem(), &UserPolicy{})
	pulumi.RegisterOutputType(UserPolicyOutput{})
}
