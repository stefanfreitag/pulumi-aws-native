// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicediscovery

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ServiceDiscovery::PrivateDnsNamespace
//
// Deprecated: PrivateDnsNamespace is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type PrivateDnsNamespace struct {
	pulumi.CustomResourceState

	Arn          pulumi.StringOutput                    `pulumi:"arn"`
	Description  pulumi.StringPtrOutput                 `pulumi:"description"`
	HostedZoneId pulumi.StringOutput                    `pulumi:"hostedZoneId"`
	Name         pulumi.StringOutput                    `pulumi:"name"`
	Properties   PrivateDnsNamespacePropertiesPtrOutput `pulumi:"properties"`
	Tags         PrivateDnsNamespaceTagArrayOutput      `pulumi:"tags"`
	Vpc          pulumi.StringOutput                    `pulumi:"vpc"`
}

// NewPrivateDnsNamespace registers a new resource with the given unique name, arguments, and options.
func NewPrivateDnsNamespace(ctx *pulumi.Context,
	name string, args *PrivateDnsNamespaceArgs, opts ...pulumi.ResourceOption) (*PrivateDnsNamespace, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Vpc == nil {
		return nil, errors.New("invalid value for required argument 'Vpc'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"vpc",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource PrivateDnsNamespace
	err := ctx.RegisterResource("aws-native:servicediscovery:PrivateDnsNamespace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrivateDnsNamespace gets an existing PrivateDnsNamespace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrivateDnsNamespace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PrivateDnsNamespaceState, opts ...pulumi.ResourceOption) (*PrivateDnsNamespace, error) {
	var resource PrivateDnsNamespace
	err := ctx.ReadResource("aws-native:servicediscovery:PrivateDnsNamespace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PrivateDnsNamespace resources.
type privateDnsNamespaceState struct {
}

type PrivateDnsNamespaceState struct {
}

func (PrivateDnsNamespaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*privateDnsNamespaceState)(nil)).Elem()
}

type privateDnsNamespaceArgs struct {
	Description *string                        `pulumi:"description"`
	Name        *string                        `pulumi:"name"`
	Properties  *PrivateDnsNamespaceProperties `pulumi:"properties"`
	Tags        []PrivateDnsNamespaceTag       `pulumi:"tags"`
	Vpc         string                         `pulumi:"vpc"`
}

// The set of arguments for constructing a PrivateDnsNamespace resource.
type PrivateDnsNamespaceArgs struct {
	Description pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	Properties  PrivateDnsNamespacePropertiesPtrInput
	Tags        PrivateDnsNamespaceTagArrayInput
	Vpc         pulumi.StringInput
}

func (PrivateDnsNamespaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*privateDnsNamespaceArgs)(nil)).Elem()
}

type PrivateDnsNamespaceInput interface {
	pulumi.Input

	ToPrivateDnsNamespaceOutput() PrivateDnsNamespaceOutput
	ToPrivateDnsNamespaceOutputWithContext(ctx context.Context) PrivateDnsNamespaceOutput
}

func (*PrivateDnsNamespace) ElementType() reflect.Type {
	return reflect.TypeOf((**PrivateDnsNamespace)(nil)).Elem()
}

func (i *PrivateDnsNamespace) ToPrivateDnsNamespaceOutput() PrivateDnsNamespaceOutput {
	return i.ToPrivateDnsNamespaceOutputWithContext(context.Background())
}

func (i *PrivateDnsNamespace) ToPrivateDnsNamespaceOutputWithContext(ctx context.Context) PrivateDnsNamespaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrivateDnsNamespaceOutput)
}

func (i *PrivateDnsNamespace) ToOutput(ctx context.Context) pulumix.Output[*PrivateDnsNamespace] {
	return pulumix.Output[*PrivateDnsNamespace]{
		OutputState: i.ToPrivateDnsNamespaceOutputWithContext(ctx).OutputState,
	}
}

type PrivateDnsNamespaceOutput struct{ *pulumi.OutputState }

func (PrivateDnsNamespaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PrivateDnsNamespace)(nil)).Elem()
}

func (o PrivateDnsNamespaceOutput) ToPrivateDnsNamespaceOutput() PrivateDnsNamespaceOutput {
	return o
}

func (o PrivateDnsNamespaceOutput) ToPrivateDnsNamespaceOutputWithContext(ctx context.Context) PrivateDnsNamespaceOutput {
	return o
}

func (o PrivateDnsNamespaceOutput) ToOutput(ctx context.Context) pulumix.Output[*PrivateDnsNamespace] {
	return pulumix.Output[*PrivateDnsNamespace]{
		OutputState: o.OutputState,
	}
}

func (o PrivateDnsNamespaceOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o PrivateDnsNamespaceOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o PrivateDnsNamespaceOutput) HostedZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) pulumi.StringOutput { return v.HostedZoneId }).(pulumi.StringOutput)
}

func (o PrivateDnsNamespaceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o PrivateDnsNamespaceOutput) Properties() PrivateDnsNamespacePropertiesPtrOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) PrivateDnsNamespacePropertiesPtrOutput { return v.Properties }).(PrivateDnsNamespacePropertiesPtrOutput)
}

func (o PrivateDnsNamespaceOutput) Tags() PrivateDnsNamespaceTagArrayOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) PrivateDnsNamespaceTagArrayOutput { return v.Tags }).(PrivateDnsNamespaceTagArrayOutput)
}

func (o PrivateDnsNamespaceOutput) Vpc() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateDnsNamespace) pulumi.StringOutput { return v.Vpc }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PrivateDnsNamespaceInput)(nil)).Elem(), &PrivateDnsNamespace{})
	pulumi.RegisterOutputType(PrivateDnsNamespaceOutput{})
}
