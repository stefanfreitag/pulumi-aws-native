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

// Resource Type definition for AWS::IAM::UserToGroupAddition
//
// Deprecated: UserToGroupAddition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserToGroupAddition struct {
	pulumi.CustomResourceState

	GroupName pulumi.StringOutput      `pulumi:"groupName"`
	Users     pulumi.StringArrayOutput `pulumi:"users"`
}

// NewUserToGroupAddition registers a new resource with the given unique name, arguments, and options.
func NewUserToGroupAddition(ctx *pulumi.Context,
	name string, args *UserToGroupAdditionArgs, opts ...pulumi.ResourceOption) (*UserToGroupAddition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupName == nil {
		return nil, errors.New("invalid value for required argument 'GroupName'")
	}
	if args.Users == nil {
		return nil, errors.New("invalid value for required argument 'Users'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserToGroupAddition
	err := ctx.RegisterResource("aws-native:iam:UserToGroupAddition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserToGroupAddition gets an existing UserToGroupAddition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserToGroupAddition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserToGroupAdditionState, opts ...pulumi.ResourceOption) (*UserToGroupAddition, error) {
	var resource UserToGroupAddition
	err := ctx.ReadResource("aws-native:iam:UserToGroupAddition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserToGroupAddition resources.
type userToGroupAdditionState struct {
}

type UserToGroupAdditionState struct {
}

func (UserToGroupAdditionState) ElementType() reflect.Type {
	return reflect.TypeOf((*userToGroupAdditionState)(nil)).Elem()
}

type userToGroupAdditionArgs struct {
	GroupName string   `pulumi:"groupName"`
	Users     []string `pulumi:"users"`
}

// The set of arguments for constructing a UserToGroupAddition resource.
type UserToGroupAdditionArgs struct {
	GroupName pulumi.StringInput
	Users     pulumi.StringArrayInput
}

func (UserToGroupAdditionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userToGroupAdditionArgs)(nil)).Elem()
}

type UserToGroupAdditionInput interface {
	pulumi.Input

	ToUserToGroupAdditionOutput() UserToGroupAdditionOutput
	ToUserToGroupAdditionOutputWithContext(ctx context.Context) UserToGroupAdditionOutput
}

func (*UserToGroupAddition) ElementType() reflect.Type {
	return reflect.TypeOf((**UserToGroupAddition)(nil)).Elem()
}

func (i *UserToGroupAddition) ToUserToGroupAdditionOutput() UserToGroupAdditionOutput {
	return i.ToUserToGroupAdditionOutputWithContext(context.Background())
}

func (i *UserToGroupAddition) ToUserToGroupAdditionOutputWithContext(ctx context.Context) UserToGroupAdditionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserToGroupAdditionOutput)
}

func (i *UserToGroupAddition) ToOutput(ctx context.Context) pulumix.Output[*UserToGroupAddition] {
	return pulumix.Output[*UserToGroupAddition]{
		OutputState: i.ToUserToGroupAdditionOutputWithContext(ctx).OutputState,
	}
}

type UserToGroupAdditionOutput struct{ *pulumi.OutputState }

func (UserToGroupAdditionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserToGroupAddition)(nil)).Elem()
}

func (o UserToGroupAdditionOutput) ToUserToGroupAdditionOutput() UserToGroupAdditionOutput {
	return o
}

func (o UserToGroupAdditionOutput) ToUserToGroupAdditionOutputWithContext(ctx context.Context) UserToGroupAdditionOutput {
	return o
}

func (o UserToGroupAdditionOutput) ToOutput(ctx context.Context) pulumix.Output[*UserToGroupAddition] {
	return pulumix.Output[*UserToGroupAddition]{
		OutputState: o.OutputState,
	}
}

func (o UserToGroupAdditionOutput) GroupName() pulumi.StringOutput {
	return o.ApplyT(func(v *UserToGroupAddition) pulumi.StringOutput { return v.GroupName }).(pulumi.StringOutput)
}

func (o UserToGroupAdditionOutput) Users() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *UserToGroupAddition) pulumi.StringArrayOutput { return v.Users }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserToGroupAdditionInput)(nil)).Elem(), &UserToGroupAddition{})
	pulumi.RegisterOutputType(UserToGroupAdditionOutput{})
}
