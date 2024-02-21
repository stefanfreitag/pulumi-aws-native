// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment
type UserPoolRiskConfigurationAttachment struct {
	pulumi.CustomResourceState

	AccountTakeoverRiskConfiguration        UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypePtrOutput        `pulumi:"accountTakeoverRiskConfiguration"`
	ClientId                                pulumi.StringOutput                                                                     `pulumi:"clientId"`
	CompromisedCredentialsRiskConfiguration UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationTypePtrOutput `pulumi:"compromisedCredentialsRiskConfiguration"`
	RiskExceptionConfiguration              UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationTypePtrOutput              `pulumi:"riskExceptionConfiguration"`
	UserPoolId                              pulumi.StringOutput                                                                     `pulumi:"userPoolId"`
}

// NewUserPoolRiskConfigurationAttachment registers a new resource with the given unique name, arguments, and options.
func NewUserPoolRiskConfigurationAttachment(ctx *pulumi.Context,
	name string, args *UserPoolRiskConfigurationAttachmentArgs, opts ...pulumi.ResourceOption) (*UserPoolRiskConfigurationAttachment, error) {
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
	var resource UserPoolRiskConfigurationAttachment
	err := ctx.RegisterResource("aws-native:cognito:UserPoolRiskConfigurationAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPoolRiskConfigurationAttachment gets an existing UserPoolRiskConfigurationAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolRiskConfigurationAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPoolRiskConfigurationAttachmentState, opts ...pulumi.ResourceOption) (*UserPoolRiskConfigurationAttachment, error) {
	var resource UserPoolRiskConfigurationAttachment
	err := ctx.ReadResource("aws-native:cognito:UserPoolRiskConfigurationAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPoolRiskConfigurationAttachment resources.
type userPoolRiskConfigurationAttachmentState struct {
}

type UserPoolRiskConfigurationAttachmentState struct {
}

func (UserPoolRiskConfigurationAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolRiskConfigurationAttachmentState)(nil)).Elem()
}

type userPoolRiskConfigurationAttachmentArgs struct {
	AccountTakeoverRiskConfiguration        *UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationType        `pulumi:"accountTakeoverRiskConfiguration"`
	ClientId                                string                                                                          `pulumi:"clientId"`
	CompromisedCredentialsRiskConfiguration *UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationType `pulumi:"compromisedCredentialsRiskConfiguration"`
	RiskExceptionConfiguration              *UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationType              `pulumi:"riskExceptionConfiguration"`
	UserPoolId                              string                                                                          `pulumi:"userPoolId"`
}

// The set of arguments for constructing a UserPoolRiskConfigurationAttachment resource.
type UserPoolRiskConfigurationAttachmentArgs struct {
	AccountTakeoverRiskConfiguration        UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypePtrInput
	ClientId                                pulumi.StringInput
	CompromisedCredentialsRiskConfiguration UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationTypePtrInput
	RiskExceptionConfiguration              UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationTypePtrInput
	UserPoolId                              pulumi.StringInput
}

func (UserPoolRiskConfigurationAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolRiskConfigurationAttachmentArgs)(nil)).Elem()
}

type UserPoolRiskConfigurationAttachmentInput interface {
	pulumi.Input

	ToUserPoolRiskConfigurationAttachmentOutput() UserPoolRiskConfigurationAttachmentOutput
	ToUserPoolRiskConfigurationAttachmentOutputWithContext(ctx context.Context) UserPoolRiskConfigurationAttachmentOutput
}

func (*UserPoolRiskConfigurationAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolRiskConfigurationAttachment)(nil)).Elem()
}

func (i *UserPoolRiskConfigurationAttachment) ToUserPoolRiskConfigurationAttachmentOutput() UserPoolRiskConfigurationAttachmentOutput {
	return i.ToUserPoolRiskConfigurationAttachmentOutputWithContext(context.Background())
}

func (i *UserPoolRiskConfigurationAttachment) ToUserPoolRiskConfigurationAttachmentOutputWithContext(ctx context.Context) UserPoolRiskConfigurationAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPoolRiskConfigurationAttachmentOutput)
}

type UserPoolRiskConfigurationAttachmentOutput struct{ *pulumi.OutputState }

func (UserPoolRiskConfigurationAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolRiskConfigurationAttachment)(nil)).Elem()
}

func (o UserPoolRiskConfigurationAttachmentOutput) ToUserPoolRiskConfigurationAttachmentOutput() UserPoolRiskConfigurationAttachmentOutput {
	return o
}

func (o UserPoolRiskConfigurationAttachmentOutput) ToUserPoolRiskConfigurationAttachmentOutputWithContext(ctx context.Context) UserPoolRiskConfigurationAttachmentOutput {
	return o
}

func (o UserPoolRiskConfigurationAttachmentOutput) AccountTakeoverRiskConfiguration() UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypePtrOutput {
	return o.ApplyT(func(v *UserPoolRiskConfigurationAttachment) UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypePtrOutput {
		return v.AccountTakeoverRiskConfiguration
	}).(UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypePtrOutput)
}

func (o UserPoolRiskConfigurationAttachmentOutput) ClientId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolRiskConfigurationAttachment) pulumi.StringOutput { return v.ClientId }).(pulumi.StringOutput)
}

func (o UserPoolRiskConfigurationAttachmentOutput) CompromisedCredentialsRiskConfiguration() UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationTypePtrOutput {
	return o.ApplyT(func(v *UserPoolRiskConfigurationAttachment) UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationTypePtrOutput {
		return v.CompromisedCredentialsRiskConfiguration
	}).(UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationTypePtrOutput)
}

func (o UserPoolRiskConfigurationAttachmentOutput) RiskExceptionConfiguration() UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationTypePtrOutput {
	return o.ApplyT(func(v *UserPoolRiskConfigurationAttachment) UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationTypePtrOutput {
		return v.RiskExceptionConfiguration
	}).(UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationTypePtrOutput)
}

func (o UserPoolRiskConfigurationAttachmentOutput) UserPoolId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolRiskConfigurationAttachment) pulumi.StringOutput { return v.UserPoolId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserPoolRiskConfigurationAttachmentInput)(nil)).Elem(), &UserPoolRiskConfigurationAttachment{})
	pulumi.RegisterOutputType(UserPoolRiskConfigurationAttachmentOutput{})
}
