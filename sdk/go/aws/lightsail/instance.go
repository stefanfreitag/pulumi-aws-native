// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lightsail

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Lightsail::Instance
type Instance struct {
	pulumi.CustomResourceState

	// An array of objects representing the add-ons to enable for the new instance.
	AddOns InstanceAddOnArrayOutput `pulumi:"addOns"`
	// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
	AvailabilityZone pulumi.StringPtrOutput `pulumi:"availabilityZone"`
	// The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
	BlueprintId pulumi.StringOutput `pulumi:"blueprintId"`
	// The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
	BundleId    pulumi.StringOutput       `pulumi:"bundleId"`
	Hardware    InstanceHardwarePtrOutput `pulumi:"hardware"`
	InstanceArn pulumi.StringOutput       `pulumi:"instanceArn"`
	// The names to use for your new Lightsail instance.
	InstanceName pulumi.StringOutput `pulumi:"instanceName"`
	// Is the IP Address of the Instance is the static IP
	IsStaticIp pulumi.BoolOutput `pulumi:"isStaticIp"`
	// The name of your key pair.
	KeyPairName pulumi.StringPtrOutput      `pulumi:"keyPairName"`
	Location    InstanceLocationPtrOutput   `pulumi:"location"`
	Networking  InstanceNetworkingPtrOutput `pulumi:"networking"`
	// Private IP Address of the Instance
	PrivateIpAddress pulumi.StringOutput `pulumi:"privateIpAddress"`
	// Public IP Address of the Instance
	PublicIpAddress pulumi.StringOutput `pulumi:"publicIpAddress"`
	// Resource type of Lightsail instance.
	ResourceType pulumi.StringOutput `pulumi:"resourceType"`
	// SSH Key Name of the  Lightsail instance.
	SshKeyName pulumi.StringOutput        `pulumi:"sshKeyName"`
	State      InstanceStateTypePtrOutput `pulumi:"state"`
	// Support code to help identify any issues
	SupportCode pulumi.StringOutput `pulumi:"supportCode"`
	// An array of key-value pairs to apply to this resource.
	Tags InstanceTagArrayOutput `pulumi:"tags"`
	// A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
	UserData pulumi.StringPtrOutput `pulumi:"userData"`
	// Username of the  Lightsail instance.
	UserName pulumi.StringOutput `pulumi:"userName"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BlueprintId == nil {
		return nil, errors.New("invalid value for required argument 'BlueprintId'")
	}
	if args.BundleId == nil {
		return nil, errors.New("invalid value for required argument 'BundleId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"availabilityZone",
		"blueprintId",
		"bundleId",
		"instanceName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Instance
	err := ctx.RegisterResource("aws-native:lightsail:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("aws-native:lightsail:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
}

type InstanceState struct {
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// An array of objects representing the add-ons to enable for the new instance.
	AddOns []InstanceAddOn `pulumi:"addOns"`
	// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
	BlueprintId string `pulumi:"blueprintId"`
	// The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
	BundleId string            `pulumi:"bundleId"`
	Hardware *InstanceHardware `pulumi:"hardware"`
	// The names to use for your new Lightsail instance.
	InstanceName *string `pulumi:"instanceName"`
	// The name of your key pair.
	KeyPairName *string             `pulumi:"keyPairName"`
	Location    *InstanceLocation   `pulumi:"location"`
	Networking  *InstanceNetworking `pulumi:"networking"`
	State       *InstanceStateType  `pulumi:"state"`
	// An array of key-value pairs to apply to this resource.
	Tags []InstanceTag `pulumi:"tags"`
	// A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
	UserData *string `pulumi:"userData"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// An array of objects representing the add-ons to enable for the new instance.
	AddOns InstanceAddOnArrayInput
	// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
	AvailabilityZone pulumi.StringPtrInput
	// The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
	BlueprintId pulumi.StringInput
	// The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
	BundleId pulumi.StringInput
	Hardware InstanceHardwarePtrInput
	// The names to use for your new Lightsail instance.
	InstanceName pulumi.StringPtrInput
	// The name of your key pair.
	KeyPairName pulumi.StringPtrInput
	Location    InstanceLocationPtrInput
	Networking  InstanceNetworkingPtrInput
	State       InstanceStateTypePtrInput
	// An array of key-value pairs to apply to this resource.
	Tags InstanceTagArrayInput
	// A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
	UserData pulumi.StringPtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

func (i *Instance) ToOutput(ctx context.Context) pulumix.Output[*Instance] {
	return pulumix.Output[*Instance]{
		OutputState: i.ToInstanceOutputWithContext(ctx).OutputState,
	}
}

type InstanceOutput struct{ *pulumi.OutputState }

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

func (o InstanceOutput) ToOutput(ctx context.Context) pulumix.Output[*Instance] {
	return pulumix.Output[*Instance]{
		OutputState: o.OutputState,
	}
}

// An array of objects representing the add-ons to enable for the new instance.
func (o InstanceOutput) AddOns() InstanceAddOnArrayOutput {
	return o.ApplyT(func(v *Instance) InstanceAddOnArrayOutput { return v.AddOns }).(InstanceAddOnArrayOutput)
}

// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
func (o InstanceOutput) AvailabilityZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.AvailabilityZone }).(pulumi.StringPtrOutput)
}

