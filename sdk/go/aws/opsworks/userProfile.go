// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package opsworks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::OpsWorks::UserProfile
//
// Deprecated: UserProfile is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserProfile struct {
	pulumi.CustomResourceState

	AllowSelfManagement pulumi.BoolPtrOutput   `pulumi:"allowSelfManagement"`
	IamUserArn          pulumi.StringOutput    `pulumi:"iamUserArn"`
	SshPublicKey        pulumi.StringPtrOutput `pulumi:"sshPublicKey"`
	SshUsername         pulumi.StringPtrOutput `pulumi:"sshUsername"`
}

// NewUserProfile registers a new resource with the given unique name, arguments, and options.
func NewUserProfile(ctx *pulumi.Context,
	name string, args *UserProfileArgs, opts ...pulumi.ResourceOption) (*UserProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IamUserArn == nil {
		return nil, errors.New("invalid value for required argument 'IamUserArn'")
	}
	var resource UserProfile
	err := ctx.RegisterResource("aws-native:opsworks:UserProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserProfile gets an existing UserProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserProfileState, opts ...pulumi.ResourceOption) (*UserProfile, error) {
	var resource UserProfile
	err := ctx.ReadResource("aws-native:opsworks:UserProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserProfile resources.
type userProfileState struct {
}

type UserProfileState struct {
}

func (UserProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*userProfileState)(nil)).Elem()
}

type userProfileArgs struct {
	AllowSelfManagement *bool   `pulumi:"allowSelfManagement"`
	IamUserArn          string  `pulumi:"iamUserArn"`
	SshPublicKey        *string `pulumi:"sshPublicKey"`
	SshUsername         *string `pulumi:"sshUsername"`
}

// The set of arguments for constructing a UserProfile resource.
type UserProfileArgs struct {
	AllowSelfManagement pulumi.BoolPtrInput
	IamUserArn          pulumi.StringInput
	SshPublicKey        pulumi.StringPtrInput
	SshUsername         pulumi.StringPtrInput
}

func (UserProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userProfileArgs)(nil)).Elem()
}

type UserProfileInput interface {
	pulumi.Input

	ToUserProfileOutput() UserProfileOutput
	ToUserProfileOutputWithContext(ctx context.Context) UserProfileOutput
}

func (*UserProfile) ElementType() reflect.Type {
	return reflect.TypeOf((*UserProfile)(nil))
}

func (i *UserProfile) ToUserProfileOutput() UserProfileOutput {
	return i.ToUserProfileOutputWithContext(context.Background())
}

func (i *UserProfile) ToUserProfileOutputWithContext(ctx context.Context) UserProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserProfileOutput)
}

type UserProfileOutput struct{ *pulumi.OutputState }

func (UserProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserProfile)(nil))
}

func (o UserProfileOutput) ToUserProfileOutput() UserProfileOutput {
	return o
}

func (o UserProfileOutput) ToUserProfileOutputWithContext(ctx context.Context) UserProfileOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UserProfileOutput{})
}
