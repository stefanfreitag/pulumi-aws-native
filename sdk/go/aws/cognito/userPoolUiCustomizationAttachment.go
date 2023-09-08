// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment
//
// Deprecated: UserPoolUiCustomizationAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserPoolUiCustomizationAttachment struct {
	pulumi.CustomResourceState

	ClientId   pulumi.StringOutput    `pulumi:"clientId"`
	Css        pulumi.StringPtrOutput `pulumi:"css"`
	UserPoolId pulumi.StringOutput    `pulumi:"userPoolId"`
}

// NewUserPoolUiCustomizationAttachment registers a new resource with the given unique name, arguments, and options.
func NewUserPoolUiCustomizationAttachment(ctx *pulumi.Context,
	name string, args *UserPoolUiCustomizationAttachmentArgs, opts ...pulumi.ResourceOption) (*UserPoolUiCustomizationAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClientId == nil {
		return nil, errors.New("invalid value for required argument 'ClientId'")
	}
	if args.UserPoolId == nil {
		return nil, errors.New("invalid value for required argument 'UserPoolId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"clientId",
		"userPoolId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserPoolUiCustomizationAttachment
	err := ctx.RegisterResource("aws-native:cognito:UserPoolUiCustomizationAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPoolUiCustomizationAttachment gets an existing UserPoolUiCustomizationAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolUiCustomizationAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPoolUiCustomizationAttachmentState, opts ...pulumi.ResourceOption) (*UserPoolUiCustomizationAttachment, error) {
	var resource UserPoolUiCustomizationAttachment
	err := ctx.ReadResource("aws-native:cognito:UserPoolUiCustomizationAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPoolUiCustomizationAttachment resources.
type userPoolUiCustomizationAttachmentState struct {
}

type UserPoolUiCustomizationAttachmentState struct {
}

func (UserPoolUiCustomizationAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolUiCustomizationAttachmentState)(nil)).Elem()
}

type userPoolUiCustomizationAttachmentArgs struct {
	ClientId   string  `pulumi:"clientId"`
	Css        *string `pulumi:"css"`
	UserPoolId string  `pulumi:"userPoolId"`
}

// The set of arguments for constructing a UserPoolUiCustomizationAttachment resource.
type UserPoolUiCustomizationAttachmentArgs struct {
	ClientId   pulumi.StringInput
	Css        pulumi.StringPtrInput
	UserPoolId pulumi.StringInput
}

func (UserPoolUiCustomizationAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolUiCustomizationAttachmentArgs)(nil)).Elem()
}

type UserPoolUiCustomizationAttachmentInput interface {
	pulumi.Input

	ToUserPoolUiCustomizationAttachmentOutput() UserPoolUiCustomizationAttachmentOutput
	ToUserPoolUiCustomizationAttachmentOutputWithContext(ctx context.Context) UserPoolUiCustomizationAttachmentOutput
}

func (*UserPoolUiCustomizationAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolUiCustomizationAttachment)(nil)).Elem()
}

func (i *UserPoolUiCustomizationAttachment) ToUserPoolUiCustomizationAttachmentOutput() UserPoolUiCustomizationAttachmentOutput {
	return i.ToUserPoolUiCustomizationAttachmentOutputWithContext(context.Background())
}

func (i *UserPoolUiCustomizationAttachment) ToUserPoolUiCustomizationAttachmentOutputWithContext(ctx context.Context) UserPoolUiCustomizationAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPoolUiCustomizationAttachmentOutput)
}

func (i *UserPoolUiCustomizationAttachment) ToOutput(ctx context.Context) pulumix.Output[*UserPoolUiCustomizationAttachment] {
	return pulumix.Output[*UserPoolUiCustomizationAttachment]{
		OutputState: i.ToUserPoolUiCustomizationAttachmentOutputWithContext(ctx).OutputState,
	}
}

type UserPoolUiCustomizationAttachmentOutput struct{ *pulumi.OutputState }

func (UserPoolUiCustomizationAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolUiCustomizationAttachment)(nil)).Elem()
}

func (o UserPoolUiCustomizationAttachmentOutput) ToUserPoolUiCustomizationAttachmentOutput() UserPoolUiCustomizationAttachmentOutput {
	return o
}

func (o UserPoolUiCustomizationAttachmentOutput) ToUserPoolUiCustomizationAttachmentOutputWithContext(ctx context.Context) UserPoolUiCustomizationAttachmentOutput {
	return o
}

func (o UserPoolUiCustomizationAttachmentOutput) ToOutput(ctx context.Context) pulumix.Output[*UserPoolUiCustomizationAttachment] {
	return pulumix.Output[*UserPoolUiCustomizationAttachment]{
		OutputState: o.OutputState,
	}
}

func (o UserPoolUiCustomizationAttachmentOutput) ClientId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolUiCustomizationAttachment) pulumi.StringOutput { return v.ClientId }).(pulumi.StringOutput)
}

func (o UserPoolUiCustomizationAttachmentOutput) Css() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *UserPoolUiCustomizationAttachment) pulumi.StringPtrOutput { return v.Css }).(pulumi.StringPtrOutput)
}

func (o UserPoolUiCustomizationAttachmentOutput) UserPoolId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolUiCustomizationAttachment) pulumi.StringOutput { return v.UserPoolId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserPoolUiCustomizationAttachmentInput)(nil)).Elem(), &UserPoolUiCustomizationAttachment{})
	pulumi.RegisterOutputType(UserPoolUiCustomizationAttachmentOutput{})
}
