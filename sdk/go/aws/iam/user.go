// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::IAM::User
type User struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A list of group names to which you want to add the user.
	Groups pulumi.StringArrayOutput `pulumi:"groups"`
	// Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.
	LoginProfile UserLoginProfilePtrOutput `pulumi:"loginProfile"`
	// A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.
	ManagedPolicyArns pulumi.StringArrayOutput `pulumi:"managedPolicyArns"`
	// The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide. The ARN of the policy used to set the permissions boundary for the user.
	Path pulumi.StringPtrOutput `pulumi:"path"`
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary pulumi.StringPtrOutput `pulumi:"permissionsBoundary"`
	// Adds or updates an inline policy document that is embedded in the specified IAM role.
	Policies UserPolicyTypeArrayOutput `pulumi:"policies"`
	// A list of tags that are associated with the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide.
	Tags UserTagArrayOutput `pulumi:"tags"`
	// The friendly name identifying the user.
	UserName pulumi.StringPtrOutput `pulumi:"userName"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		args = &UserArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"userName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource User
	err := ctx.RegisterResource("aws-native:iam:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("aws-native:iam:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
}

type UserState struct {
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// A list of group names to which you want to add the user.
	Groups []string `pulumi:"groups"`
	// Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.
	LoginProfile *UserLoginProfile `pulumi:"loginProfile"`
	// A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.
	ManagedPolicyArns []string `pulumi:"managedPolicyArns"`
	// The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide. The ARN of the policy used to set the permissions boundary for the user.
	Path *string `pulumi:"path"`
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary *string `pulumi:"permissionsBoundary"`
	// Adds or updates an inline policy document that is embedded in the specified IAM role.
	Policies []UserPolicyType `pulumi:"policies"`
	// A list of tags that are associated with the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide.
	Tags []UserTag `pulumi:"tags"`
	// The friendly name identifying the user.
	UserName *string `pulumi:"userName"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// A list of group names to which you want to add the user.
	Groups pulumi.StringArrayInput
	// Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.
	LoginProfile UserLoginProfilePtrInput
	// A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.
	ManagedPolicyArns pulumi.StringArrayInput
	// The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide. The ARN of the policy used to set the permissions boundary for the user.
	Path pulumi.StringPtrInput
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary pulumi.StringPtrInput
	// Adds or updates an inline policy document that is embedded in the specified IAM role.
	Policies UserPolicyTypeArrayInput
	// A list of tags that are associated with the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide.
	Tags UserTagArrayInput
	// The friendly name identifying the user.
	UserName pulumi.StringPtrInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}

type UserInput interface {
	pulumi.Input

	ToUserOutput() UserOutput
	ToUserOutputWithContext(ctx context.Context) UserOutput
}

func (*User) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (i *User) ToUserOutput() UserOutput {
	return i.ToUserOutputWithContext(context.Background())
}

func (i *User) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserOutput)
}

func (i *User) ToOutput(ctx context.Context) pulumix.Output[*User] {
	return pulumix.Output[*User]{
		OutputState: i.ToUserOutputWithContext(ctx).OutputState,
	}
}

type UserOutput struct{ *pulumi.OutputState }

func (UserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (o UserOutput) ToUserOutput() UserOutput {
	return o
}

func (o UserOutput) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return o
}

func (o UserOutput) ToOutput(ctx context.Context) pulumix.Output[*User] {
	return pulumix.Output[*User]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide.
func (o UserOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A list of group names to which you want to add the user.
func (o UserOutput) Groups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *User) pulumi.StringArrayOutput { return v.Groups }).(pulumi.StringArrayOutput)
}

// Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.
func (o UserOutput) LoginProfile() UserLoginProfilePtrOutput {
	return o.ApplyT(func(v *User) UserLoginProfilePtrOutput { return v.LoginProfile }).(UserLoginProfilePtrOutput)
}

// A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.
func (o UserOutput) ManagedPolicyArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *User) pulumi.StringArrayOutput { return v.ManagedPolicyArns }).(pulumi.StringArrayOutput)
}

// The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide. The ARN of the policy used to set the permissions boundary for the user.
func (o UserOutput) Path() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.Path }).(pulumi.StringPtrOutput)
}

// The ARN of the policy that is used to set the permissions boundary for the user.
func (o UserOutput) PermissionsBoundary() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.PermissionsBoundary }).(pulumi.StringPtrOutput)
}

// Adds or updates an inline policy document that is embedded in the specified IAM role.
func (o UserOutput) Policies() UserPolicyTypeArrayOutput {
	return o.ApplyT(func(v *User) UserPolicyTypeArrayOutput { return v.Policies }).(UserPolicyTypeArrayOutput)
}

// A list of tags that are associated with the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide.
func (o UserOutput) Tags() UserTagArrayOutput {
	return o.ApplyT(func(v *User) UserTagArrayOutput { return v.Tags }).(UserTagArrayOutput)
}

// The friendly name identifying the user.
func (o UserOutput) UserName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *User) pulumi.StringPtrOutput { return v.UserName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserInput)(nil)).Elem(), &User{})
	pulumi.RegisterOutputType(UserOutput{})
}
