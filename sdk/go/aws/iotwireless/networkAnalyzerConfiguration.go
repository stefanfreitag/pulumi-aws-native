// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotwireless

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Create and manage NetworkAnalyzerConfiguration resource.
type NetworkAnalyzerConfiguration struct {
	pulumi.CustomResourceState

	// Arn for network analyzer configuration, Returned upon successful create.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The description of the new resource
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the network analyzer configuration
	Name pulumi.StringOutput `pulumi:"name"`
	// An array of key-value pairs to apply to this resource.
	Tags NetworkAnalyzerConfigurationTagArrayOutput `pulumi:"tags"`
	// Trace content for your wireless gateway and wireless device resources
	TraceContent TraceContentPropertiesPtrOutput `pulumi:"traceContent"`
	// List of wireless gateway resources that have been added to the network analyzer configuration
	WirelessDevices pulumi.StringArrayOutput `pulumi:"wirelessDevices"`
	// List of wireless gateway resources that have been added to the network analyzer configuration
	WirelessGateways pulumi.StringArrayOutput `pulumi:"wirelessGateways"`
}

// NewNetworkAnalyzerConfiguration registers a new resource with the given unique name, arguments, and options.
func NewNetworkAnalyzerConfiguration(ctx *pulumi.Context,
	name string, args *NetworkAnalyzerConfigurationArgs, opts ...pulumi.ResourceOption) (*NetworkAnalyzerConfiguration, error) {
	if args == nil {
		args = &NetworkAnalyzerConfigurationArgs{}
	}

	var resource NetworkAnalyzerConfiguration
	err := ctx.RegisterResource("aws-native:iotwireless:NetworkAnalyzerConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkAnalyzerConfiguration gets an existing NetworkAnalyzerConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkAnalyzerConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkAnalyzerConfigurationState, opts ...pulumi.ResourceOption) (*NetworkAnalyzerConfiguration, error) {
	var resource NetworkAnalyzerConfiguration
	err := ctx.ReadResource("aws-native:iotwireless:NetworkAnalyzerConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkAnalyzerConfiguration resources.
type networkAnalyzerConfigurationState struct {
}

type NetworkAnalyzerConfigurationState struct {
}

func (NetworkAnalyzerConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkAnalyzerConfigurationState)(nil)).Elem()
}

type networkAnalyzerConfigurationArgs struct {
	// The description of the new resource
	Description *string `pulumi:"description"`
	// Name of the network analyzer configuration
	Name *string `pulumi:"name"`
	// An array of key-value pairs to apply to this resource.
	Tags []NetworkAnalyzerConfigurationTag `pulumi:"tags"`
	// Trace content for your wireless gateway and wireless device resources
	TraceContent *TraceContentProperties `pulumi:"traceContent"`
	// List of wireless gateway resources that have been added to the network analyzer configuration
	WirelessDevices []string `pulumi:"wirelessDevices"`
	// List of wireless gateway resources that have been added to the network analyzer configuration
	WirelessGateways []string `pulumi:"wirelessGateways"`
}

// The set of arguments for constructing a NetworkAnalyzerConfiguration resource.
type NetworkAnalyzerConfigurationArgs struct {
	// The description of the new resource
	Description pulumi.StringPtrInput
	// Name of the network analyzer configuration
	Name pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags NetworkAnalyzerConfigurationTagArrayInput
	// Trace content for your wireless gateway and wireless device resources
	TraceContent TraceContentPropertiesPtrInput
	// List of wireless gateway resources that have been added to the network analyzer configuration
	WirelessDevices pulumi.StringArrayInput
	// List of wireless gateway resources that have been added to the network analyzer configuration
	WirelessGateways pulumi.StringArrayInput
}

func (NetworkAnalyzerConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkAnalyzerConfigurationArgs)(nil)).Elem()
}

type NetworkAnalyzerConfigurationInput interface {
	pulumi.Input

	ToNetworkAnalyzerConfigurationOutput() NetworkAnalyzerConfigurationOutput
	ToNetworkAnalyzerConfigurationOutputWithContext(ctx context.Context) NetworkAnalyzerConfigurationOutput
}

func (*NetworkAnalyzerConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkAnalyzerConfiguration)(nil)).Elem()
}

func (i *NetworkAnalyzerConfiguration) ToNetworkAnalyzerConfigurationOutput() NetworkAnalyzerConfigurationOutput {
	return i.ToNetworkAnalyzerConfigurationOutputWithContext(context.Background())
}

func (i *NetworkAnalyzerConfiguration) ToNetworkAnalyzerConfigurationOutputWithContext(ctx context.Context) NetworkAnalyzerConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkAnalyzerConfigurationOutput)
}

type NetworkAnalyzerConfigurationOutput struct{ *pulumi.OutputState }

func (NetworkAnalyzerConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkAnalyzerConfiguration)(nil)).Elem()
}

func (o NetworkAnalyzerConfigurationOutput) ToNetworkAnalyzerConfigurationOutput() NetworkAnalyzerConfigurationOutput {
	return o
}

func (o NetworkAnalyzerConfigurationOutput) ToNetworkAnalyzerConfigurationOutputWithContext(ctx context.Context) NetworkAnalyzerConfigurationOutput {
	return o
}

// Arn for network analyzer configuration, Returned upon successful create.
func (o NetworkAnalyzerConfigurationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The description of the new resource
func (o NetworkAnalyzerConfigurationOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Name of the network analyzer configuration
func (o NetworkAnalyzerConfigurationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o NetworkAnalyzerConfigurationOutput) Tags() NetworkAnalyzerConfigurationTagArrayOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) NetworkAnalyzerConfigurationTagArrayOutput { return v.Tags }).(NetworkAnalyzerConfigurationTagArrayOutput)
}

// Trace content for your wireless gateway and wireless device resources
func (o NetworkAnalyzerConfigurationOutput) TraceContent() TraceContentPropertiesPtrOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) TraceContentPropertiesPtrOutput { return v.TraceContent }).(TraceContentPropertiesPtrOutput)
}

// List of wireless gateway resources that have been added to the network analyzer configuration
func (o NetworkAnalyzerConfigurationOutput) WirelessDevices() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) pulumi.StringArrayOutput { return v.WirelessDevices }).(pulumi.StringArrayOutput)
}

// List of wireless gateway resources that have been added to the network analyzer configuration
func (o NetworkAnalyzerConfigurationOutput) WirelessGateways() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NetworkAnalyzerConfiguration) pulumi.StringArrayOutput { return v.WirelessGateways }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkAnalyzerConfigurationInput)(nil)).Elem(), &NetworkAnalyzerConfiguration{})
	pulumi.RegisterOutputType(NetworkAnalyzerConfigurationOutput{})
}
