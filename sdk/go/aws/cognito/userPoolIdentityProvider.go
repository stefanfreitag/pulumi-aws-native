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

// Resource Type definition for AWS::Cognito::UserPoolIdentityProvider
//
// Deprecated: UserPoolIdentityProvider is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserPoolIdentityProvider struct {
	pulumi.CustomResourceState

	AttributeMapping pulumi.AnyOutput         `pulumi:"attributeMapping"`
	IdpIdentifiers   pulumi.StringArrayOutput `pulumi:"idpIdentifiers"`
	ProviderDetails  pulumi.AnyOutput         `pulumi:"providerDetails"`
	ProviderName     pulumi.StringOutput      `pulumi:"providerName"`
	ProviderType     pulumi.StringOutput      `pulumi:"providerType"`
	UserPoolId       pulumi.StringOutput      `pulumi:"userPoolId"`
}

// NewUserPoolIdentityProvider registers a new resource with the given unique name, arguments, and options.
func NewUserPoolIdentityProvider(ctx *pulumi.Context,
	name string, args *UserPoolIdentityProviderArgs, opts ...pulumi.ResourceOption) (*UserPoolIdentityProvider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProviderName == nil {
		return nil, errors.New("invalid value for required argument 'ProviderName'")
	}
	if args.ProviderType == nil {
		return nil, errors.New("invalid value for required argument 'ProviderType'")
	}
	if args.UserPoolId == nil {
		return nil, errors.New("invalid value for required argument 'UserPoolId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"providerName",
		"providerType",
		"userPoolId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserPoolIdentityProvider
	err := ctx.RegisterResource("aws-native:cognito:UserPoolIdentityProvider", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPoolIdentityProvider gets an existing UserPoolIdentityProvider resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolIdentityProvider(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPoolIdentityProviderState, opts ...pulumi.ResourceOption) (*UserPoolIdentityProvider, error) {
	var resource UserPoolIdentityProvider
	err := ctx.ReadResource("aws-native:cognito:UserPoolIdentityProvider", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPoolIdentityProvider resources.
type userPoolIdentityProviderState struct {
}

type UserPoolIdentityProviderState struct {
}

func (UserPoolIdentityProviderState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolIdentityProviderState)(nil)).Elem()
}

type userPoolIdentityProviderArgs struct {
	AttributeMapping interface{} `pulumi:"attributeMapping"`
	IdpIdentifiers   []string    `pulumi:"idpIdentifiers"`
	ProviderDetails  interface{} `pulumi:"providerDetails"`
	ProviderName     string      `pulumi:"providerName"`
	ProviderType     string      `pulumi:"providerType"`
	UserPoolId       string      `pulumi:"userPoolId"`
}

// The set of arguments for constructing a UserPoolIdentityProvider resource.
type UserPoolIdentityProviderArgs struct {
	AttributeMapping pulumi.Input
	IdpIdentifiers   pulumi.StringArrayInput
	ProviderDetails  pulumi.Input
	ProviderName     pulumi.StringInput
	ProviderType     pulumi.StringInput
	UserPoolId       pulumi.StringInput
}

func (UserPoolIdentityProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolIdentityProviderArgs)(nil)).Elem()
}

type UserPoolIdentityProviderInput interface {
	pulumi.Input

	ToUserPoolIdentityProviderOutput() UserPoolIdentityProviderOutput
	ToUserPoolIdentityProviderOutputWithContext(ctx context.Context) UserPoolIdentityProviderOutput
}

func (*UserPoolIdentityProvider) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolIdentityProvider)(nil)).Elem()
}

func (i *UserPoolIdentityProvider) ToUserPoolIdentityProviderOutput() UserPoolIdentityProviderOutput {
	return i.ToUserPoolIdentityProviderOutputWithContext(context.Background())
}

func (i *UserPoolIdentityProvider) ToUserPoolIdentityProviderOutputWithContext(ctx context.Context) UserPoolIdentityProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPoolIdentityProviderOutput)
}

func (i *UserPoolIdentityProvider) ToOutput(ctx context.Context) pulumix.Output[*UserPoolIdentityProvider] {
	return pulumix.Output[*UserPoolIdentityProvider]{
		OutputState: i.ToUserPoolIdentityProviderOutputWithContext(ctx).OutputState,
	}
}

type UserPoolIdentityProviderOutput struct{ *pulumi.OutputState }

func (UserPoolIdentityProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolIdentityProvider)(nil)).Elem()
}

func (o UserPoolIdentityProviderOutput) ToUserPoolIdentityProviderOutput() UserPoolIdentityProviderOutput {
	return o
}

func (o UserPoolIdentityProviderOutput) ToUserPoolIdentityProviderOutputWithContext(ctx context.Context) UserPoolIdentityProviderOutput {
	return o
}

func (o UserPoolIdentityProviderOutput) ToOutput(ctx context.Context) pulumix.Output[*UserPoolIdentityProvider] {
	return pulumix.Output[*UserPoolIdentityProvider]{
		OutputState: o.OutputState,
	}
}

func (o UserPoolIdentityProviderOutput) AttributeMapping() pulumi.AnyOutput {
	return o.ApplyT(func(v *UserPoolIdentityProvider) pulumi.AnyOutput { return v.AttributeMapping }).(pulumi.AnyOutput)
}

func (o UserPoolIdentityProviderOutput) IdpIdentifiers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *UserPoolIdentityProvider) pulumi.StringArrayOutput { return v.IdpIdentifiers }).(pulumi.StringArrayOutput)
}

func (o UserPoolIdentityProviderOutput) ProviderDetails() pulumi.AnyOutput {
	return o.ApplyT(func(v *UserPoolIdentityProvider) pulumi.AnyOutput { return v.ProviderDetails }).(pulumi.AnyOutput)
}

func (o UserPoolIdentityProviderOutput) ProviderName() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolIdentityProvider) pulumi.StringOutput { return v.ProviderName }).(pulumi.StringOutput)
}

func (o UserPoolIdentityProviderOutput) ProviderType() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolIdentityProvider) pulumi.StringOutput { return v.ProviderType }).(pulumi.StringOutput)
}

func (o UserPoolIdentityProviderOutput) UserPoolId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolIdentityProvider) pulumi.StringOutput { return v.UserPoolId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserPoolIdentityProviderInput)(nil)).Elem(), &UserPoolIdentityProvider{})
	pulumi.RegisterOutputType(UserPoolIdentityProviderOutput{})
}