// The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
func (o InstanceOutput) BlueprintId() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.BlueprintId }).(pulumi.StringOutput)
}

// The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
func (o InstanceOutput) BundleId() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.BundleId }).(pulumi.StringOutput)
}

func (o InstanceOutput) Hardware() InstanceHardwarePtrOutput {
	return o.ApplyT(func(v *Instance) InstanceHardwarePtrOutput { return v.Hardware }).(InstanceHardwarePtrOutput)
}

func (o InstanceOutput) InstanceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.InstanceArn }).(pulumi.StringOutput)
}

// The names to use for your new Lightsail instance.
func (o InstanceOutput) InstanceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.InstanceName }).(pulumi.StringOutput)
}

// Is the IP Address of the Instance is the static IP
func (o InstanceOutput) IsStaticIp() pulumi.BoolOutput {
	return o.ApplyT(func(v *Instance) pulumi.BoolOutput { return v.IsStaticIp }).(pulumi.BoolOutput)
}

// The name of your key pair.
func (o InstanceOutput) KeyPairName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.KeyPairName }).(pulumi.StringPtrOutput)
}

func (o InstanceOutput) Location() InstanceLocationPtrOutput {
	return o.ApplyT(func(v *Instance) InstanceLocationPtrOutput { return v.Location }).(InstanceLocationPtrOutput)
}

func (o InstanceOutput) Networking() InstanceNetworkingPtrOutput {
	return o.ApplyT(func(v *Instance) InstanceNetworkingPtrOutput { return v.Networking }).(InstanceNetworkingPtrOutput)
}

// Private IP Address of the Instance
func (o InstanceOutput) PrivateIpAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.PrivateIpAddress }).(pulumi.StringOutput)
}

// Public IP Address of the Instance
func (o InstanceOutput) PublicIpAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.PublicIpAddress }).(pulumi.StringOutput)
}

// Resource type of Lightsail instance.
func (o InstanceOutput) ResourceType() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.ResourceType }).(pulumi.StringOutput)
}

// SSH Key Name of the  Lightsail instance.
func (o InstanceOutput) SshKeyName() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.SshKeyName }).(pulumi.StringOutput)
}

func (o InstanceOutput) State() InstanceStateTypePtrOutput {
	return o.ApplyT(func(v *Instance) InstanceStateTypePtrOutput { return v.State }).(InstanceStateTypePtrOutput)
}

// Support code to help identify any issues
func (o InstanceOutput) SupportCode() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.SupportCode }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o InstanceOutput) Tags() InstanceTagArrayOutput {
	return o.ApplyT(func(v *Instance) InstanceTagArrayOutput { return v.Tags }).(InstanceTagArrayOutput)
}

// A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.
func (o InstanceOutput) UserData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.UserData }).(pulumi.StringPtrOutput)
}

// Username of the  Lightsail instance.
func (o InstanceOutput) UserName() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.UserName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceInput)(nil)).Elem(), &Instance{})
	pulumi.RegisterOutputType(InstanceOutput{})
}
