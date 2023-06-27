// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotfleetwise

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::IoTFleetWise::SignalCatalog Resource Type
//
// Deprecated: SignalCatalog is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type SignalCatalog struct {
	pulumi.CustomResourceState

	Arn                  pulumi.StringOutput              `pulumi:"arn"`
	CreationTime         pulumi.StringOutput              `pulumi:"creationTime"`
	Description          pulumi.StringPtrOutput           `pulumi:"description"`
	LastModificationTime pulumi.StringOutput              `pulumi:"lastModificationTime"`
	Name                 pulumi.StringPtrOutput           `pulumi:"name"`
	NodeCounts           SignalCatalogNodeCountsPtrOutput `pulumi:"nodeCounts"`
	Nodes                SignalCatalogNodeArrayOutput     `pulumi:"nodes"`
	Tags                 SignalCatalogTagArrayOutput      `pulumi:"tags"`
}

// NewSignalCatalog registers a new resource with the given unique name, arguments, and options.
func NewSignalCatalog(ctx *pulumi.Context,
	name string, args *SignalCatalogArgs, opts ...pulumi.ResourceOption) (*SignalCatalog, error) {
	if args == nil {
		args = &SignalCatalogArgs{}
	}

	var resource SignalCatalog
	err := ctx.RegisterResource("aws-native:iotfleetwise:SignalCatalog", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSignalCatalog gets an existing SignalCatalog resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSignalCatalog(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SignalCatalogState, opts ...pulumi.ResourceOption) (*SignalCatalog, error) {
	var resource SignalCatalog
	err := ctx.ReadResource("aws-native:iotfleetwise:SignalCatalog", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SignalCatalog resources.
type signalCatalogState struct {
}

type SignalCatalogState struct {
}

func (SignalCatalogState) ElementType() reflect.Type {
	return reflect.TypeOf((*signalCatalogState)(nil)).Elem()
}

type signalCatalogArgs struct {
	Description *string                  `pulumi:"description"`
	Name        *string                  `pulumi:"name"`
	NodeCounts  *SignalCatalogNodeCounts `pulumi:"nodeCounts"`
	Nodes       []SignalCatalogNode      `pulumi:"nodes"`
	Tags        []SignalCatalogTag       `pulumi:"tags"`
}

// The set of arguments for constructing a SignalCatalog resource.
type SignalCatalogArgs struct {
	Description pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	NodeCounts  SignalCatalogNodeCountsPtrInput
	Nodes       SignalCatalogNodeArrayInput
	Tags        SignalCatalogTagArrayInput
}

func (SignalCatalogArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*signalCatalogArgs)(nil)).Elem()
}

type SignalCatalogInput interface {
	pulumi.Input

	ToSignalCatalogOutput() SignalCatalogOutput
	ToSignalCatalogOutputWithContext(ctx context.Context) SignalCatalogOutput
}

func (*SignalCatalog) ElementType() reflect.Type {
	return reflect.TypeOf((**SignalCatalog)(nil)).Elem()
}

func (i *SignalCatalog) ToSignalCatalogOutput() SignalCatalogOutput {
	return i.ToSignalCatalogOutputWithContext(context.Background())
}

func (i *SignalCatalog) ToSignalCatalogOutputWithContext(ctx context.Context) SignalCatalogOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SignalCatalogOutput)
}

type SignalCatalogOutput struct{ *pulumi.OutputState }

func (SignalCatalogOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SignalCatalog)(nil)).Elem()
}

func (o SignalCatalogOutput) ToSignalCatalogOutput() SignalCatalogOutput {
	return o
}

func (o SignalCatalogOutput) ToSignalCatalogOutputWithContext(ctx context.Context) SignalCatalogOutput {
	return o
}

func (o SignalCatalogOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *SignalCatalog) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o SignalCatalogOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *SignalCatalog) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

func (o SignalCatalogOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SignalCatalog) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o SignalCatalogOutput) LastModificationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *SignalCatalog) pulumi.StringOutput { return v.LastModificationTime }).(pulumi.StringOutput)
}

func (o SignalCatalogOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SignalCatalog) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o SignalCatalogOutput) NodeCounts() SignalCatalogNodeCountsPtrOutput {
	return o.ApplyT(func(v *SignalCatalog) SignalCatalogNodeCountsPtrOutput { return v.NodeCounts }).(SignalCatalogNodeCountsPtrOutput)
}

func (o SignalCatalogOutput) Nodes() SignalCatalogNodeArrayOutput {
	return o.ApplyT(func(v *SignalCatalog) SignalCatalogNodeArrayOutput { return v.Nodes }).(SignalCatalogNodeArrayOutput)
}

func (o SignalCatalogOutput) Tags() SignalCatalogTagArrayOutput {
	return o.ApplyT(func(v *SignalCatalog) SignalCatalogTagArrayOutput { return v.Tags }).(SignalCatalogTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SignalCatalogInput)(nil)).Elem(), &SignalCatalog{})
	pulumi.RegisterOutputType(SignalCatalogOutput{})
}
