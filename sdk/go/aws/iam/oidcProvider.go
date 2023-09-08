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

// Resource Type definition for AWS::IAM::OIDCProvider
type OidcProvider struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the OIDC provider
	Arn            pulumi.StringOutput        `pulumi:"arn"`
	ClientIdList   pulumi.StringArrayOutput   `pulumi:"clientIdList"`
	Tags           OidcProviderTagArrayOutput `pulumi:"tags"`
	ThumbprintList pulumi.StringArrayOutput   `pulumi:"thumbprintList"`
	Url            pulumi.StringPtrOutput     `pulumi:"url"`
}

// NewOidcProvider registers a new resource with the given unique name, arguments, and options.
func NewOidcProvider(ctx *pulumi.Context,
	name string, args *OidcProviderArgs, opts ...pulumi.ResourceOption) (*OidcProvider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ThumbprintList == nil {
		return nil, errors.New("invalid value for required argument 'ThumbprintList'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"url",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OidcProvider
	err := ctx.RegisterResource("aws-native:iam:OidcProvider", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOidcProvider gets an existing OidcProvider resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOidcProvider(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OidcProviderState, opts ...pulumi.ResourceOption) (*OidcProvider, error) {
	var resource OidcProvider
	err := ctx.ReadResource("aws-native:iam:OidcProvider", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OidcProvider resources.
type oidcProviderState struct {
}

type OidcProviderState struct {
}

func (OidcProviderState) ElementType() reflect.Type {
	return reflect.TypeOf((*oidcProviderState)(nil)).Elem()
}

type oidcProviderArgs struct {
	ClientIdList   []string          `pulumi:"clientIdList"`
	Tags           []OidcProviderTag `pulumi:"tags"`
	ThumbprintList []string          `pulumi:"thumbprintList"`
	Url            *string           `pulumi:"url"`
}

// The set of arguments for constructing a OidcProvider resource.
type OidcProviderArgs struct {
	ClientIdList   pulumi.StringArrayInput
	Tags           OidcProviderTagArrayInput
	ThumbprintList pulumi.StringArrayInput
	Url            pulumi.StringPtrInput
}

func (OidcProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*oidcProviderArgs)(nil)).Elem()
}

type OidcProviderInput interface {
	pulumi.Input

	ToOidcProviderOutput() OidcProviderOutput
	ToOidcProviderOutputWithContext(ctx context.Context) OidcProviderOutput
}

func (*OidcProvider) ElementType() reflect.Type {
	return reflect.TypeOf((**OidcProvider)(nil)).Elem()
}

func (i *OidcProvider) ToOidcProviderOutput() OidcProviderOutput {
	return i.ToOidcProviderOutputWithContext(context.Background())
}

func (i *OidcProvider) ToOidcProviderOutputWithContext(ctx context.Context) OidcProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OidcProviderOutput)
}

func (i *OidcProvider) ToOutput(ctx context.Context) pulumix.Output[*OidcProvider] {
	return pulumix.Output[*OidcProvider]{
		OutputState: i.ToOidcProviderOutputWithContext(ctx).OutputState,
	}
}

type OidcProviderOutput struct{ *pulumi.OutputState }

func (OidcProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OidcProvider)(nil)).Elem()
}

func (o OidcProviderOutput) ToOidcProviderOutput() OidcProviderOutput {
	return o
}

func (o OidcProviderOutput) ToOidcProviderOutputWithContext(ctx context.Context) OidcProviderOutput {
	return o
}

func (o OidcProviderOutput) ToOutput(ctx context.Context) pulumix.Output[*OidcProvider] {
	return pulumix.Output[*OidcProvider]{
		OutputState: o.OutputState,
	}
}

// Amazon Resource Name (ARN) of the OIDC provider
func (o OidcProviderOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *OidcProvider) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o OidcProviderOutput) ClientIdList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *OidcProvider) pulumi.StringArrayOutput { return v.ClientIdList }).(pulumi.StringArrayOutput)
}

func (o OidcProviderOutput) Tags() OidcProviderTagArrayOutput {
	return o.ApplyT(func(v *OidcProvider) OidcProviderTagArrayOutput { return v.Tags }).(OidcProviderTagArrayOutput)
}

func (o OidcProviderOutput) ThumbprintList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *OidcProvider) pulumi.StringArrayOutput { return v.ThumbprintList }).(pulumi.StringArrayOutput)
}

func (o OidcProviderOutput) Url() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OidcProvider) pulumi.StringPtrOutput { return v.Url }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OidcProviderInput)(nil)).Elem(), &OidcProvider{})
	pulumi.RegisterOutputType(OidcProviderOutput{})
}
