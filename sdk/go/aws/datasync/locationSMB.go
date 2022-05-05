// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::LocationSMB.
type LocationSMB struct {
	pulumi.CustomResourceState

	// The Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.
	AgentArns pulumi.StringArrayOutput `pulumi:"agentArns"`
	// The name of the Windows domain that the SMB server belongs to.
	Domain pulumi.StringPtrOutput `pulumi:"domain"`
	// The Amazon Resource Name (ARN) of the SMB location that is created.
	LocationArn pulumi.StringOutput `pulumi:"locationArn"`
	// The URL of the SMB location that was described.
	LocationUri  pulumi.StringOutput              `pulumi:"locationUri"`
	MountOptions LocationSMBMountOptionsPtrOutput `pulumi:"mountOptions"`
	// The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
	Password pulumi.StringOutput `pulumi:"password"`
	// The name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server.
	ServerHostname pulumi.StringOutput `pulumi:"serverHostname"`
	// The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination
	Subdirectory pulumi.StringOutput `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags LocationSMBTagArrayOutput `pulumi:"tags"`
	// The user who can mount the share, has the permissions to access files and folders in the SMB share.
	User pulumi.StringOutput `pulumi:"user"`
}

// NewLocationSMB registers a new resource with the given unique name, arguments, and options.
func NewLocationSMB(ctx *pulumi.Context,
	name string, args *LocationSMBArgs, opts ...pulumi.ResourceOption) (*LocationSMB, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AgentArns == nil {
		return nil, errors.New("invalid value for required argument 'AgentArns'")
	}
	if args.Password == nil {
		return nil, errors.New("invalid value for required argument 'Password'")
	}
	if args.ServerHostname == nil {
		return nil, errors.New("invalid value for required argument 'ServerHostname'")
	}
	if args.Subdirectory == nil {
		return nil, errors.New("invalid value for required argument 'Subdirectory'")
	}
	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	var resource LocationSMB
	err := ctx.RegisterResource("aws-native:datasync:LocationSMB", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLocationSMB gets an existing LocationSMB resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLocationSMB(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LocationSMBState, opts ...pulumi.ResourceOption) (*LocationSMB, error) {
	var resource LocationSMB
	err := ctx.ReadResource("aws-native:datasync:LocationSMB", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LocationSMB resources.
type locationSMBState struct {
}

type LocationSMBState struct {
}

func (LocationSMBState) ElementType() reflect.Type {
	return reflect.TypeOf((*locationSMBState)(nil)).Elem()
}

type locationSMBArgs struct {
	// The Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.
	AgentArns []string `pulumi:"agentArns"`
	// The name of the Windows domain that the SMB server belongs to.
	Domain       *string                  `pulumi:"domain"`
	MountOptions *LocationSMBMountOptions `pulumi:"mountOptions"`
	// The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
	Password string `pulumi:"password"`
	// The name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server.
	ServerHostname string `pulumi:"serverHostname"`
	// The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination
	Subdirectory string `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags []LocationSMBTag `pulumi:"tags"`
	// The user who can mount the share, has the permissions to access files and folders in the SMB share.
	User string `pulumi:"user"`
}

// The set of arguments for constructing a LocationSMB resource.
type LocationSMBArgs struct {
	// The Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.
	AgentArns pulumi.StringArrayInput
	// The name of the Windows domain that the SMB server belongs to.
	Domain       pulumi.StringPtrInput
	MountOptions LocationSMBMountOptionsPtrInput
	// The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
	Password pulumi.StringInput
	// The name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server.
	ServerHostname pulumi.StringInput
	// The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination
	Subdirectory pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	Tags LocationSMBTagArrayInput
	// The user who can mount the share, has the permissions to access files and folders in the SMB share.
	User pulumi.StringInput
}

func (LocationSMBArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*locationSMBArgs)(nil)).Elem()
}

type LocationSMBInput interface {
	pulumi.Input

	ToLocationSMBOutput() LocationSMBOutput
	ToLocationSMBOutputWithContext(ctx context.Context) LocationSMBOutput
}

func (*LocationSMB) ElementType() reflect.Type {
	return reflect.TypeOf((**LocationSMB)(nil)).Elem()
}

func (i *LocationSMB) ToLocationSMBOutput() LocationSMBOutput {
	return i.ToLocationSMBOutputWithContext(context.Background())
}

func (i *LocationSMB) ToLocationSMBOutputWithContext(ctx context.Context) LocationSMBOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LocationSMBOutput)
}

type LocationSMBOutput struct{ *pulumi.OutputState }

func (LocationSMBOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LocationSMB)(nil)).Elem()
}

func (o LocationSMBOutput) ToLocationSMBOutput() LocationSMBOutput {
	return o
}

func (o LocationSMBOutput) ToLocationSMBOutputWithContext(ctx context.Context) LocationSMBOutput {
	return o
}

// The Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.
func (o LocationSMBOutput) AgentArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringArrayOutput { return v.AgentArns }).(pulumi.StringArrayOutput)
}

// The name of the Windows domain that the SMB server belongs to.
func (o LocationSMBOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringPtrOutput { return v.Domain }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the SMB location that is created.
func (o LocationSMBOutput) LocationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringOutput { return v.LocationArn }).(pulumi.StringOutput)
}

// The URL of the SMB location that was described.
func (o LocationSMBOutput) LocationUri() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringOutput { return v.LocationUri }).(pulumi.StringOutput)
}

func (o LocationSMBOutput) MountOptions() LocationSMBMountOptionsPtrOutput {
	return o.ApplyT(func(v *LocationSMB) LocationSMBMountOptionsPtrOutput { return v.MountOptions }).(LocationSMBMountOptionsPtrOutput)
}

// The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
func (o LocationSMBOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// The name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server.
func (o LocationSMBOutput) ServerHostname() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringOutput { return v.ServerHostname }).(pulumi.StringOutput)
}

// The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination
func (o LocationSMBOutput) Subdirectory() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringOutput { return v.Subdirectory }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LocationSMBOutput) Tags() LocationSMBTagArrayOutput {
	return o.ApplyT(func(v *LocationSMB) LocationSMBTagArrayOutput { return v.Tags }).(LocationSMBTagArrayOutput)
}

// The user who can mount the share, has the permissions to access files and folders in the SMB share.
func (o LocationSMBOutput) User() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationSMB) pulumi.StringOutput { return v.User }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LocationSMBInput)(nil)).Elem(), &LocationSMB{})
	pulumi.RegisterOutputType(LocationSMBOutput{})
}
