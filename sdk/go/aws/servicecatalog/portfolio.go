// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ServiceCatalog::Portfolio
//
// Deprecated: Portfolio is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Portfolio struct {
	pulumi.CustomResourceState

	AcceptLanguage pulumi.StringPtrOutput  `pulumi:"acceptLanguage"`
	Description    pulumi.StringPtrOutput  `pulumi:"description"`
	DisplayName    pulumi.StringOutput     `pulumi:"displayName"`
	PortfolioName  pulumi.StringOutput     `pulumi:"portfolioName"`
	ProviderName   pulumi.StringOutput     `pulumi:"providerName"`
	Tags           PortfolioTagArrayOutput `pulumi:"tags"`
}

// NewPortfolio registers a new resource with the given unique name, arguments, and options.
func NewPortfolio(ctx *pulumi.Context,
	name string, args *PortfolioArgs, opts ...pulumi.ResourceOption) (*Portfolio, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DisplayName == nil {
		return nil, errors.New("invalid value for required argument 'DisplayName'")
	}
	if args.ProviderName == nil {
		return nil, errors.New("invalid value for required argument 'ProviderName'")
	}
	var resource Portfolio
	err := ctx.RegisterResource("aws-native:servicecatalog:Portfolio", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPortfolio gets an existing Portfolio resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPortfolio(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PortfolioState, opts ...pulumi.ResourceOption) (*Portfolio, error) {
	var resource Portfolio
	err := ctx.ReadResource("aws-native:servicecatalog:Portfolio", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Portfolio resources.
type portfolioState struct {
}

type PortfolioState struct {
}

func (PortfolioState) ElementType() reflect.Type {
	return reflect.TypeOf((*portfolioState)(nil)).Elem()
}

type portfolioArgs struct {
	AcceptLanguage *string        `pulumi:"acceptLanguage"`
	Description    *string        `pulumi:"description"`
	DisplayName    string         `pulumi:"displayName"`
	ProviderName   string         `pulumi:"providerName"`
	Tags           []PortfolioTag `pulumi:"tags"`
}

// The set of arguments for constructing a Portfolio resource.
type PortfolioArgs struct {
	AcceptLanguage pulumi.StringPtrInput
	Description    pulumi.StringPtrInput
	DisplayName    pulumi.StringInput
	ProviderName   pulumi.StringInput
	Tags           PortfolioTagArrayInput
}

func (PortfolioArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*portfolioArgs)(nil)).Elem()
}

type PortfolioInput interface {
	pulumi.Input

	ToPortfolioOutput() PortfolioOutput
	ToPortfolioOutputWithContext(ctx context.Context) PortfolioOutput
}

func (*Portfolio) ElementType() reflect.Type {
	return reflect.TypeOf((**Portfolio)(nil)).Elem()
}

func (i *Portfolio) ToPortfolioOutput() PortfolioOutput {
	return i.ToPortfolioOutputWithContext(context.Background())
}

func (i *Portfolio) ToPortfolioOutputWithContext(ctx context.Context) PortfolioOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortfolioOutput)
}

type PortfolioOutput struct{ *pulumi.OutputState }

func (PortfolioOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Portfolio)(nil)).Elem()
}

func (o PortfolioOutput) ToPortfolioOutput() PortfolioOutput {
	return o
}

func (o PortfolioOutput) ToPortfolioOutputWithContext(ctx context.Context) PortfolioOutput {
	return o
}

func (o PortfolioOutput) AcceptLanguage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Portfolio) pulumi.StringPtrOutput { return v.AcceptLanguage }).(pulumi.StringPtrOutput)
}

func (o PortfolioOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Portfolio) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o PortfolioOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Portfolio) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

func (o PortfolioOutput) PortfolioName() pulumi.StringOutput {
	return o.ApplyT(func(v *Portfolio) pulumi.StringOutput { return v.PortfolioName }).(pulumi.StringOutput)
}

func (o PortfolioOutput) ProviderName() pulumi.StringOutput {
	return o.ApplyT(func(v *Portfolio) pulumi.StringOutput { return v.ProviderName }).(pulumi.StringOutput)
}

func (o PortfolioOutput) Tags() PortfolioTagArrayOutput {
	return o.ApplyT(func(v *Portfolio) PortfolioTagArrayOutput { return v.Tags }).(PortfolioTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PortfolioInput)(nil)).Elem(), &Portfolio{})
	pulumi.RegisterOutputType(PortfolioOutput{})
}
